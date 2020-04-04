---
Title: Reference to Individual Email Message in Plain Text File
Date: 2007-12-13 22:40
Author: Huahai
Category: notebook
Tags: Editor, Vim, Linux, GTD
Slug: reference-to-individual-email-message-in-plain-text-file
Alias: /blog/2007/12/reference-individual-email-message-plain-text-file
Lang: en
---

A lot of people implement [GTD methodology entirely with Gmail](https://saw.themurdaughs.com/gtd-with-gmail-whitepaper). I don't feel comfortable doing that because gmail is not that secure. And I think depending on a network service is a bad idea for a GTD system. So I still download all my emails to my local computers. As [my plain text based GTD implementation](https://yyhh.org/blog/2007/12/simple-gtd-list-solution-desktop-web-and-possibly-mobile) was taking shape, I realized that I needed to refer to individual email messages in my local mail folders, both in the "Projects/Next-Action" list and as reference materials. For example, in my list, there would be an item "think about Johon's request", and it should include a link to the email message containing John's request. Ideally, invoking this link should open up this email message in *kmail*, my email reader. Also, I would like the creation of such a link in my list to be semi-automatic.

The first problem is to find the unique id for the email message. Although there's an Message-ID field in standard email format, kmail does not make it easy to use that field. It turns out that just using the unique filename of email messages is sufficient. Kmail by default uses *maildir* format to store emails, and maildir stores each message as an individual file with a unique name. This situation makes linking to email messages as easy as linking to files. Now the question is, how do I know what filename an individual email message is saved as?

The answer is I don't know, kmail does not reveal that information. At least I don't know the filename when the email is first saved in my email folder. But, the good news is, I don't need to know the filename when the email is in my inbox. Because, as GTD methodology decrees, stuff in inbox should not be permanent, but is to be moved into either projects/next-action list or reference collection. Now, when I process my inbox, and move a message into my GTD email folder, I can figure out what name it is saved in. No, I am not suggesting using kmail's "save-as" method. That's still too much work, because I then have to open a file browser, choose a filename for the email to save as, and manually put a link to that file in my list. Besides, kmail can only "save-as" mbox format, and it sucks.

What I now end up with is a neat solution. Basically, all I need to do, is to drag a message into my local GTD mail folder in kmail. And a link to the saved message will be automatically inserted into my plain-text project/next-action list or my reference file, depending on a dialog selection. This screen shot shows an email being dragged into GTD folder in kmail: ![kmail](https://i274.photobucket.com/albums/jj251/huahaiy/kmail-drag-gtd.png)

A dialog then shows up:![dialog](https://i274.photobucket.com/albums/jj251/huahaiy/kmail-drag-gtd-dialog.png).

After making a selection, a reference to the email message is inserted in vim, which looks like this:  

&lt;mail:~/Mail/GTD/cur/1197479411.14855.WSF8K:2,S&gt;

This implementation depends on [inotify-tools](https://inotify-tools.sourceforge.net/), which utilizes newer Linux kernel's *inotify* capability. It watches GTD mail folder. When an email message is moved into this folder, a script records its filename, and inserts a link to the email in my project/next-action list. This solution also depends on *vim* with server mode support, so other program can send commands to it. I always start my projects/next-action editing session in server mode, with special server names, such as "active\_projects":  

gvim --servername "active\_projects" projects.taskpaper

Finally, a vim plug-in [utl.vim](https://www.vim.org/scripts/script.php?script_id=293) is needed to invoke any URL in plain text.

All these components are glued together with a simple shell script *~/bin/email2gtd.sh*:  

<font face="monospace">  
<font color="#a0b0c0">*\#!/bin/bash*</font>  
<font color="#a0b0c0">*\# waiting for email message being dropped in GTD mail folder, then insert*</font>  
<font color="#a0b0c0">*\# a reference to the email in one of the available vim server buffers,*</font>  
<font color="#a0b0c0">*\# depending on user selection in dialog prompt*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\# author: Huahai Yang, 12/13/2007 11:22:36 AM (PST)  *</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#007020">**while**</font> <font color="#5b3674">*email*</font>=<font color="#1060a0">$(</font><font color="#70a0d0">*inotifywait -e moved\_to ~/Mail/GTD/cur --format* </font><font color="#408010">"</font><font color="#4070a0">%f</font><font color="#408010">"</font><font color="#1060a0">)</font><font color="#408010">;</font> <font color="#4c8f2f">**do**</font>

  <font color="#a0b0c0">*\# the list of available vim servers*</font>  
  <font color="#5b3674">*servers*</font>=<font color="#408010">(</font> <font color="#1060a0">$(</font><font color="#70a0d0">*vim --serverlist*</font><font color="#1060a0">)</font> <font color="#408010">)</font>

  <font color="#a0b0c0">*\# the number of available vim servers*</font>  
  <font color="#5b3674">*num*</font>=<font color="#1060a0">${\#</font><font color="#1060a0">servers</font><font color="#1060a0">\[</font>@<font color="#1060a0">\]</font><font color="#1060a0">}</font>

  <font color="#4c8f2f">**if**</font> <font color="#70a0d0">*\[\[*</font> <font color="#1060a0"> $num</font> <font color="#4c8f2f">**-eq**</font> <font color="#40a070">0</font> <font color="#70a0d0">*\]\]*</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
    kdialog --msgbox <font color="#408010">"</font><font color="#4070a0">There is no vim server running.</font><font color="#408010">"</font>  
  <font color="#4c8f2f">**else**</font>  
    <font color="#a0b0c0">*\# construct dialog choices*</font>  
    <font color="#5b3674">*choices*</font>=<font color="#408010">""</font>  
    <font color="#007020">**for**</font> id <font color="#007020">**in**</font> <font color="#1060a0"> $(</font><font color="#70a0d0">*seq* </font><font color="#40a070">0</font><font color="#70a0d0">* *</font><font color="#1060a0"> $((</font><font color="#1060a0"> $num</font><font color="#70a0d0">* -* </font><font color="#40a070">1</font><font color="#1060a0">))</font><font color="#1060a0">)</font><font color="#408010">;</font> <font color="#4c8f2f">**do**</font>  
      <font color="#5b3674">*choices*</font>=<font color="#1060a0"> ${</font><font color="#1060a0">choices</font><font color="#1060a0">}</font><font color="#408010">"</font><font color="#4070a0"> </font><font color="#408010">"</font><font color="#1060a0"> ${</font><font color="#1060a0">servers</font><font color="#1060a0">\[</font><font color="#1060a0"> $id</font><font color="#1060a0">\]</font><font color="#1060a0">}</font><font color="#408010">"</font><font color="#4070a0"> </font><font color="#408010">"</font><font color="#1060a0"> ${</font><font color="#1060a0">servers</font><font color="#1060a0">\[</font><font color="#1060a0"> $id</font><font color="#1060a0">\]</font><font color="#1060a0">}</font><font color="#408010">"</font><font color="#4070a0"> off</font><font color="#408010">"</font>  
    <font color="#4c8f2f">**done**</font>

    <font color="#5b3674">*server*</font>=<font color="#1060a0"> $(</font><font color="#70a0d0">*kdialog --title* </font><font color="#408010">"</font><font color="#4070a0">Insert email reference</font><font color="#408010">"</font><font color="#70a0d0">* \\*</font>  
<font color="#70a0d0">*        --radiolist* </font><font color="#408010">"</font><font color="#4070a0">Please select which vim server to insert into:</font><font color="#408010">"</font><font color="#70a0d0">* \\*</font>  
<font color="#70a0d0">*        *</font><font color="#1060a0"> $choices</font><font color="#1060a0">)</font>

    <font color="#a0b0c0">*\# insert the email reference to the end of the current line*</font>  
    vim --servername <font color="#408010">"</font><font color="#1060a0"> $server</font><font color="#408010">"</font> \\  
        --remote-send <font color="#408010">"</font><font color="#4070a0">&lt;ESC&gt;A&lt;mail:~/Mail/GTD/cur/</font><font color="#408010">"</font><font color="#1060a0"> ${</font><font color="#1060a0">email</font><font color="#1060a0">}</font><font color="#408010">"</font><font color="#4070a0">&gt;&lt;ESC&gt;</font><font color="#408010">"</font>  
  <font color="#4c8f2f">**fi**</font>  
<font color="#4c8f2f">**done**</font>  

</font>

This script should run in the background. I personally run it from *~/.kde/Autostart* so it is automatically loaded when I log in. It watches the *~/Mail/GTD* folder I created in kmail, and insert a reference to an email to available vim server when the email is moved to the folder.

Finally, I set up utl.vim plug-in so that it knows how to invoke a reference to email message. After installing utl.vim, I added the following function in my *.vimrc*, so that utl.vim can handle my "mail:" style URL:

<font face="monospace">  
<font color="#a0b0c0">*" lauch kmail to handle reference to email message*</font>  
<font color="#007020">**fu**</font>! Utl\_AddressScheme\_mail<font color="#408010">(</font>auri<font color="#408010">)</font>  
  <font color="#007020">**exe**</font> <font color="#4070a0">"!kmail --view "</font> <font color="#408010">.</font> UtlUri\_unescape<font color="#408010">(</font> UtlUri\_opaque<font color="#408010">(</font>a:auri<font color="#408010">)</font> <font color="#408010">)</font>  
  <font color="#007020">**return**</font> <font color="#4070a0">''</font>  
<font color="#007020">**endfu**</font>  
</font>


Now when cursor is on an email link, hit *\\gu* will open up the message in kmail.

[<img src="https://i274.photobucket.com/albums/jj251/huahaiy/gtd-email-reference.png" width="720" />](https://i274.photobucket.com/albums/jj251/huahaiy/gtd-email-reference.png)
