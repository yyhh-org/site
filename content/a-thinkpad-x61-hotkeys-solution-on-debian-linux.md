---
Title: A Thinkpad X61 Hotkeys Solution on Debian Linux
Date: 2007-10-28 23:41
Author: Huahai
Category: notebook
Tags: Linux
Slug: a-thinkpad-x61-hotkeys-solution-on-debian-linux
Alias: /blog/2007/10/thinkpad-x61-hotkeys-solution-debian-linux
Lang: en
---

On my old Thinkpad X31, there is a nice little program called [tpb](http://www.nongnu.org/tpb/) that makes all Thinkpad hotkeys work on Linux. However, that project hasn't been updated for two years, and tpb does not work with the newer Thinkpad models. On my new X61, notably, the sound volume controls are broken: volume UP and volume Down keys produce the same effect - bring the volume to the half level. It seems that piece of hardware called nvram, on which tpb relies, now produces different values than older models. So, I have to ditch tpb. After some trial and errors, I worked out a mixed solution that made all keys work as expected.

**What's needed**

\* [Newer kernel](http://www.kernel.org/). At least 2.6.16 or above (not sure exact version number).

\* [acpid](http://acpid.sourceforge.net/). Newer laptops all support ACPI, so acpid should be used. I believe all linux distribution has it.

\* [thinkpad\_acpi](http://ibm-acpi.sourceforge.net/). This kernel module deals with Thinkpad hardware and generate ACPI events, such as temperature change, function key press, docking, etc. This module is included in the mainline kernel since 2.6.10. The version included in kernel 2.6.22 is thinkpad\_acpi 0.14. The latest version is 0.18. I find 0.14 works fine. Maybe 0.18 is better, I don't know. If this module is loaded, *cat /proc/acpi/ibm/driver* should show its version number. If not, load the module with *modprobe thinkpad\_acpi*. If you want it autoloaded on boot, put a line *thinkpad\_acpi* in */etc/modules*. If your kernel doesn't has this module (unlikely), you will have to download the source and build the module yourself.

\* [powersaved](http://sourceforge.net/projects/powersave/) This daemon is what actually handles ACPI events. In the past, people put ACPI events handling scripts in */etc/acpi* directory. Now this is not recommended. So you should not install similar packages such as *acpi-support*, *hibernate* scripts, etc. Instead, user space program such as *powersaved* should handle ACPI events. Therefore, all your ACPI customizations should be done under either */usr/lib/powersave/scripts* or */etc/powersave*

\* [uswsusp](http://suspend.sourceforge.net/) This user space software suspend package is called by powersaved to actually do sleeping (i.e. saving state in RAM, so sleep and resume are quick) and hibernation (i.e. save state on disk, so it lasts).

All these are already packaged in Debian. Just use apt-get to install them.

**What's worked: without configuration**

Without any software, sound Mute key and Thinklight key always work, they are hardware controlled I think.

With the above package installed, "Fn+F12 hibernate" worked without any problem. "Fn+F4 sleep" may or may not work. Please follow the suggestions in this [s2ram](http://en.opensuse.org/S2ram) documentation, and test the command options in order, until sleep works. My X61 worked with *s2ram -f -a 1*, so I stopped testing other options. Once found a successful combination, edit */usr/lib/powersave/sleep*, so that these two options reads

`SUSPEND2RAM_FORCE="yes" SUSPEND2RAM_ACPI_SLEEP="1" #use your successful -a number here, mine is 1`

"Fn+F5 toggle bluetooth" seems to work, as I can turn the bluetooth LED on and off with it and get corresponding KPowersave notification (I am on KDE).

I do not have a dock, so I can't test "Fn+F9 docking".

"Fn+F2 lock screen", "Fn+F7 toggle display", "Fn+Home brightness up", "Fn+End brightness down", "Fn+space zoom" , and "ThinkVantage", did not work out of box. But ACPI sees them, so I configured powersaved to make them work. See below.

"Volume Up/Down", "Fn+up stop", "Fn+down play", "Fn+left rewind", "Fn+right forward", "Page Left/Right", "Windows", and "Menu" did not work out of box, but X sees them, so I configured Xmodmap and KDE shortcuts to make them work. See below.

There's a battery icon on "Fn+F3", pressing it turned screen blank, but the backlight was still on, so it's useless. I used powersaved to make it a switch to go into power save mode - low LCD brightness and low power level. See below.

From the icon on it, "Fn+F8" seems to be a touchpad/touchpoint switch, and pressing it had no effect, since X61 doesn't have a touchpad. I made it a switch to presentation mode - no screensaver, no auto sleep, etc. See below.

**Configure ACPI hotkeys with powersaved**

Most Thinkpad function keys generate ACPI events. I use powersaved to hand ACP events. First I tell powersavd to use my own ACPI events handler by editing */etc/powersave/events* file, and change the line *EVENT\_OTHER="ignore"* to *EVENT\_OTHER="thinkpad\_acpi\_events"*.

Now I create a file */usr/lib/powersaved/scripts/thinkpad\_acpi\_events*, which looks like this:

<font face="monospace" size="1em">  
<font color="#a0b0c0">*\#!/bin/bash*</font>  
<font color="#a0b0c0">*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*</font>  
<font color="#a0b0c0">*\#                                                                         \#*</font>  
<font color="#a0b0c0">*\#                         Powersave Daemon                                \#*</font>  
<font color="#a0b0c0">*\#                                                                         \#*</font>  
<font color="#a0b0c0">*\#          Copyright (C) 2005,2006 SUSE Linux Products GmbH               \#*</font>  
<font color="#a0b0c0">*\#                                                                         \#*</font>  
<font color="#a0b0c0">*\# Author(s): Based on code by Stefan Seyfried                             \#*</font>  
<font color="#a0b0c0">*\#            Hotkey support by Alex Solovey, <solovey@us.ibm.com>           \#*</font>  
<font color="#a0b0c0">*\#            Enhancements (docking station support) by Holger Macht       \#*</font>  
<font color="#a0b0c0">*\#                                                                         \#*</font>  
<font color="#a0b0c0">*\# This program is free software; you can redistribute it and/or modify it \#*</font>  
<font color="#a0b0c0">*\# under the terms of the GNU General Public License as published by the   \#*</font>  
<font color="#a0b0c0">*\# Free Software Foundation; either version 2 of the License, or (at you   \#*</font>  
<font color="#a0b0c0">*\# option) any later version.                                              \#*</font>  
<font color="#a0b0c0">*\#                                                                         \#*</font>  
<font color="#a0b0c0">*\# This program is distributed in the hope that it will be useful, but     \#*</font>  
<font color="#a0b0c0">*\# WITHOUT ANY WARRANTY; without even the implied warranty of              \#*</font>  
<font color="#a0b0c0">*\# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU       \#*</font>  
<font color="#a0b0c0">*\# General Public License for more details.                                \#*</font>  
<font color="#a0b0c0">*\#                                                                         \#*</font>  
<font color="#a0b0c0">*\# You should have received a copy of the GNU General Public License along \#*</font>  
<font color="#a0b0c0">*\# with this program; if not, write to the Free Software Foundation, Inc., \#*</font>  
<font color="#a0b0c0">*\# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA                  \#*</font>  
<font color="#a0b0c0">*\#                                                                         \#*</font>  
<font color="#a0b0c0">*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\# thinkpad\_acpi\_events - process ThinkPad specific ACPI events generated by*</font>  
<font color="#a0b0c0">*\# ibm\_acpi driver and log them to syslog*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\# Configuration changes required for the script to work with powersave package:*</font>  
<font color="#a0b0c0">*\# 1) Set EVENT\_OTHER="thinkpad\_acpi\_events" in /etc/sysconfig/powersave/events*</font>  
<font color="#a0b0c0">*\# 2) Place this script into /usr/lib/powersave/scripts directory*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\# Customized by Huahai Yang to support Thinkpad X61 ACPI keys on KDE.*</font>  
<font color="#a0b0c0">*\# Added on screen visual feedback for key press, the following keys are* </font>  
<font color="#a0b0c0">*\# supported on top of existing powersaved supported keys:*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\# - Fn+F1 to start wireless connection*</font>  
<font color="#a0b0c0">*\# - Fn+F2 to lock desktop*</font>  
<font color="#a0b0c0">*\# - Fn+F3, F6, F9 to switch among Powersave, Performance and Presentation*</font>  
<font color="#a0b0c0">*\#   mode*</font>  
<font color="#a0b0c0">*\# - Fn+F7 to turn on/off external display*</font>  
<font color="#a0b0c0">*\# - Fn+F8 to toggle clone/xinerama dual head display mode*</font>  
<font color="#a0b0c0">*\# - Fn+F11 to start LAN connection* </font>  
<font color="#a0b0c0">*\# - Fn+Home, Fn+End to increase, decrease LCD brightness*</font>  
<font color="#a0b0c0">*\# - Fn+Space to take screenshot*</font>  
<font color="#a0b0c0">*\# - ThinkVantage to open konsole*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*</font>  
<font color="#5b3674">*PATH*</font>=/bin:/usr/bin:/usr/X11R6/bin:/sbin:/usr/sbin  <font color="#a0b0c0">*\# be paranoid, we're running as root.*</font>

<font color="#a0b0c0">*\# First, we pull in the helper functions.*</font>  
<font color="#408010">. </font><font color="#1060a0"> ${</font><font color="#1060a0">0</font><font color="#408010">%</font>/\*<font color="#1060a0">}</font>/helper\_functions <font color="#a0b0c0">*\# \`dirname $0\`/helper\_functions*</font>  
<font color="#a0b0c0">*\# get\_x\_user comes from here...*</font>  
<font color="#408010">. </font><font color="#1060a0"> ${</font><font color="#1060a0">0</font><font color="#408010">%</font>/\*<font color="#1060a0">}</font>/x\_helper\_functions <font color="#a0b0c0">*\# \`dirname $0\`/x\_helper\_functions*</font>  
<font color="#007020">**export**</font> PATH

<font color="#5b3674">*ME*</font>=<font color="#1060a0"> ${</font><font color="#1060a0">0</font><font color="#408010">\#\#</font>\*/<font color="#1060a0">}</font> <font color="#a0b0c0">*\# basename  $0*</font>

<font color="#a0b0c0">*\# argument $4 is set to $EV\_ID in helper\_functions which is included above*</font>  
<font color="#4c8f2f">**if**</font> <font color="#408010">\[</font> <font color="#4c8f2f">**-z**</font> <font color="#408010">"</font><font color="#1060a0"> $EV\_ID</font><font color="#408010">"</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
    DEBUG <font color="#408010">"</font><font color="#1060a0"> $ME</font><font color="#4070a0"> 'Sorry, not enough arguments: </font><font color="#1060a0"> $4</font><font color="#4070a0"> is empty.'</font><font color="#408010">"</font> WARN  
    <font color="#1060a0"> $SCRIPT\_RETURN</font> <font color="#1060a0"> $EV\_ID</font> <font color="#40a070">1</font> <font color="#408010">"</font><font color="#1060a0"> $ME</font><font color="#4070a0"> finished unsuccessful.</font><font color="#408010">"</font>  
    <font color="#007020">**exit**</font> <font color="#40a070">1</font>  
<font color="#4c8f2f">**fi**</font>

<font color="#a0b0c0">*\# this script run as root, so we need to pretend we are the normal user, or*</font>  
<font color="#a0b0c0">*\# X functionalities won't work.*</font>  
run\_on\_xserver<font color="#408010">()</font> <font color="#70a0d0">*{*</font>  
    get\_x\_user  
    DEBUG <font color="#408010">"</font><font color="#4070a0">User </font><font color="#1060a0"> $X\_USER</font><font color="#4070a0"> display </font><font color="#1060a0"> $DISP</font><font color="#4070a0"> </font><font color="#1060a0"> $1</font><font color="#4070a0"> </font><font color="#408010">"</font> INFO  
    su - <font color="#1060a0"> $X\_USER</font> -c <font color="#408010">"</font><font color="#4070a0">DISPLAY=</font><font color="#1060a0"> $DISP</font><font color="#4070a0"> </font><font color="#1060a0"> $1</font><font color="#408010">"</font>  
<font color="#70a0d0">*}*</font>

<font color="#5b3674">*HOTKEY*</font>=<font color="#1060a0"> $3</font>

<font color="#5b3674">*TYPE*</font>=<font color="#1060a0"> $1</font>

DEBUG <font color="#408010">"</font><font color="#4070a0">Custom event script for ThinkPad ibm\_acpi driver</font><font color="#408010">"</font> INFO

<font color="#a0b0c0">*\# we discard $2 which is the name of the current scheme.*</font>  
<font color="#007020">**set** </font><font color="#1060a0"> $HOTKEY</font>  <font color="#a0b0c0">*\# powersaved gives us "other '&lt;current\_scheme\_name&gt;' '&lt;content of /proc/acpi/event&gt;'"*</font>  
        <font color="#a0b0c0">*\# so we must split $3 to get the contents of /proc/acpi/event.*</font>  
<font color="#5b3674">*EVENT*</font>=<font color="#1060a0"> $1</font>   <font color="#a0b0c0">*\# "ibm/hotkey"*</font>  
<font color="#5b3674">*ACPI*</font>=<font color="#1060a0"> $2</font>    <font color="#a0b0c0">*\# "HOTK"*</font>  
<font color="#5b3674">*WHAT*</font>=<font color="#1060a0"> $3</font>    <font color="#a0b0c0">*\# "00000080"*</font>  
<font color="#5b3674">*SERIAL*</font>=<font color="#1060a0"> $4</font>  <font color="#a0b0c0">*\# "0000100c" Fn+F12*</font>

<font color="#a0b0c0">*\# it is easier to deal with numerical values (for me :-)*</font>  
<font color="#007020">**declare**</font> <font color="#5b3674">*-i*</font> <font color="#5b3674">*VAL*</font>  
<font color="#5b3674">*VAL*</font>=0x<font color="#1060a0"> $WHAT</font> <font color="#a0b0c0">*\# hex -&gt; decimal*</font>  
<font color="#007020">**declare**</font> <font color="#5b3674">*-i*</font> <font color="#5b3674">*SER*</font>  
<font color="#5b3674">*SER*</font>=0x<font color="#1060a0"> $SERIAL</font> <font color="#a0b0c0">*\# hex -&gt; decimal*</font>

<font color="#a0b0c0">*\# on screen display, it's always good to have visual feedback*</font>  
<font color="#5b3674">*OSD*</font>=<font color="#408010">"</font><font color="#4070a0">DISPLAY=:0.0 osd\_cat -p bottom -o 80 -A center -c green -l 1 -f -\*-lucidatypewriter-\*-r-\*-\*-\*-240-\*-\*-\*-\*-\*-\*</font><font color="#408010">"</font>

<font color="#a0b0c0">*\# configration file of kxdocker, needed to change it so kxdocker is started at correct position when display mode* </font>  
<font color="#a0b0c0">*\# changed between clone and xinemera mode*</font>  
<font color="#5b3674">*KXDOCKER\_CONF*</font>=<font color="#408010">"</font><font color="#4070a0">/home/huahaiy/.kde/share/apps/kxdocker/kxdocker\_conf.xml</font><font color="#408010">"</font>

<font color="#4c8f2f">**if**</font> <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $EVENT</font><font color="#408010">"</font> <font color="#4c8f2f">**=**</font> <font color="#4070a0">"ibm/hotkey"</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
  <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">log event</font><font color="#408010">"</font>  
  <font color="#4c8f2f">**if**</font> <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $VAL</font><font color="#408010">"</font> <font color="#4c8f2f">**-eq**</font> <font color="#40a070">128</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
    <font color="#4c8f2f">**case**</font> <font color="#1060a0"> $SER</font> <font color="#4c8f2f">**in**</font>  
      4097<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F1</font><font color="#408010">"</font>   
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">make wireless connection</font><font color="#408010">"</font>  
        /home/huahaiy/bin/wireless.sh <font color="#408010">&</font>  
        <font color="#007020">**;;**</font>  
      4098<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F2</font><font color="#408010">"</font>   
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">lock screen</font><font color="#408010">"</font>  
        <font color="#a0b0c0">*\#run\_on\_xserver "dcop kdesktop KScreensaverIface lock"* </font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xscreensaver-command -lock</font><font color="#408010">"</font>  
        <font color="#007020">**;;**</font>  
      4099<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F3</font><font color="#408010">"</font>  
        <font color="#a0b0c0">*\#if \[ -x /opt/thinkpad/pm/onscreen\_pm.sh \] ; then*</font>  
        <font color="#a0b0c0">*\#    run\_on\_xserver "/opt/thinkpad/pm/onscreen\_pm.sh start" &*</font>  
        <font color="#a0b0c0">*\#    ACTION="start onscreen\_pm applet"*</font>  
        <font color="#a0b0c0">*\#else*</font>  
        <font color="#a0b0c0">*\#    run\_on\_xserver "xset dpms force off" &*</font>  
        <font color="#a0b0c0">*\#    ACTION="blank screen"*</font>  
        <font color="#a0b0c0">*\#fi*</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">enter powersave mode</font><font color="#408010">"</font>  
        powersave -e Powersave  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'Power Save Mode' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>   
        <font color="#007020">**;;**</font>  
      4100<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F4</font><font color="#408010">"</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">suspend-to-ram</font><font color="#408010">"</font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xscreensaver-command -lock</font><font color="#408010">"</font> <font color="#408010">&</font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xset dpms force suspend</font><font color="#408010">"</font>  
       <font color="#408010"> . </font><font color="#1060a0"> $SYSCONF\_DIR</font>/<font color="#007020">**sleep**</font>  
        <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $DISABLE\_USER\_SUSPEND2RAM</font><font color="#408010">"</font> <font color="#4c8f2f">**!=**</font> <font color="#408010">"</font><font color="#4070a0">yes</font><font color="#408010">"</font> <font color="#408010">\]</font> <font color="#408010">&&</font> powersave <font color="#408010">"</font><font color="#4070a0">--</font><font color="#1060a0"> $ACTION</font><font color="#408010">"</font>  
        <font color="#007020">**;;**</font>  
      4101<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F5</font><font color="#408010">"</font>   
        <font color="#4c8f2f">**if**</font> <font color="#408010">\[</font> <font color="#4c8f2f">**-x**</font> /opt/thinkpad/ac/onscreen\_ac.sh <font color="#408010">\]</font> <font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
          run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">/opt/thinkpad/ac/onscreen\_ac.sh start</font><font color="#408010">"</font> <font color="#408010">&</font>  
          <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">start onscreen\_ac applet</font><font color="#408010">"</font>  
        <font color="#4c8f2f">**elif**</font> <font color="#007020">**grep**</font> <font color="#4c8f2f">**-q**</font> <font color="#408010">"</font><font color="#4070a0">status.\*disabled</font><font color="#408010">"</font> /proc/acpi/ibm/bluetooth <font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
          <font color="#007020">**echo**</font><font color="#4070a0"> enable </font><font color="#4c8f2f">**&gt;**</font> /proc/acpi/ibm/bluetooth  
          <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">enable blooetooth</font><font color="#408010">"</font>  
        <font color="#4c8f2f">**else**</font>  
          <font color="#007020">**echo**</font><font color="#4070a0"> disable </font><font color="#4c8f2f">**&gt;**</font> /proc/acpi/ibm/bluetooth  
          <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">disable blooetooth</font><font color="#408010">"</font>  
        <font color="#4c8f2f">**fi**</font>  
        <font color="#007020">**;;**</font>  
      4102<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F6</font><font color="#408010">"</font>   
        powersave -e Performance  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'Full Performance Mode' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">enter full performance mode</font><font color="#408010">"</font>  
        <font color="#007020">**;;**</font>  
      4103<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F7</font><font color="#408010">"</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">toggle external display</font><font color="#408010">"</font>  
        <font color="#a0b0c0">*\#echo video\_switch &gt; /proc/acpi/ibm/video*</font>  
        <font color="#4c8f2f">**if**</font> run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr -q</font><font color="#408010">"</font> <font color="#408010">|</font> <font color="#007020">**grep**</font> <font color="#408010">"</font><font color="#4070a0">VGA connected</font><font color="#408010">";</font> <font color="#4c8f2f">**then**</font>   
          <font color="#4c8f2f">**if**</font> run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr -q</font><font color="#408010">"</font> <font color="#408010">|</font> <font color="#007020">**grep**</font> <font color="#408010">"</font><font color="#4070a0">VGA connected \[0-9\]\\+</font><font color="#408010">";</font> <font color="#4c8f2f">**then**</font>  
            run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'Turn OFF External VGA Display' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>  
            run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr --output VGA --off</font><font color="#408010">"</font>  
          <font color="#4c8f2f">**else**</font>   
            run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'Turn ON External VGA Display' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>  
            run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr --output VGA --mode 1024x768</font><font color="#408010">"</font>  
          <font color="#4c8f2f">**fi**</font>  
        <font color="#4c8f2f">**else**</font>  
          <font color="#a0b0c0">*\# if VGA is unplugged, mark it off, and restart kxdocker with correct position*</font>  
          run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'External VGA Display is DISCONNECTED' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>  
          run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">dcop kxdocker MainApplication-Interface quit</font><font color="#408010">"</font>  
          run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr --output VGA --off</font><font color="#408010">"</font>  
          <font color="#007020">**sed**</font> <font color="#4c8f2f">**-i**</font> <font color="#4c8f2f">**-e**</font> <font color="#408010">'</font><font color="#4070a0">s/LeftForce="-512"/LeftForce="0"/</font><font color="#408010">'</font> <font color="#1060a0"> $KXDOCKER\_CONF</font>  
          run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">kxdocker</font><font color="#408010">"</font>  
        <font color="#4c8f2f">**fi**</font>  
        <font color="#007020">**;;**</font>  
      4104<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F8</font><font color="#408010">"</font>   
        <font color="#a0b0c0">*\#ACTION="expand screen"*</font>  
        <font color="#a0b0c0">*\#echo expand\_toggle &gt; /proc/acpi/ibm/video*</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">toggle monitor layout</font><font color="#408010">"</font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">dcop kxdocker MainApplication-Interface quit</font><font color="#408010">"</font>  
        <font color="#4c8f2f">**if**</font> run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr -q</font><font color="#408010">"</font> <font color="#408010">|</font> <font color="#007020">**grep**</font> <font color="#408010">"</font><font color="#4070a0">VGA connected</font><font color="#408010">";</font> <font color="#4c8f2f">**then**</font>   
          <font color="#4c8f2f">**if**</font> run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr -q</font><font color="#408010">"</font> <font color="#408010">|</font> <font color="#007020">**grep**</font> <font color="#408010">"</font><font color="#4070a0">VGA connected 1024x768+1024</font><font color="#408010">";</font> <font color="#4c8f2f">**then**</font>  
            run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'Switch to Clone Mode' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>   
            run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr --output VGA --pos 0x0 --fb 2048x768</font><font color="#408010">"</font>  
          <font color="#4c8f2f">**else**</font>  
            run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'Switch to Xinerama Mode' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>  
            run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr --output VGA --pos 1024x0 --fb 2048x768</font><font color="#408010">"</font>  
          <font color="#4c8f2f">**fi**</font>  
          <font color="#007020">**sed**</font> <font color="#4c8f2f">**-i**</font> <font color="#4c8f2f">**-e**</font> <font color="#408010">'</font><font color="#4070a0">s/LeftForce="0"/LeftForce="-512"/</font><font color="#408010">'</font> <font color="#1060a0"> $KXDOCKER\_CONF</font>  
        <font color="#4c8f2f">**else**</font>  
          run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'External VGA Display is DISCONNECTED' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>  
          run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xrandr --output VGA --off</font><font color="#408010">"</font>  
          <font color="#007020">**sed**</font> <font color="#4c8f2f">**-i**</font> <font color="#4c8f2f">**-e**</font> <font color="#408010">'</font><font color="#4070a0">s/LeftForce="-512"/LeftForce="0"/</font><font color="#408010">'</font> <font color="#1060a0"> $KXDOCKER\_CONF</font>  
        <font color="#4c8f2f">**fi**</font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">kxdocker</font><font color="#408010">"</font>  
        <font color="#007020">**;;**</font>      
      4105<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F9</font><font color="#408010">"</font>  
        <font color="#a0b0c0">*\#ACTION="undock"*</font>  
        <font color="#a0b0c0">*\#echo undock &gt; /proc/acpi/ibm/dock*</font>  
        powersave -e Presentation  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'Presentation Mode' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">enter presentation mode</font><font color="#408010">"</font>  
        <font color="#007020">**;;**</font>  
      4106<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F10</font><font color="#408010">"</font> <font color="#007020">**;;**</font>  
      4107<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F11</font><font color="#408010">"</font>   
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">make NIC connection</font><font color="#408010">"</font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">echo 'Connecting LAN...' | </font><font color="#1060a0"> $OSD</font><font color="#408010">"</font> <font color="#408010">&</font>  
        /home/huahaiy/bin/nic.sh <font color="#408010">&</font>  
        <font color="#007020">**;;**</font>  
      4108<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+F12</font><font color="#408010">"</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">suspend-to-disk</font><font color="#408010">"</font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">xscreensaver-command -lock</font><font color="#408010">"</font> <font color="#408010">&</font>  
       <font color="#408010"> . </font><font color="#1060a0"> $SYSCONF\_DIR</font>/<font color="#007020">**sleep**</font>  
        <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $DISABLE\_USER\_SUSPEND2DISK</font><font color="#408010">"</font> <font color="#4c8f2f">**!=**</font> <font color="#408010">"</font><font color="#4070a0">yes</font><font color="#408010">"</font> <font color="#408010">\]</font> <font color="#408010">&&</font> powersave <font color="#408010">"</font><font color="#4070a0">--</font><font color="#1060a0"> $ACTION</font><font color="#408010">"</font>  
        <font color="#007020">**;;**</font>  
      4109<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+Backspace</font><font color="#408010">"</font> <font color="#007020">**;;**</font>  
      4110<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+Insert</font><font color="#408010">"</font> <font color="#007020">**;;**</font>  
      4111<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+Delete</font><font color="#408010">"</font> <font color="#007020">**;;**</font>  
      4112<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+Home</font><font color="#408010">"</font>  
        powersave -ku  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">brighter display</font><font color="#408010">"</font>   
        <font color="#007020">**;;**</font>  
      4113<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+End</font><font color="#408010">"</font>  
        powersave -kd  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">dimmer display</font><font color="#408010">"</font>   
        <font color="#007020">**;;**</font>  
      4116<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Fn+Zoom</font><font color="#408010">"</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">toggle screen resolution</font><font color="#408010">"</font>  
        <font color="#a0b0c0">*\#run\_on\_xserver "/home/huahaiy/bin/toggle-zoom.sh"*</font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">ksnapshot</font><font color="#408010">"</font>  
        <font color="#007020">**;;**</font>  
      4120<font color="#007020">**)**</font>   <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Thinkpad</font><font color="#408010">"</font>  
        run\_on\_xserver <font color="#408010">"</font><font color="#4070a0">konsole</font><font color="#408010">"</font> <font color="#408010">&</font>  
        <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">launch konsole</font><font color="#408010">"</font>  
        <font color="#007020">**;;**</font>  
      \*<font color="#007020">**)**</font>      <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Unidentified</font><font color="#408010">"</font> <font color="#007020">**;;**</font>  
    <font color="#4c8f2f">**esac**</font>  
  <font color="#4c8f2f">**else**</font>  
    <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Unidentified</font><font color="#408010">"</font>  
  <font color="#4c8f2f">**fi**</font>    
  DEBUG <font color="#408010">"</font><font color="#1060a0"> $HOTKEY</font><font color="#4070a0"> hotkey: keycode </font><font color="#1060a0"> $VAL</font><font color="#4070a0"> serial </font><font color="#1060a0"> $SER</font><font color="#4070a0">. action: </font><font color="#1060a0"> $ACTION</font><font color="#4070a0"> </font><font color="#408010">"</font> INFO  
<font color="#4c8f2f">**elif**</font> <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $EVENT</font><font color="#408010">"</font> <font color="#4c8f2f">**=**</font> <font color="#4070a0">"ibm/bay"</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
  <font color="#4c8f2f">**case**</font> <font color="#1060a0"> $VAL</font> <font color="#4c8f2f">**in**</font>  
    1<font color="#007020">**)**</font>  <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Eject lever inserted</font><font color="#408010">"</font> <font color="#007020">**;;**</font>  
    3<font color="#007020">**)**</font>  <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Eject Request</font><font color="#408010">"</font> <font color="#007020">**;;**</font>  
    \*<font color="#007020">**)**</font>  <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Unidentified</font><font color="#408010">"</font> <font color="#007020">**;;**</font>  
  <font color="#4c8f2f">**esac**</font>  
  DEBUG <font color="#408010">"</font><font color="#1060a0"> $HOTKEY</font><font color="#4070a0"> UltraBay event: </font><font color="#1060a0"> $EVENT</font><font color="#4070a0"> </font><font color="#408010">"</font> INFO  
<font color="#4c8f2f">**elif**</font> <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $EVENT</font><font color="#408010">"</font> <font color="#4c8f2f">**=**</font> <font color="#4070a0">"ibm/dock"</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
  <font color="#4c8f2f">**case**</font> <font color="#1060a0"> $VAL</font> <font color="#4c8f2f">**in**</font>  
    0<font color="#007020">**)**</font>  <font color="#4c8f2f">**if**</font> <font color="#408010">\[</font> <font color="#1060a0"> $SER</font> <font color="#4c8f2f">**-eq**</font> <font color="#40a070">3</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font> <font color="#a0b0c0">*\# X32 has strange dock code*</font>  
      <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Dock requested</font><font color="#408010">"</font>  
      <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">Docking</font><font color="#408010">"</font>  
      <font color="#007020">**echo**</font><font color="#4070a0"> dock </font><font color="#4c8f2f">**&gt;**</font> /proc/acpi/ibm/dock <font color="#40a070">2</font><font color="#4c8f2f">**&gt;**</font><font color="#408010">&</font><font color="#40a070">1</font>  
      <font color="#4c8f2f">**fi**</font>  
      <font color="#007020">**;;**</font>  
    1<font color="#007020">**)**</font>  <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Dock requested</font><font color="#408010">"</font>  
      <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">Docking</font><font color="#408010">"</font>  
      <font color="#007020">**echo**</font><font color="#4070a0"> dock </font><font color="#408010">&gt;</font> /proc/acpi/ibm/dock <font color="#40a070">2</font><font color="#408010">&gt;&1</font>  
      <font color="#007020">**;;**</font>  
    3<font color="#007020">**)**</font>  <font color="#5b3674">*HOTKEY*</font>=<font color="#408010">"</font><font color="#4070a0">Undock requested</font><font color="#408010">"</font>  
      <font color="#5b3674">*ACTION*</font>=<font color="#408010">"</font><font color="#4070a0">Undocking</font><font color="#408010">"</font>  
      <font color="#007020">**echo**</font><font color="#4070a0"> undock </font><font color="#408010">&gt;</font> /proc/acpi/ibm/dock <font color="#40a070">2</font><font color="#408010">&gt;&1</font>  
      <font color="#007020">**;;**</font>  
    <font color="#4c8f2f">**esac**</font>  
    DEBUG <font color="#408010">"</font><font color="#1060a0"> $HOTKEY</font><font color="#4070a0">: keycode </font><font color="#1060a0"> $VAL</font><font color="#4070a0"> serial </font><font color="#1060a0"> $SER</font><font color="#4070a0">. action: </font><font color="#1060a0"> $ACTION</font><font color="#4070a0"> </font><font color="#408010">"</font> INFO  
<font color="#4c8f2f">**else**</font>  
    DEBUG <font color="#408010">"</font><font color="#4070a0">Unidentified event: </font><font color="#1060a0"> $EVENT</font><font color="#4070a0"> </font><font color="#1060a0"> $ACPI</font><font color="#4070a0"> </font><font color="#1060a0"> $WHAT</font><font color="#4070a0"> </font><font color="#1060a0"> $SERIAL</font><font color="#408010">"</font> INFO  
<font color="#4c8f2f">**fi**</font>

<font color="#1060a0"> $SCRIPT\_RETURN</font> <font color="#1060a0"> $EV\_ID</font> <font color="#40a070">0</font> <font color="#408010">"</font><font color="#1060a0"> $ME</font><font color="#4070a0"> finished</font><font color="#408010">"</font>  
EXIT <font color="#40a070">0</font>  

</font>

Notice that you need to install *osd\_cat* package to get on-screen display, or you can comments out them. Also, I used *xscreensaver* to lock screen, because KDE screen saver and locker do not support [ThinkFinger](http://thinkfinger.sourceforge.net/). I like the coolness of login and unlocking screen with a finger swipe :) Finally, I use simple scripts to make network connections. Here is *nic.sh*:

<font face="monospace" size="1em">  
<font color="#a0b0c0">*\#!/bin/sh*</font>

<font color="#a0b0c0">*\# This script brings up wired network connection (plug in cable first!). With* </font>  
<font color="#a0b0c0">*\# augument "stop", it turns off wireless network interface. Root privilige*</font>  
<font color="#a0b0c0">*\# is required to run* </font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\# Author: Huahai Yang, Oct 15, 2007*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#4c8f2f">**if**</font> <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $1</font><font color="#408010">"</font> <font color="#4c8f2f">**=**</font> <font color="#4070a0">"stop"</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
  ifdown eth0  
<font color="#4c8f2f">**else**</font>   
  ifup eth0

  <font color="#a0b0c0">*\# restart some services that depends on networking*</font>  
  <font color="#a0b0c0">*\#/etc/init.d/samba restart*</font>  
  /etc/init.d/spamassassin restart  
<font color="#4c8f2f">**fi**</font>  

</font>

And here is *wireless.sh*

<font face="monospace" size="1em">  
<font color="#a0b0c0">*\#!/bin/sh*</font>  
<font color="#a0b0c0">*\# This script use Matthew Brett's wlan-ui.pl to select a wireless AP to* </font>  
<font color="#a0b0c0">*\# connect to. With augument "stop", it turns off wireless network interface.*</font>  
<font color="#a0b0c0">*\# Root privilige is required to run* </font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#a0b0c0">*\# Author: Huahai Yang*</font>  
<font color="#a0b0c0">*\#*</font>  
<font color="#4c8f2f">**if**</font> <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $1</font><font color="#408010">"</font> <font color="#4c8f2f">**=**</font> <font color="#4070a0">"stop"</font> <font color="#408010">\]</font><font color="#408010">;</font>  
<font color="#4c8f2f">**then**</font>  
  ifconfig eth1 down  
  /etc/init.d/ipw3945d stop  
  modprobe <font color="#4c8f2f">**-r**</font> ipw3945  
<font color="#4c8f2f">**else**</font>   
  /etc/init.d/ipw3945d start  
  <font color="#5b3674">*DISPLAY*</font>=:0.<font color="#40a070">0</font> wlan-ui.pl

  <font color="#a0b0c0">*\# restart some services that depends on networking*</font>  
  <font color="#a0b0c0">*\#/etc/init.d/samba restart*</font>  
  /etc/init.d/spamassassin restart  
<font color="#4c8f2f">**fi**</font>  

</font>

[wlan-ui.pl](http://wlan-ui.sourceforge.net/wlan-ui_pod.html) is a GTK-2 based little GUI program that scans the available wireless access points, and allows you to connect to one of them. The only configuration needed is to put the name of your wireless card kernel module name in */etc/wlan-uirc*, mine has a line:* $MODULE='ipw3945'*

**Configure X hotkeys**

ACPI does not deal with the rest of the hotkeys. But most of these can be seen by X server, so it's possible to map them to any functions you like.

First, need to get their keycodes. Use *xev* to do that and write down the keycodes.

Second, edit your *~/.Xmodmap*, put these keycodes in, assign them reasonable XF86 names, and mine is here:

```
! Page Left, Right keycode 234 = F19 keycode 233 = F20`

! multimedia  
keycode 162 = XF86AudioPlay  
keycode 164 = XF86AudioStop  
keycode 153 = XF86AudioNext  
keycode 144 = XF86AudioPrev

! volume up, down  
keycode 174 = XF86AudioLowerVolume  
keycode 176 = XF86AudioRaiseVolume

! Windows keys  
keycode 117 = XF86MenuKB  
keycode 115 = XF86Start

! No Caps Lock  
clear lock  
! Caps Lock as Win key  
add mod4 = Caps\_Lock  
```

Now try *xmodmap ~/.Xmodmap*, then go to KDE Control Center &gt; Regional and Accessibility &gt; Input Actions, and associate these keys with whatever actions you like.

To autoload your Xmodmap setting, create a file in *~/.kde/Autostart*, and put the xmodmap command in. Mine has:

` #!/bin/sh # map keys xmodmap ~/.Xmodmap`

To properly handle volume up and down keys, I associated these keys with this script:

<font face="monospace" size="1em">  
<font color="#a0b0c0">*\#!/bin/sh*</font>  
<font color="#a0b0c0">*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*</font>  
<font color="#a0b0c0">*\# Bring up or down sound volume with amixer, with on screen display*</font>  
<font color="#a0b0c0">*\# the total volume range is 58.5dB, so we change 4.5dB each run, it takes*</font>  
<font color="#a0b0c0">*\# 13 run to go from 0 to 58.5dB* </font>  
<font color="#a0b0c0">*\#* </font>  
<font color="#a0b0c0">*\# Usage: audio-volume.sh \[up|down\]*</font>  
<font color="#a0b0c0">*\#* </font>  
<font color="#a0b0c0">*\# Author: Huahai Yang*</font>  
<font color="#a0b0c0">*\# Last upated: Oct. 16, 2007*</font>  
<font color="#a0b0c0">*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*</font>

<font color="#4c8f2f">**if**</font> <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $1</font><font color="#408010">"</font> <font color="#4c8f2f">**=**</font> <font color="#4070a0">"up"</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
  <font color="#5b3674">*PERCENT*</font>=<font color="#ff0000">**<span class="underline"> $(</span>**</font><font color="#70a0d0">*amixer* </font><font color="#007020">**set**</font><font color="#70a0d0">* PCM* </font><font color="#40a070">4</font><font color="#70a0d0">*.5dB+* </font><font color="#408010">|</font><font color="#70a0d0">* \\*</font>  
<font color="#70a0d0">*    sed -n -e* </font><font color="#408010">'</font><font color="#4070a0">s/\[^\\\[\]\*\\\[</font><font color="#70a0d0">*\\(*</font><font color="#4070a0">\[0-9\]\*</font><font color="#70a0d0">*\\)*</font><font color="#4070a0">\\%\\\]\[^\\%\]\*/\\1/p</font><font color="#408010">'</font><font color="#70a0d0">* -e* </font><font color="#408010">'</font><font color="#4070a0">n</font><font color="#408010">'</font><font color="#ff0000">**<span class="underline">)</span>**</font>  
<font color="#4c8f2f">**elif**</font> <font color="#408010">\[</font> <font color="#408010">"</font><font color="#1060a0"> $1</font><font color="#408010">"</font> <font color="#4c8f2f">**=**</font> <font color="#4070a0">"down"</font> <font color="#408010">\]</font><font color="#408010">;</font> <font color="#4c8f2f">**then**</font>  
  <font color="#5b3674">*PERCENT*</font>=<font color="#ff0000">**<span class="underline"> $(</span>**</font><font color="#70a0d0">*amixer* </font><font color="#007020">**set**</font><font color="#70a0d0">* PCM* </font><font color="#40a070">4</font><font color="#70a0d0">*.5dB-* </font><font color="#408010">|</font><font color="#70a0d0">* \\*</font>  
<font color="#70a0d0">*                sed -n -e* </font><font color="#408010">'</font><font color="#4070a0">s/\[^\\\[\]\*\\\[</font><font color="#70a0d0">*\\(*</font><font color="#4070a0">\[0-9\]\*</font><font color="#70a0d0">*\\)*</font><font color="#4070a0">\\%\\\]\[^\\%\]\*/\\1/p</font><font color="#408010">'</font><font color="#70a0d0">* -e* </font><font color="#408010">'</font><font color="#4070a0">n</font><font color="#408010">'</font><font color="#ff0000">**<span class="underline">)</span>**</font>  
<font color="#4c8f2f">**else**</font>  
  <font color="#5b3674">*PERCENT*</font>=<font color="#ff0000">**<span class="underline"> $(</span>**</font><font color="#70a0d0">*amixer get PCM* </font><font color="#408010">|</font><font color="#70a0d0">* \\*</font>  
<font color="#70a0d0">*                sed -n -e* </font><font color="#408010">'</font><font color="#4070a0">s/\[^\\\[\]\*\\\[</font><font color="#70a0d0">*\\(*</font><font color="#4070a0">\[0-9\]\*</font><font color="#70a0d0">*\\)*</font><font color="#4070a0">\\%\\\]\[^\\%\]\*/\\1/p</font><font color="#408010">'</font><font color="#70a0d0">* -e* </font><font color="#408010">'</font><font color="#4070a0">n</font><font color="#408010">'</font><font color="#ff0000">**<span class="underline">)</span>**</font>  
<font color="#4c8f2f">**fi**</font> 

osd\_cat <font color="#70a0d0">*-b*</font> percentage <font color="#70a0d0">*-P*</font> <font color="#1060a0"> $PERCENT</font> <font color="#70a0d0">*-d*</font> <font color="#40a070">1</font> <font color="#70a0d0">*-p*</font> bottom <font color="#70a0d0">*-o*</font> <font color="#40a070">80</font> <font color="#70a0d0">*-i*</font> <font color="#40a070">100</font> <font color="#70a0d0">*-A*</font> left <font color="#70a0d0">*-c*</font> green <font color="#70a0d0">*-T*</font> <font color="#408010">"</font><font color="#4070a0">Sound Volume</font><font color="#408010">"</font> <font color="#408010">&</font>

</font>

That's all there is to it. Now all hotkeys work as intended, and with nice on-screen user feedback. Please let me know if I missed anything.

**Updated**: I've changed Fn+F8 key to toggle between Clone mode and Xinerama mode of dual head display, please see [this post](http://yyhh.org/blog/2007/11/dual-head-xrandr-1-2-revisited) for details.
