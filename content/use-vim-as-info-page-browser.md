---
Title: Use Vim as Info Page Browser
Date: 2007-11-29 07:56
Author: Huahai
Category: notebook
Tags: Vim, Linux
Slug: use-vim-as-info-page-browser
Alias: /blog/2007/11/use-vim-info-page-browser
Lang: en
---

In [this post](https://yyhh.org/blog/2007/11/use-vim-read-manual-page), I set up vim as a manual page viewer, using [ManPageView](https://vim.sourceforge.net/scripts/script.php?script_id=489) plugin. It turned out that the same plugin can be used to view info pages as well. All one needs to to is to add ".i" suffix to the command that you are seeking help on. For example, ":Man sed.i" will show the info page for sed. With this information, we can set up vim as info page browser, just add these lines in *~/.bashrc*:

` vinfo() { /usr/bin/vim -c "Man $@.i" -c 'silent! only' -c 'nmap q :q' } alias info='vinfo'`

Now open a terminal, type *info whatever* will show the info page of whatever you are seeking help on, if it exists, with nice syntax highlighting and easy to use key bindings. One caveat is that you would get an blank page if the info page does not exist, instead of getting the top level info directory as with the real info command. However, real info command doesn't have syntax highlighting and familiar key-bindings, so I stick with vim.
