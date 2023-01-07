# yyhh.org source

This is the source for https://yyhh.org. The site is built with [pelican](https://getpelican.com).

## Setup

First pull the submodules

```bash
git submodule update --init
```

Make sure you have python on your system. It is safer to use the same version of python as we do.

```bash
brew install pyenv
pyenv install 3.8.16
pyenv global 3.8.16
```

Also need node.js for Web based editor

```bash
brew install node
```

Now install needed libary:

```bash
pip install pelican pelican-alias invoke livereload markdown beautifulsoup4
```

## Write and Test Locally

Run or click on `write-blog` command

Then point browser to http://localhost:8000/admin to start writing the blog using a Web UI.

After finish writing and hit publish button, the blog is published locally,  point browser to http://localhost:8000 to view the blog live locally.

The dev-server supports auto-reloading, and will rebuild your documentation whenever anything changes. It's a bit slow, need to wait for 30 seconds or so for the build to finish.

## Publish to yyhh.org

After the ssh key to the host server has been set, just run or click on `publish-blog`

## Stop Writing without Publish

If you want to stop the local Web server without publishing the changes, run or click on `stop-blog`

## Upgrade software

Just append --upgrade to the install command, eg.

```bash
pip install pelican pelican-alias invoke livereload markdown beautifulsoup4 --upgrade
```
