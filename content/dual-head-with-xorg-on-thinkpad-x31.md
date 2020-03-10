---
Title: Dual Head with Xorg on Thinkpad X31
Date: 2005-10-15 04:00
Author: Huahai
Category: notebook
Tags: Linux, Xorg
Slug: dual-head-with-xorg-on-thinkpad-x31
Alias: /blog/2005/10/dual-head-xorg-thinkpad-x31
Lang: en
---

My Thinkpad X31 got a small 12.1 inch screen, so I decide to increase the screen real estate by adding an extra monitor. The idea is that the LCD and the CRT monitor will display different part of the same desktop. This dual head solution is sometimes called 'Xinerama' in X terminology.  

I happen to have a 17 inch CRT monitor floating around so I set out to acheive this Xinerama objective. Plug this extra monitor into my laptop, I got a cloned view of the LCD on the CRT, which is nice for presentation, but is not Xinerama. After some googling, I found out that Xorg 6.8.2, the version of X server I am using on this laptop, does not seem to work well with regular xinerama extension setup. However, its display driver for my ATI chip, Radeon, has a native xinerama-like function built in, called MergedFB. The idea is that two monitors will share a big, virtual desktop (framebuffer), and each monitor can then look at different part of the virtual desktop, exactly what I wanted.  
Setup is easy. Change /etc/X11/xorg.conf. In Device section, I have  

```
Section "Device"  
  Identifier "ATI Radeon"  
  Driver "radeon"  
  BoardName "Radeon Mobility M6 LY"  
  Option "AGPMode" "4"  
  Option "AGPFastWrite" "on"  
  Option "EnablePageFlip" "on"  
  Option "RenderAccel" "on"  
  # radeon specific Xinerama settings:  
  Option "MergedFB" "on"  
  Option "MonitorLayout" "LVDS, CRT"  
  Option "MetaModes" "1024x768-1024x768 1024x768"  
  Option "MergedDPI" "108 108"  
  #for external monitor  
  Option "CRT2HSync" "30.0-68.0"  
  Option "CRT2VRefresh" "50.0-110.0"  
  Option "CRT2Position" "RightOf"  
EndSection  
```

Basically, the MergedFB option turns on the pseudo-xinerama setting. MonitorLayout specifies the two monitors: one the laptop LCD, another external CRT. The MetaModes defines two modes: one for the big virtual screen, one for regular small screen. You can use xrandr -s 0/1 to switch them back and forth. CRT2Position says this external monitor should be rendered as if it's at the right of the LCD. Other values include: "LeftOf", "Above", "Below' and "Clone". man radeon to see details.  

Well, that's it. Restart X, plug in your external monitor, you will have a big virtual desktop across two displays. And windows on the desktop will be placed intelligently by the system so you won't get half of the window on one monitor another half on another, which is very nice. xrandr -s 0 will switch to a clone mode, where both displays the same view.  
There is still a pesty problem. The font size is bad in cloned views! xrandr -q shows that there's two display sizes, 2048x768, and 1024x768, which is fine. The problem is that both modes has the SAME physical sizes! So basically, in the 1024x768 mode, your DPI is cut in half, which renders fine in KDE, but not on other applications, such as PDF reader, OpenOffice, and Firefox, etc. This problem makes this setup unworkable when you don't have an external Monitor.  

So right now, I don't have a perfect solution for dual head on Xorg 6.8.2 :( Normally, I will not turn on MergedFB. Only when I need an extra monitor, I will edit xorg.conf to uncomment the MergeFB line, then restart X.  

Looking forward to a patch to radeon to solve this problem.
