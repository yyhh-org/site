---
Status: published
Title: Use XRandR 1.2 to Swtich on External Display for Thinkpad Laptop
Date: 2007-10-28 15:00
Author: Huahai
Category: notebook
Tags: Linux, Xorg
Slug: use-xrandr-12-to-swtich-on-external-display-for-thinkpad-laptop
Alias: /blog/2007/10/use-xrandr-1-2-swtich-external-display-thinkpad-laptop
Lang: en
---

Thinkpad X61 has an VGA output port, so it supports dual-head display. However, with the Intel GMA965 graphics chipset in X61, the thinkpad\_acpi (used to be called ibm\_acpi) kernel module does not seem to support switching on or off this VGA port any more. The traditionally used commands, such as "echo crt\_enable &gt; /proc/acpi/ibm/video", no longer work.  
Fortunately, the xserver-xorg-video-intel display driver supports xrandr 1.2. extension in recent versions of Xorg X server. So we can use xrandr to dynamically switch on or off the external VGA display, and much more.

It's often necessary to connect a projector through the VGA port and display the same content as the LCD, for example, for presentation purpose. This so called clone mode of dual-head is supported out-of-box with xrandr, no X configuration and no restarting X is necessary. xrandr can detect the presence of the external video connection, even when the external device is not powered on! Let's try it out. First, without connecting anyting to the VGA port, issue xrandr query command:

`xrandr -q`

You will get something like this:

Screen 0: minimum 320 x 200, current 1024 x 768, maximum 1024 x 1024  
VGA disconnected (normal left inverted right x axis y axis)

LVDS connected 1024x768+0+0 (normal left inverted right x axis y axis) 246mm x 184mm  
1024x768 50.0\*+ 60.0 40.0

800x600 60.3

640x480 60.0 59.9

Now, connect your an external monitor to the VGA port without powering it on, issue the same xranr query command. The output will be something similar to:

Screen 0: minimum 320 x 200, current 1024 x 768, maximum 1024 x 1024

VGA connected (normal left inverted right x axis y axis)

1024x768 60.0

800x600 60.3

640x480 59.9

LVDS connected 1024x768+0+0 (normal left inverted right x axis y axis) 246mm x 184mm

1024x768 50.0\*+ 60.0 40.0

800x600 60.3

640x480 60.0 59.9

This shows the presence of the external VGA device. And the device is given some generic display modes.  
Now power on the monitor, you will get something similar to:

Screen 0: minimum 320 x 200, current 1024 x 768, maximum 1024 x 1024

VGA connected (normal left inverted right x axis y axis)

1024x768 75.0 + 84.9 85.0 75.1 75.0 70.1 60.0

832x624 74.6

800x600 84.9 85.1 72.2 75.0 60.3 56.2

640x480 85.0 84.6 75.0 72.8 75.0 60.0 59.9

720x400 85.0 70.1

640x400 85.1

640x350 85.1

LVDS connected 1024x768+0+0 (normal left inverted right x axis y axis) 246mm x 184mm

1024x768 50.0\*+ 60.0 40.0

800x600 60.3

640x480 60.0 59.9

Now the monitor's supported modes are detected, and those allowable modes for the 1024x1024 virtual screen are shown.  
At this moment, the external VGA device is connected and powered on, but has not been given any video signal (so from a software point of view, it's off). In order to use the VGA device, we need to use xrandr command to "turn it on". This command will do:

`xrandr --output VGA  --auto`

You should see the cloned view of your LCD on the monitor. Now issue xrandr query command, you will see:  
Screen 0: minimum 320 x 200, current 1024 x 768, maximum 1024 x 1024  
VGA connected 1024x768+0+0 (normal left inverted right x axis y axis) 312mm x 234mm  
1024x768 75.0\*+ 84.9 85.0 75.1 75.0\* 70.1 60.0  
832x624 74.6  
800x600 84.9 85.1 72.2 75.0 60.3 56.2  
640x480 85.0 84.6 75.0 72.8 75.0 60.0 59.9  
720x400 85.0 70.1  
640x400 85.1  
640x350 85.1  
LVDS connected 1024x768+0+0 (normal left inverted right x axis y axis) 246mm x 184mm  
1024x768 50.0\*+ 60.0 40.0  
800x600 60.3  
640x480 60.0 59.9  
The difference is that VGA now have a string '1024x768+0+0', where 1024x768 obviously is the size, and the 0 0 is the start x y position of the VGA viewpoint within the virtual screen.  
Of course, you can "turn it off" by

`xrandr --output VGA --off`

Similarly, you can turn off/on your laptop built-in LCD display with

`xrandr --output LVDS --off`

or

`xrandr --output LVDS --auto`

It's so easy, and it works beautifully. For convenience, you can hook these commands to your favorite ACPI events handling program, such as powersave (if you use this, check out my other blog entry on hotkey setup), pm-utils, etc. Then, by pressing Fn+F7, you can toggle external display on or off, just like you would do in Windows.

Instead of "clone" mode, many people want to set up "real dual-head", i.e. creating a big virtual screen shared by the built-in LCD and the external monitor. The LCD view could be to the leftof, rightof, above, or below the external display view. It's easy to setup, just add a line "Virtual bigX bigY" in the Display subsection of the Monitor section in your /etc/X11/xorg.conf, where bigX and bigY are the desired sizes of the virtual display, e.g. 2048 2048. Restart X, then use xrandr command to turn on/off external display and move the viewpoints anywhere within this virtual screen. You can probably man xrandr to find out more.  
I personally do not use "real dual-head", because I have the inverse problem: I have more computers than monitors. What I need is software KVM switch, for which Yunyao have found a solution: [synergy.](https://synergy2.sourceforge.net/) Thanks, my dear :) **Update**: I actually did "real dual-head", please see [this post](/blog/2007/11/dual-head-xrandr-1-2-revisited) for details.
