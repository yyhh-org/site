# yyhh.org source

This is the source for https://yyhh.org. The site is built with [pelican](https://getpelican.com).

## Setup

First pull the submodules

```bash
git submodule update --init
```

Use Python 3.11, matching the Netlify build environment in `netlify.toml`.

```bash
brew install pyenv
pyenv install 3.11
pyenv local 3.11
```
Then follow the instruction in `pyenv init`.

Also need node.js for Web based editor

```bash
brew install node
```

Now install needed libary:

```bash
pip install -r requirements.txt
```

## Write and Test Locally

Run or click on `write-blog` command

Then point browser to http://localhost:8000/admin to start writing the blog using a Web UI.

Fill in the Description field with one or two short sentences in the post's language. When editing Markdown directly, use a `Summary:` field in the front matter. The theme uses it for article previews and description metadata.

After finish writing and hit publish button, the blog is published locally,  point browser to http://localhost:8000 to view the blog live locally.

The dev-server supports auto-reloading, and will rebuild your documentation whenever anything changes. It's a bit slow, need to wait for 30 seconds or so for the build to finish.

## Publish to yyhh.org

Push to the GitHub repository's `master` branch to trigger the automatic Netlify build and deployment. The Python version is configured in `netlify.toml`.

For the legacy SSH deployment, after the ssh key to the host server has been set, run or click on `publish-blog`.

## Stop Writing without Publish

If you want to stop the local Web server without publishing the changes, run or click on `stop-blog`

## Upgrade software

Just append --upgrade to the install command, eg.

```bash
pip install --upgrade -r requirements.txt
```
