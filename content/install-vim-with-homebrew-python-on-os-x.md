---
Status: published
Title: Install Vim with Homebrew Python on OS X
Date: 2012-05-16 04:50
Author: Huahai
Category: notebook
Tags: Editor, Vim, OSX
Slug: install-vim-with-homebrew-python-on-os-x
Alias: /blog/2012/05/install-vim-homebrew-python-os-x
Lang: en
---

For people that need full features of vim, the default installation of vim on Mac OS X is definitely not enough. For example, I need to [use vim to post to this blog](https://yyhh.org/blog/2007/10/posting-blog-entry-drupal-within-vim), which requires a version of vim with python support. I also prefer terminal version of vim to the GUI version, so [MacVim](https://code.google.com/p/macvim/) is less desirable.

One way to get what I want is to compile a version of vim with [homebrew](https://mxcl.github.com/homebrew/). Homebrew does not officially have a vim fomula, because that would be a duplicate of the system version. Fortunately, we can grab an unofficial formula at *<https://raw.github.com/Homebrew/homebrew-dupes/master/vim.rb>*

Also, you may want to install the latest homebrew python with the framework option:
    
    :::bash
    brew install python --framework

In order for vim to use the homebrew version of python (2.7.3) instead of the system one (an old 2.6), we need to change a line and add a line in the downloaded formula (vim.rb) file:

    :::cfg
    ...  
    "--enable-pythoninterp=dynamic",  
    "--with-python-config-dir=/usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config",  
    ...

Now install vim with the formula:

    :::bash
    brew install ./vim.rb

To check vim is using the correct version of python. Issue command in vim:

    :::cfg
    :python import sys; print sys.version

If we get something like this:

>2.7.3 (default, May 15 2012, 20:51:34)  
>[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]  
>Press ENTER or type command to continue

we are done!
