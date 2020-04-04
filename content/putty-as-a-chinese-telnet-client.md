---
Title: Putty as a Chinese Telnet client
Date: 2005-11-02 00:42
Author: Huahai
Category: notebook
Tags: Software
Slug: putty-as-a-chinese-telnet-client
Alias: /blog/2005/11/putty-chinese-telnet-client
Lang: en
---

How to display Chinese characters correctly on a Telnet client running on a non-Chinese version of Windows machine? Web browsers today support whatever character encodings, this is not so with Telnet client. If you make a Telnet connection to a Chinese server with Windows telnet client, you will most likely see strange characters on screen.

Solution: [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/).

Download the PuTTY programs. Better to download the Windows installer, install as usual.  

Launch PuTTY, you will see a configuration screen. Choose Wndows-&gt;Appearance, change Font settings, to use a Chinese font, such as NSimsun. On the Font dialog, change Script from Western to Chinese\_GB2312.  

on the configuration screen, choose Windows-&gt;Translation, click on the Charater set translation on received data pull-down menu to select the last one: Use font encoding.  

Connect to your favirate Chinese BBS server.  

If your Windows do not have Chinese fonts already installed, you can install from your Windows installation disk, or download it from somewhere.
