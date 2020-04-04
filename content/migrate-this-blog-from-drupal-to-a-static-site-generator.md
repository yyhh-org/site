---
Title: Migrate this blog from Drupal to a static site generator
Date: 2020-03-10T19:34:39.357Z
Author: Huahai
Category: notebook
Tags: 'Drupal, SSG, Pelican, SysAdmin'
Lang: en
Status: published
---
This blog has undergone a few migrations over its 15 years life span. 

It started out as a Blogger account in 2005. The purpose was to record some system administration details when I was an assistant professor at university, setting up my laboratry for students.   

Then Yunyao joined in after I moved the blog to a self hosted Drupal 5 installation in 2007. It has been with the same hosting company ever since, and I upgraded Drupal all the way to version 8.

But this old hosting account started to show limitations a couple of years ago. The technical specification simply could no longer keep up with the demands of modern PHP applications, which universally require the use of composer as a dependency manager. 

Composer always ran out of memory in this very modest environment (512M memory limit). It took some effort to keep Drupal up to date without the modern tools. The final straw is an error that prevented us from creating new posts. It's likely a database error, but I could not investigate properly without tools such as drush. 

So it is finally the time to move on. A static site generator (SSG) seems to be a good fit. Since the host only needs to serve static files, the limitation with my host account is not a concern any more. 

### Jekyll, Hugo and Pelican

There are perhaps hundreds of options for SSG. After some reading, I tried Jekyll, Hugo and Pelican. In the end, Pelican is the one that I got it to work, so here we are.

The first problem I needed to solve is to get the content out of Drupal and feed them into the SSG system.  

Both Jekyll and Hugo have importers for Drupal 6 and 7 that directly import from the Drupal database.  However none of them work with Drupal 8, which has some significant database schema changes.  

I had some trouble compiling Ruby mysql library needed for Jekyll importer, so I gave up early on  Jekyll. 

On to Hugo, I quickly realized that I did not have the time to figure out the intricacy of the Drupal 8 database schema to adapt its Drupal 7 importer to 8. By the way, I also dislike golang the language, for I think it is reactionary (but that's for another post), so I gave it up. 

On the other hand, Pelican has an RSS feed importer, which I easily modified the python code to extract the pieces needed for the frontmatter of Pelican. Since each Drupal installation is different, the resulting HTML could be very different. Having an easy to hack importer helps a lot.  

The lesson seems to be that a feed importer is better than a database importer for a  blog platform, since all the useful information are in the feed. There should not be a need to bother with databases, which tend to evolve a lot from one version to another. Feed format is universal. 

### Pelican and NetlifyCMS

After some minor cleanup of the markdown files generated from the feed importer, I quickly switched the live site to Pelican. I then pushed the whole thing to a github repository and thought I was done. Then Yunyao said she wanted a Web based editor like before, instead of having to write blogs like writing programming code. 

That means we need a headless CMS to pair with Pelican. Again, there are so many options, and I just picked the first one that come into my head, NetlifyCMS. It includes simply two files that you drop into the content directory under `/admin`. It provides a react.js app with a nice editor for writing the posts in WYSIWYG fashion. 

![netlify screenshot](/images/uploads/screen-shot-2020-03-10-at-1.54.57-pm.png "Screenshot of Netlify CMS")

The form widgets for the frontmatter fields are a big help. Otherwise, I will have to copy an old post as the template to write new ones. The configuration of these widgets in a `config.yml` file is quite nice and easy.

```yml
backend:
  name: git-gateway

local_backend: true
    
media_folder: "content/images/uploads" # Folder where user uploaded files should go
public_folder: "/images/uploads"

collections: # A list of collections the CMS should be able to edit
  - name: "blog" # Used in routes, ie.: /admin/collections/:slug/edit
    identifier_field: "Title"
    label: "Article" # Used in the UI, ie.: "New Post"
    folder: "content" # The path to the folder where the documents are stored
    extension: md
    format: frontmatter
    create: true # Allow users to create new documents in this collection
    slug: "{{slug}}" # Filename template, e.g., title.md
    fields: # The fields each document in this collection have
      - {label: "Title", name: "Title", widget: "string"}
      - {label: "Date", name: "Date", widget: "datetime"}
      - {label: "Author", name: "Author", widget: "select", default: "Yunyao", options: ["Yunyao", "Huahai"]}
      - {label: "Category", name: "Category", widget: "select", default: "experience", options: ["experience", "notebook", "opinion"], hint: "Select category"}
      - {label: "Tags", name: "Tags", widget: "string", hint: "Enter comma-separated words"}
      - {label: "Series", name: "Series", widget: "string", required: false, hint: "Give multiple related articles a series name"}
      - {label: "Language", name: "Lang", widget: "select", default: "en", options: ["en", "zh"], hint: "Select en for English, zh for 中文"}
      - {label: "Status", name: "Status", widget: "select", default: "published", options: ["draft", "published"], hint: "Draft does not show on site"}
      - {label: "Body", name: "body", widget: "markdown"}
```

 I am also taking advantage of its beta feature: local development. So I can write a bash script to `write-blog`:

```bash
#!/bin/bash

cd -- "$(dirname "$0")"

set -m 

git pull 

npx netlify-cms-proxy-server &
echo $! > npx.pid

invoke livereload &
echo $! > invoke.pid

echo "------------------------------------------------------------"

echo "Go to https://localhost:8000/admin to edit blog"
echo "Go to https://localhost:8000 to view blog"

echo "Don't forget to run 'publish-blog' to publish the blog to yyhh.org"

echo "------------------------------------------------------------"

fg
```

and to `publish-blog`

```bash
#!/bin/bash

cd -- "$(dirname "$0")"

kill -9 `cat npx.pid`
kill -9 `cat invoke.pid`

git add -A
git commit -am "publish blog"
git push

invoke publish

echo "Blog published at https://yyhh.org"
```

### Good and Bad

This setup works nicely. Obviously, the site loads much faster, as it just serves static files.

Pelican also gets me some new features that I did not have before. The i18n subsite feature allows us to separate English and Chinese content completely, so people do not have to read things they cannot understand. The translation configuration with gettext and po files works pretty well.  

Pelican is pretty old in term of "the latest and the greatest" technology fad, so there is not a lot of activities going on. There are not many themes that are actively updated. It is however sufficient for a personal blog.

The main concern is the slowness of the build. It would take about 50 seconds to build this site on my laptop (albeit a very old one). As more content is added, it would get worse. So I will definitely switch again in the future. 

On the other hand, with the help of NetlifyCMS, the authoring is not affected too much by the slow build, because the CMS already gives us immediate feedback on the page we are editing. The build is only kicked off when we hit the publish button. So for now, I am OK with this setup. 
