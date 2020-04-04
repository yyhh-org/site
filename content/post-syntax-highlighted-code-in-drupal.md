---
Title: Post syntax highlighted code in Drupal
Date: 2007-11-17 10:45
Author: Huahai
Category: notebook
Tags: Editor, Vim, Drupal
Slug: post-syntax-highlighted-code-in-drupal
Alias: /blog/2007/11/post-syntax-highlighted-code-drupal
Lang: en
---

You may have seen that I sometimes post code here. Wouldn't it be nice if all the code are syntax highlighted, like what we see in a text editor? Well, with the help of Vim, it's easy. Vim is bundled with a "2html" script, that can turn whatever shown in Vim into a HTML file, with all it's color and format. To invoke this command, simply issue ":so \\$VIMRUNTIME/syntax/2html.vim" command in Vim to run the script, or more simply ":TOhtml". No, you don't have to type this many characters, autocompletion should do most of the typing for you. Vim will then open up a window that contains the newly converted HTML file.

(Update: for newer version of vim, need to `:let g:html_use_css=0` first)

If I want to post it to Drupal, I simply remove the unnecessary tags such as "html", "body" and "head", etc. and save the file. When I write the blog entry, I read back the file and insert it where I want it. Also, I enclose the code with ``

code here

  
so the default Drupal style sheet renders the code within a nice box and on a light gray background.

This approach is much better than installing some syntax highlighting modules written in PHP on Drupal. Now the supported syntax highlighting file formats are practically unlimited, only bound by Vim's syntax highlighting repertoire, which includes pretty much every imaginable text file format. What's more, Vim's color theme applies here! So you can have all kinds of colorful code. Below are some examples.

This is my *~/.vimrc*, displayed with xterm16 allblue color theme, which I use in terminal:

<font face="monospace">  
<font color="#8787af">" vim behavior</font>  
<font color="#0087af">set</font> <font color="#8700d7">nocompatible</font>

<font color="#8787af">" set 256 color scheme for terminial use</font>  
<font color="#0087af">set</font> <font color="#8700d7">term</font>=xterm-256color  
<font color="#8787af">"colors desert256</font>  
<font color="#8787af">"let xterm16\_brightness = 'default'     " Change if needed</font>  
<font color="#0087af">let</font> xterm16\_colormap <font color="#0087af">=</font> <font color="#87afaf">'allblue'</font>       <font color="#8787af">" Change if needed </font>  
<font color="#8787af">"let xterm16\_colormap = 'soft'       " Change if needed </font>  
<font color="#0087af">colors</font> xterm16  
<font color="#8787af">"colors pyte</font>

<font color="#8787af">" REQUIRED. This makes vim invoke latex-suite when you open a tex file.</font>  
<font color="#0087af">filetype</font> <font color="#87af87">plugin</font> <font color="#87af87">on</font>

<font color="#8787af">"</font> <font color="#8700d7">IMPORTANT:</font><font color="#8787af"> win32 users will need to have 'shellslash' set so that latex</font>  
<font color="#8787af">" can be called correctly.</font>  
<font color="#0087af">set</font> <font color="#8700d7">shellslash</font>

<font color="#8787af">"</font> <font color="#8700d7">IMPORTANT:</font><font color="#8787af"> grep will sometimes skip displaying the file name if you</font>  
<font color="#8787af">" search in a singe file. This will confuse latex-suite. Set your grep</font>  
<font color="#8787af">" program to alway generate a file-name.</font>  
<font color="#0087af">set</font> <font color="#8700d7">grepprg</font>=grep\\ -nH\\ \\$\*

<font color="#8787af">"</font> <font color="#8700d7">OPTIONAL:</font><font color="#8787af"> This enables automatic indentation as you type.</font>  
<font color="#0087af">filetype</font> <font color="#87af87">indent</font> <font color="#87af87">on</font>

<font color="#8787af">"</font> <font color="#8700d7">TIP:</font><font color="#8787af"> if you write your \\label's as \\label{fig:something}, then if you</font>  
<font color="#8787af">" type in \\ref{fig: and press &lt;C-n&gt; you will automatically cycle through</font>  
<font color="#8787af">" all the figure labels. Very useful!</font>  
<font color="#0087af">set</font> <font color="#8700d7">iskeyword</font>+=:

<font color="#8787af">" so .tex file will always be recognized as Latex.</font>  
<font color="#0087af">let</font> g:tex\_flavor <font color="#0087af">=</font> <font color="#87afaf">"latex"</font>

<font color="#8787af">" this is mostly a matter of taste. but LaTeX looks good with just a bit</font>  
<font color="#8787af">" of indentation.</font>  
<font color="#0087af">set</font> <font color="#8700d7">tabstop</font>=2  
<font color="#0087af">set</font> <font color="#8700d7">shiftwidth</font>=2  
<font color="#0087af">set</font> <font color="#8700d7">expandtab</font> 

<font color="#0087af">set</font> <font color="#8700d7">autoindent</font>  
<font color="#0087af">set</font> <font color="#8700d7">smartindent</font>

<font color="#8787af">" matching brackets</font>  
<font color="#0087af">set</font> <font color="#8700d7">showmatch</font>

<font color="#8787af">" show cursor position</font>  
<font color="#0087af">set</font> <font color="#8700d7">ruler</font>

<font color="#8787af">" minibufexpl setting</font>  
<font color="#0087af">let</font> BufExplMapWindowNavVim <font color="#0087af">=</font> <font color="#87afaf">1</font>  
<font color="#0087af">let</font> g:miniBufExplMapWindowNavArrows <font color="#0087af">=</font> <font color="#87afaf">1</font>  
<font color="#0087af">let</font> g:miniBufExplMapCTabSwitchBufs <font color="#0087af">=</font> <font color="#87afaf">1</font>  
<font color="#0087af">let</font> g:miniBufExplModSelTarget <font color="#0087af">=</font> <font color="#87afaf">1</font>

<font color="#8787af">"set paste Mode On/Off</font>  
<font color="#0087af">map</font> <font color="#00af87">&lt;</font><font color="#00af87">F11</font><font color="#00af87">&gt;</font> :call Paste\_on\_off()<font color="#00af87">&lt;</font><font color="#00af87">CR</font><font color="#00af87">&gt;</font>  
<font color="#0087af">set</font> <font color="#8700d7">pastetoggle</font>=<font color="#00af87">&lt;</font><font color="#00af87">F11</font><font color="#00af87">&gt;</font>  
<font color="#0087af">let</font> paste\_mode <font color="#0087af">=</font> <font color="#87afaf">0</font> <font color="#8787af">" 0 = normal, 1 = paste</font>  
<font color="#0087af">func</font>! Paste\_on\_off<font color="#0087af">()</font>  
  <font color="#0087af">if</font> g:paste\_mode <font color="#0087af">==</font> <font color="#87afaf">0</font>  
    <font color="#0087af">set</font> <font color="#8700d7">paste</font>  
    <font color="#0087af">let</font> g:paste\_mode <font color="#0087af">=</font> <font color="#87afaf">1</font>  
  <font color="#0087af">else</font>  
    <font color="#0087af">set</font> <font color="#8700d7">nopaste</font>  
    <font color="#0087af">let</font> g:paste\_mode <font color="#0087af">=</font> <font color="#87afaf">0</font>  
  <font color="#0087af">endif</font>  
  <font color="#0087af">return</font>  
<font color="#0087af">endfunc</font>

<font color="#8787af">" spell checking on/off</font>  
<font color="#0087af">map</font> <font color="#00af87">&lt;</font><font color="#00af87">F10</font><font color="#00af87">&gt;</font> :call Spell\_on\_off()<font color="#00af87">&lt;</font><font color="#00af87">CR</font><font color="#00af87">&gt;</font>  
<font color="#0087af">let</font> spell\_mode <font color="#0087af">=</font> <font color="#87afaf">0</font>  
<font color="#0087af">func</font>! Spell\_on\_off<font color="#0087af">()</font>  
  <font color="#0087af">if</font> g:spell\_mode <font color="#0087af">==</font> <font color="#87afaf">0</font>  
    <font color="#0087af">setlocal</font> <font color="#8700d7">spell</font> <font color="#8700d7">spelllang</font>=en\_us  
    <font color="#0087af">let</font> g:spell\_mode <font color="#0087af">=</font> <font color="#87afaf">1</font>  
  <font color="#0087af">else</font>   
    <font color="#0087af">setlocal</font> <font color="#8700d7">nospell</font>  
    <font color="#0087af">let</font> g:spell\_mode <font color="#0087af">=</font> <font color="#87afaf">0</font>  
  <font color="#0087af">endif</font>  
  <font color="#0087af">return</font>  
<font color="#0087af">endfunc</font>

<font color="#8787af">" post blog entry to my Drupal site</font>  
<font color="#8787af">" Use :e blog/nodeID\_which\_is\_digits to open an existing entry for editting;</font>  
<font color="#8787af">"     For example :e blog/12</font>  
<font color="#8787af">" Use :e blog/anything\_other\_than\_digits to open a new entry for editing</font>  
<font color="#8787af">"     For example :e blog/blah</font>  
<font color="#8787af">" Use :w to post it. </font>  
<font color="#8787af">" Use :w blog/anything to post a file as a new blog entry</font>

<font color="#8787af">python &lt;&lt; EOF</font>

strUserName = <font color="#a8a8a8">'</font><font color="#87afaf">secret</font><font color="#a8a8a8">'</font>  
strPassword = <font color="#a8a8a8">'</font><font color="#87afaf">secret</font><font color="#a8a8a8">'</font>  
strDrupal = <font color="#a8a8a8">'</font><font color="#87afaf"><https://yyhh.org></font><font color="#a8a8a8">'</font>

<font color="#8700d7">import</font> vim  
<font color="#8700d7">import</font> xmlrpclib  
<font color="#8700d7">import</font> re

<font color="#0087af">def</font> <font color="#00afaf">PostBlog</font>():

  <font color="#8787af">\#</font>  
  <font color="#8787af">\# If first line contains a blog entry ID then edit existing post,</font>  
  <font color="#8787af">\# otherwise write a new one.</font>  
  <font color="#8787af">\#</font>  
  nFirstLine = 0  
  strID = vim.current.buffer\[0\]  
  <font color="#0087af">if</font> <font color="#0087af">not</font> re.match( <font color="#a8a8a8">'</font><font color="#87afaf">^\\d+\\$</font><font color="#a8a8a8">'</font>, strID):  
    strID = <font color="#a8a8a8">''</font>  
  else:  
    nFirstLine = 1

  strTitle = vim.current.buffer\[nFirstLine\]  
  strText = <font color="#a8a8a8">"</font><font color="#00af87">\\n</font><font color="#a8a8a8">"</font>.join( vim.current.buffer\[nFirstLine+1:\])

  oDrupal = xmlrpclib.ServerProxy( strDrupal + <font color="#a8a8a8">'</font><font color="#87afaf">/xmlrpc.php</font><font color="#a8a8a8">'</font>)

  oPost = { <font color="#a8a8a8">'</font><font color="#87afaf">title</font><font color="#a8a8a8">'</font>: strTitle, <font color="#a8a8a8">'</font><font color="#87afaf">description</font><font color="#a8a8a8">'</font>: strText}

  <font color="#0087af">if</font> strID == <font color="#a8a8a8">''</font>:  
    strID = oDrupal.metaWeblog.newPost( <font color="#a8a8a8">'</font><font color="#87afaf">blog</font><font color="#a8a8a8">'</font>, strUserName, strPassword, oPost, True)  
  else:  
    bSuccess = oDrupal.metaWeblog.editPost( strID, strUserName, strPassword, oPost, True)

  <font color="#0087af">print</font> <font color="#a8a8a8">"</font><font color="#87afaf">Posted entry %s</font><font color="#a8a8a8">"</font> % strID

  <font color="#8787af">\#</font>  
  <font color="#8787af">\# Don't intend to write posts to disk so unmodify the buffer and</font>  
  <font color="#8787af">\# allow easy quit from VIM.</font>  
  <font color="#8787af">\#</font>  
  vim.command( <font color="#a8a8a8">'</font><font color="#87afaf">set nomodified</font><font color="#a8a8a8">'</font>)

<font color="#0087af">def</font> <font color="#00afaf">ReadBlog</font>( strID ):  
    
  <font color="#8787af">\#</font>  
  <font color="#8787af">\# So html plugin is automatically enabled for editing the post </font>  
  <font color="#8787af">\# with auto-completion and syntax highlighting</font>  
  <font color="#8787af">\#</font>  
  vim.command(<font color="#a8a8a8">'</font><font color="#87afaf">setfiletype html</font><font color="#a8a8a8">'</font>)

  <font color="#0087af">if</font> <font color="#0087af">not</font> strID.isdigit():  
    <font color="#0087af">print</font> <font color="#a8a8a8">"</font><font color="#87afaf">New blog entry</font><font color="#a8a8a8">"</font>  
    <font color="#0087af">return</font>

  oDrupal = xmlrpclib.ServerProxy( strDrupal + <font color="#a8a8a8">'</font><font color="#87afaf">/xmlrpc.php</font><font color="#a8a8a8">'</font>)

  oBlog = oDrupal.metaWeblog.getPost( strID, strUserName, strPassword )

  vim.current.buffer\[:\] = \[\]  
  vim.current.buffer\[0\] = strID  
  vim.current.buffer.append( oBlog\[<font color="#a8a8a8">'</font><font color="#87afaf">title</font><font color="#a8a8a8">'</font>\])  
  vim.current.buffer.append( <font color="#a8a8a8">''</font>)  
  <font color="#0087af">for</font> strLine <font color="#0087af">in</font> oBlog\[<font color="#a8a8a8">'</font><font color="#87afaf">description</font><font color="#a8a8a8">'</font>\].split(<font color="#a8a8a8">'</font><font color="#00af87">\\n</font><font color="#a8a8a8">'</font>):  
    vim.current.buffer.append( strLine)

<font color="#8787af">EOF</font>

:au BufWriteCmd blog/\* <font color="#0087af">py</font> <font color="#a8a8a8">PostBlog</font><font color="#0087af">()</font>   
:au BufReadCmd blog/\* <font color="#0087af">py</font> <font color="#a8a8a8">ReadBlog</font><font color="#0087af">(</font>vim<font color="#0087af">.</font>eval<font color="#0087af">(</font><font color="#87afaf">"expand('&lt;afile&gt;:t')"</font><font color="#0087af">))</font>

<font color="#0087af">syntax</font> <font color="#87af87">on</font>  

</font>

On Drupal's side, I needed to enable full HTML input format, or these colorful HTML code will be removed by Drupal. Oh, another thing, do not use TinyMCE rich text editor to edit the post, because it will mess up the HTML code. Well, TinyMCE was installed here per Yunyao's request, I don't use it anyway, I [use vim to edit my post](https://yyhh.org/blog/2007/10/posting-blog-entry-drupal-within-vim):-)
