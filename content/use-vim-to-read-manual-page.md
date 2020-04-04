---
Title: Use Vim to read manual page
Date: 2007-11-09 22:10
Author: Huahai
Category: notebook
Tags: Editor, Vim, Linux
Slug: use-vim-to-read-manual-page
Alias: /blog/2007/11/use-vim-read-manual-page
Lang: en
---

Command line manual page is an indispensable tool for working with Linux system.If you forget how to use a command, just type *man* followed by the name of the command. One thing I don't like about the manual system on my Debian sid is that it uses *most* to display the manual. The key bindings of *most* feel awkward for me since I am used to *vim*. Of course, there are many "vimers" like me, and they've found ways to fix this. Actually, there are [many different ways](https://vim.sourceforge.net/tips/tip.php?tip_id=167), but I find the approach below works best for me. Basically, it involves creating a shell alias for *man*, so when *man* is used, shell invokes *vim* instead to read the manual. The following is added in *~/.bashrc*:

``` 
# use vim as man's pager, rely on ManPageView plugin 
vman() {   
  /usr/bin/whatis "$@" > /dev/null   
  if [ $? -eq 0 ]; then     
    /usr/bin/vim -c "Man $@" -c 'silent! only' -c 'nmap q :q'   
  else     
    /usr/bin/man "$@"   
  fi 
} 
alias man='vman'`
```

This script relies on [ManPageView](https://vim.sourceforge.net/scripts/script.php?script_id=489) plugin. However, I found the bundled syntax highlighting for this plug-in does not work as I expected, so I just deleted *~/.vim/syntax/man.vim*. It works because *vim* 7.0 has manual page syntax highlighting already built-in.
