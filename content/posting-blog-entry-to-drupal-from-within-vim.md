Title: Posting blog entry to Drupal from within Vim
Date: 2007-10-27 21:52
Author: Huahai
Category: notebook
Tags: Vim, Python, Drupal
Slug: posting-blog-entry-to-drupal-from-within-vim
Alias: /blog/2007/10/posting-blog-entry-drupal-within-vim
Lang: en

Some people may wonder why would anyone want to do this? Well, there are at least two benefits. 

One, I can write posts *offline* with my favorite editor, whenever I feel like it. Then post them from within vim once I got an Internet connection. 

Two, I get to use niceties of vim such as spellchecker, autocompletion and syntax highlighting for html code. I found this solution on [Peter Wilkinson's Blog](http://www.petersblog.org/node/876). I did a few minor changes to make [his script](http://www.petersblog.org/node/876) to work with the latest version of python. 

A step further, I combined it with [his another post](http://www.petersblog.org/node/907), now I can even use the regular vim syntax to read/post blog entry just like a regular file, e.g. *:e blog/4* to edit blog entry number 4, *:w* to post the edited version. Very cool. See the following *.vimrc* code for details:

<font face="monospace" size="1.2em">  
<font color="#786000">" post blog entry to my Drupal site</font>  
<font color="#786000">" Use :e blog/nodeID\_which\_is\_digits to open an existing entry for editting;</font>  
<font color="#786000">"     For example :e blog/12</font>  
<font color="#786000">" Use :e blog/anything\_other\_than\_digits to open a new entry for editing</font>  
<font color="#786000">"     For example :e blog/blah</font>  
<font color="#786000">" Use :w to post it. </font>  
<font color="#786000">" Use :w blog/anything to post a file as a new blog entry</font>

<font color="#786000">python &lt;&lt; EOF</font>

strUserName = <font color="#000000">'</font><font color="#077807">your\_username</font><font color="#000000">'</font>  
strPassword = <font color="#000000">'</font><font color="#077807">your\_password</font><font color="#000000">'</font>  
strDrupal = <font color="#000000">'</font><font color="#077807"><http://your.domain.name></font><font color="#000000">'</font>

<font color="#800090">import</font> vim  
<font color="#800090">import</font> xmlrpclib  
<font color="#800090">import</font> re

<font color="#1f3f81">**def**</font> <font color="#007080">PostBlog</font>():

  <font color="#786000">\#</font>  
  <font color="#786000">\# If first line contains a blog entry ID then edit existing post,</font>  
  <font color="#786000">\# otherwise write a new one.</font>  
  <font color="#786000">\#</font>  
  nFirstLine = 0  
  strID = vim.current.buffer\[0\]  
  <font color="#1f3f81">**if**</font> <font color="#1f3f81">**not**</font> re.match( <font color="#000000">'</font><font color="#077807">^\\d+$</font><font color="#000000">'</font>, strID):  
    strID = <font color="#000000">''</font>  
  else:  
    nFirstLine = 1

  strTitle = vim.current.buffer\[nFirstLine\]  
  strText = <font color="#000000">"</font><font color="#912f11">\\n</font><font color="#000000">"</font>.join( vim.current.buffer\[nFirstLine+1:\])

  oDrupal = xmlrpclib.ServerProxy( strDrupal + <font color="#000000">'</font><font color="#077807">/xmlrpc.php</font><font color="#000000">'</font>)

  oPost = { <font color="#000000">'</font><font color="#077807">title</font><font color="#000000">'</font>: strTitle, <font color="#000000">'</font><font color="#077807">description</font><font color="#000000">'</font>: strText}

  <font color="#1f3f81">**if**</font> strID == <font color="#000000">''</font>:  
    strID = oDrupal.metaWeblog.newPost( <font color="#000000">'</font><font color="#077807">blog</font><font color="#000000">'</font>, strUserName, strPassword, oPost, True)  
  else:  
    bSuccess = oDrupal.metaWeblog.editPost( strID, strUserName, strPassword, oPost, True)

  <font color="#1f3f81">**print**</font> <font color="#000000">"</font><font color="#077807">Posted entry %s</font><font color="#000000">"</font> % strID

  <font color="#786000">\#</font>  
  <font color="#786000">\# Don't intend to write posts to disk so unmodify the buffer and</font>  
  <font color="#786000">\# allow easy quit from VIM.</font>  
  <font color="#786000">\#</font>  
  vim.command( <font color="#000000">'</font><font color="#077807">set nomodified</font><font color="#000000">'</font>)

<font color="#1f3f81">**def**</font> <font color="#007080">ReadBlog</font>( strID ):  
    
  <font color="#786000">\#</font>  
  <font color="#786000">\# So html plugin is automatically enabled for editing the post </font>  
  <font color="#786000">\# with auto-completion and syntax highlighting</font>  
  <font color="#786000">\#</font>  
  vim.command(<font color="#000000">'</font><font color="#077807">setfiletype html</font><font color="#000000">'</font>)

  <font color="#1f3f81">**if**</font> <font color="#1f3f81">**not**</font> strID.isdigit():  
    <font color="#1f3f81">**print**</font> <font color="#000000">"</font><font color="#077807">New blog entry</font><font color="#000000">"</font>  
    <font color="#1f3f81">**return**</font>

  oDrupal = xmlrpclib.ServerProxy( strDrupal + <font color="#000000">'</font><font color="#077807">/xmlrpc.php</font><font color="#000000">'</font>)

  oBlog = oDrupal.metaWeblog.getPost( strID, strUserName, strPassword )

  vim.current.buffer\[:\] = \[\]  
  vim.current.buffer\[0\] = strID  
  vim.current.buffer.append( oBlog\[<font color="#000000">'</font><font color="#077807">title</font><font color="#000000">'</font>\])  
  vim.current.buffer.append( <font color="#000000">''</font>)  
  <font color="#1f3f81">**for**</font> strLine <font color="#1f3f81">**in**</font> oBlog\[<font color="#000000">'</font><font color="#077807">description</font><font color="#000000">'</font>\].split(<font color="#000000">'</font><font color="#912f11">\\n</font><font color="#000000">'</font>):  
    vim.current.buffer.append( strLine)

<font color="#786000">EOF</font>

:au BufWriteCmd blog/\* <font color="#1f3f81">**py**</font> <font color="#000000">PostBlog</font><font color="#1f3f81">**()**</font>   
:au BufReadCmd blog/\* <font color="#1f3f81">**py**</font> <font color="#000000">ReadBlog</font><font color="#1f3f81">**(**</font>vim<font color="#1f3f81">**.**</font>eval<font color="#1f3f81">**(**</font><font color="#077807">"expand('&lt;afile&gt;:t')"</font><font color="#1f3f81">**))**</font>

<font color="#1f3f81">**syntax**</font> <font color="#912f11">**on**</font>  

</font>
