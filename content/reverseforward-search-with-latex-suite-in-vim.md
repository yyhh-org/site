Title: Reverse/Forward Search with Latex-Suite in Vim
Date: 2007-11-22 17:19
Author: Huahai
Category: notebook
Tags: Editor, Vim, LaTeX
Slug: reverseforward-search-with-latex-suite-in-vim
Alias: /blog/2007/11/reverse-forward-search-latex-suite-vim
Lang: en

When editing a long Latex document, it is beneficial to be able to point from current location in DVI back to Tex, and vice visa. This is what called reverse/forward search between DVI and Latex. With [Latex-Suite in Vim](http://vim-latex.sourceforge.net/), this functionality is already implemented, and there's no need to specify "\\usepackage scrltx" in the Tex file. However, it's not fully configured by default. Forward search with "\\ls" works, but inverse search by "Ctrl-Left click" in xdiv is not enabled. To turn it on, edit *~/.vim/ftplugin/tex/texrc*, change the line "TexLet g:Tex\_UseEditorSettingInDVIViewer = 0" to "TexLet g:Tex\_UseEditorSettingInDVIViewer = 1".
