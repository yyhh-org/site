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
pyenv install 3.6.6
pyenv global 3.6.6
```

Now install needed software:

```bash
pip install pelican pelican-alias invoke livereload markdown beautifulsoup4
```

## Test

After you edit the documents, you can test the site by starting a dev-server:

```bash
invoke livereload

```
And point browser to http://localhost:8000

The dev-server also supports auto-reloading, and will rebuild your documentation whenever anything changes.


## Deploy

After the ssh key to our host server has been set, just do

```bash
invoke publish

```

## Upgrade software

Just append --upgrade to the install command, eg. 

```bash
pip install pelican pelican-alias invoke livereload markdown beautifulsoup4 --upgrade
```

