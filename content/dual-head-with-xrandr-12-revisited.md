Title: Dual head with xrandr 1.2 revisited
Date: 2007-11-16 04:04
Author: Huahai
Category: notebook
Tags: Linux, Xorg
Slug: dual-head-with-xrandr-12-revisited
Alias: /blog/2007/11/dual-head-xrandr-1-2-revisited
Lang: en

In [this post](/blog/2007/10/use-xrandr-1-2-swtich-external-display-thinkpad-laptop), I discussed "clone" mode of dual head with xrandr 1.2. Now I got an extra monitor, and would like to use "xinerama" mode, wherein the built-in laptop LCD and the external monitor share a single virtual screen. 

To set this up, I changed my */etc/X11/xorg.conf* to add a monitor section for the external monitor:

``` 
Section "Device"   
  Identifier    "Intel 965GM"   
  Driver        "intel"   
  BusID         "PCI:0:2:0"   
  Screen        0   
  Option        "XAANoOffscreenPixmaps" "true"   
  Option        "DRI" "true"   
  Option        "monitor-LVDS" "Builtin"   
  Option        "monitor-VGA" "External" 
EndSection`
```
