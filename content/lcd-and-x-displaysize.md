---
Title: LCD and X DisplaySize
Date: 2005-10-15 04:00
Author: Huahai
Category: notebook
Tags: Linux, Xorg
Slug: lcd-and-x-displaysize
Alias: /blog/2005/10/lcd-and-x-displaysize
Lang: en
---

Under Linux, have you ever felt that stuff on your brand new LCD display looked blurry, especially with small font sizes, the words start to look fuzzy after a while? Chances are that you did not set the LCD with its optimal resolution. There is an easy fix:  

1. Measure the actually size of your LCD display area in millimeters (mm). Use a ruler. For example, my small X31 screen measures 240mm (width) by 180mm (height ).  

2. Now check the values you have in your X configuration  

    `xdpyinfo | grep dimensionsi`

and compare the mm with the your actual measurement. If the numbers are far off, you do have a misconfiged display size.  

3. Edit /etc/X11/xorg.conf as root, in the "Monitor" section, add a line  

    `DisplaySize 240 180`

Use your measured values of course.  

Press Ctrl-Alt-Backspace to restart X server.  

Once the X is back, you should see crisp clear display.  

The fonts may now look too big or too small, you can change them in window manager settings, be it KDE or GNOME or something else.
