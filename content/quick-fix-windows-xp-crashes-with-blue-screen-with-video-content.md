---
Title: "Quick Fix: Windows XP Crashes with Blue Screen with Video Content"
Date: 2011-09-22 00:06
Author: Yunyao
Category: notebook
Tags: Software, Windows
Slug: quick-fix-windows-xp-crashes-with-blue-screen-with-video-content
Alias: /blog/2011/09/quick-fix-windows-xp-crashes-blue-screen-video-content
Lang: en
---

For some reason, my main working machine, a Windows XP desktop, recently  started to crash a lot followed by the blue screen of death. The error message output at the blue screen does not seem to be helpful.  

**\*\*\*STOP: 0x0000008E (0xE0000001, 0xBA490925, 0xA880D820, 0x00000000)**  
**\*\*\*watchdog.sys - Address BA490925, base at BA90000, Date stamp 480254ab**

After a few crashes, I realized that the machine crashes whenever I play any video in the web browser ( I am using FireFox). Initially, I didn't bother to look into this problem and simply attempt to solve the problem by avoid playing any video, since I don't really intent to watch any video during my work hours and would rather spend my time doing really work instead of fixing the machine. However, this didn't really help since so many sites now a days include video content .

So today, when the machine crashed again, I decided to fix this issue once and for all. Luckily, one Google search using the error message turned up quite a few answers. Most of the answers tent to be too complicated than what I wanted and involving checking for malware, virus, etc, which is not really my concern. Luckily, I found a very simply solution [here](https://forums.adobe.com/thread/798985).

Due to changes to the link, the exact solution from the above link no longer work. But **the basic idea is to go to any site with flash content, and then right click on the flash content, select "setting" from the pop-up menu and uncheck** **"Enable hardware acceleration".**

**<img src="https://www.macromedia.com/support/documentation/en/flashplayer/help/images/display_en.gif" width="213" height="136" />**

For example, you can go to <https://www.adobe.com/products/flashplatformruntimes/gallery/> or any Youtube page. Just make sure that you don't play the video before you make the change. Otherwise, you will see the blue screen again.
