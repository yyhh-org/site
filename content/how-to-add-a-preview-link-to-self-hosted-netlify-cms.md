---
Status: draft
Lang: en
Title: How to Add a Preview Link to Self-hosted Netlify CMS
Date: 2020-04-09T21:47:15.849Z
Author: Huahai
Category: notebook
Tags: SSG, Netlify CMS, Jenkins, Github, nginx, SysAdmin
---
If you are using a self-hosted  Netlify CMS as the online editor for your SSG powered Website and you are using the editorial workflow (you have `publish_mode: editorial_workflow` in your config.yml), a pain point is that you do not see a preview of the live page when the page is in draft. Unlike the master branch that you can  see the live page after it is built, the draft is committed to a different git branch so you do not have a link to the built page.

Sure, you always have a preview on the right panel in Netlify CMS, but this preview does not look like the real page. Even if you use `CMS.registerPreviewStyle` to register a stylesheet that matches your live page style, you still miss all the other parts, such the header, footer and sidebar, so you don't know how the whole page looks like until the page is published.

![Preview link in Netlify CMS](/images/uploads/screen-shot-2020-04-09-at-4.10.24-pm.png "Preview link in Netlify CMS")

Netlify CMS has a feature to show a preview link for drafts, but one needs to do some setup to make it shows up. Right now, this feature only supports github as the git backend. Here I will show how I work with github, Jenkins and nginx to supply a preview link to Netlify CMS. 

Before we begin, here's what we already have. We use a github organization, say example-com to host the repository for the site, so `example-com/site` would be the repo. The site source contains a Jenkinsfile, so when the repo is committed to, Jenkins automatically builds the site using its github integration. 

We also set up nginx to directly point to the built site directory as the root. We are using eleventy as the SSG, so the built site is in `_site` directory. This works well for automatic deployment of the site. Whenever the master branch of the source repository is committed to, after a few seconds, the web server's `<jenkins-agent-home>/workspace/<jenkins-job-name>_master/_site` directory will contain the updated site content for https://example.com

To add a preview link, we basically need to do the same for the preview branch, `PR-5`, a pull-request to github sent by Netlify. There are a few things need to happen.

## DNS

We need to setup a wildcard DNS record, so that HTTP requests to places such as `PR-5.example.com`, `PR-11.example.com`  goes to the IP address of the Web server. Basically, you need to add an `A` record for `*.example.com`.

## Nginx

On the Web server, we need to setup nginx to look for these PR host names, and dynamically set the site root to point to the correct Jenkins workspace directory. For example, `PR-5.example.com` should have `<jenkins-agent-home>/workspace/<jenkins-job-name>_PR-5/_site` as the root. To do that, first edit `/etc/nginx/nginx.conf`, add in the `http` context the following:

```
	map $http_host $rootpath {
		~^(?<pr>pr\-.+)\.example\.com$  $pr;
	}
```

This will capture the `PR-5` part of the hostname, and put it in `$rootpath` variable.

Then create a nginx site conf for the PR sites, say, `/etc/nginx/site-enabled/pr.conf`,

```
server {

	# SSL configuration
	#
	listen 443 ssl;
	listen [::]:443 ssl;

	ssl                  on;
	ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

        ssl_session_timeout  5m;
        ssl_ciphers  HIGH:!aNULL:!MD5;

	server_name ~^pr\-.+\.example\.com$;

	set_by_lua $pr "return string.upper(ngx.var.rootpath)";
	root /home/jenkins-slave/workspace/example-com_site_$pr/_site;

	location / {
		index index.html;
	}
}
```

Because DNS is case insensitive, it will not preserve the uppercase of PR-5.example.com, we will have to use lua to uppercase it to match the case sensitive directory path. 

Notice also that we have a wildcard SSL certificate from Lets' Encrypt for `*.example.com`.

## Jenkinsfile

On Jenkins, just setup a job that use a Jenkinsfile. My Jenkinsfile in the site source looks like this:

```
#!/usr/bin/env groovy

pipeline {
  agent { label 'web' }
  environment {
    GITHUB_ACCESS_TOKEN = credentials('GITHUB_ACCESS_TOKEN')
  }
  stages {
    stage('Build') {
      steps {
        sh "env"
        script {
          if (env.BRANCH_NAME.startsWith("PR-")) {
            env.BUILD_INFO = "<${env.RUN_DISPLAY_URL}|${env.JOB_NAME} [${env.BUILD_NUMBER}]> submitted by ${env.CHANGE_AUTHOR} with PR <https://github.com/example-com/site/pull/${CHANGE_ID}|#${env.CHANGE_ID}>: ${env.CHANGE_TITLE}"
          } else {
            env.GIT_COMMIT_MSG = sh (
              script: "git log --format=%B -n 1 ${env.GIT_COMMIT} | head -n 1",
              returnStdout: true).trim()
            env.GIT_AUTHOR_NAME = sh (
              script: "git show -s --pretty=%an ${env.GIT_COMMIT}",
              returnStdout: true).trim()
            env.BUILD_INFO = "<${env.RUN_DISPLAY_URL}|${env.JOB_NAME} [${env.BUILD_NUMBER}]> submitted by ${env.GIT_AUTHOR_NAME} with commit <https://github.com/juji-io/site/commit/${env.GIT_COMMIT}|${env.GIT_COMMIT.take(7)}>: ${env.GIT_COMMIT_MSG}"
          }
        }
        sh '''
          npm install
          npx @11ty/eleventy
        '''
      }
    }
  }
  post {
    success {
      script {
        if (env.BRANCH_NAME.startsWith("PR-")) {
          sh '''
              GIT_PR_COMMIT=$(git show-ref -s "refs/remotes/origin/${BRANCH_NAME}")
              curl -X POST -H "Content-Type:application/json" \
              -H "Authorization: token ${GITHUB_ACCESS_TOKEN}" \
              -d '{"state": "success", "context": "netlify-cms/preview/deploy", "description": "Deploy preview ready", "target_url": "https://'"${BRANCH_NAME}"'.example.com/"}' \
              "https://api.github.com/repos/juji-io/site/statuses/${GIT_PR_COMMIT}"
          '''
          }
      }
      slackSend (color: '#00FF00', message: "SUCCESSFUL: Job ${env.BUILD_INFO}")
    }
    aborted {
      slackSend (color: '#FF00FF', message: "ABORTED: Job ${env.BUILD_INFO}")
    }
    notBuilt {
      slackSend (color: '#AAAAAA', message: "NOT_BUILT: Job ${env.BUILD_INFO}")
    }
    unstable {
      slackSend (color: '#FFFF00', message: "UNSTABLE: Job ${env.BUILD_INFO}")
    }
  }
}
```

On github, I have created a personal access token, and added the token in Jenkins credentials as `GITHUB_ACCESS_TOKEN`. 

You can see that we are sending build status to slack, but that's not important. The important part is in the additional step in the post success script, where we use curl to send a POST request to github statuses API to report a successful preview deployment (as a pull request). All the information needed for the preview link is in the JSON payload

```
{ 
  "state": "success", 
  "context": "netlify-cms/preview/deploy", 
  "description": "Deploy preview ready", 
  "target_url": "https://'"${BRANCH_NAME}"'.example.com/"
}
```

The `state` is required. The `context` is what I made up, but it is important to have the keyword "deploy" in there, as that's what Netlify CMS is looking for. The `description` can be whatever. The `target_url` is the preview link we are after!  

## Netlify CMS config.yml

If you want the preview link to point to the draft article itself, you will need to add a `preview_path` in the collection in config.yml. For example, `preview_path: blog/{{slug}}`. 

Wow, all these, just for a link. Oh well, without this link, your writers and editors will probably be mad at you, so it definitely worth it.