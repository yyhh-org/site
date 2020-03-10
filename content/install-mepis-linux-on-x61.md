---
Title: Install MEPIS Linux on X61
Date: 2007-10-28 00:58
Author: Huahai
Category: notebook
Tags: Linux
Slug: install-mepis-linux-on-x61
Alias: /blog/2007/10/install-mepis-linux-x61
Lang: en
---

I got a brand new Thinkpad X61 laptop last Saturday. Unfortunately, the factory loaded Vista Home Basic was too bloated and ate up 700MB memory from a fresh boot without launching any application! If you know me, you know what I will do - remove Windows and load up Linux!

The Linux distribution of my choice has always been [SimplyMEPIS](/www.mepis.org). It's a KDE distribution, which I like better than its major alternative Gnome. The latest SimplyMEPIS is 7.0rc5. This version of MEPIS went back to their original pure Debian roots. Their 6.x versions were based on Ubuntu, which I always thought was a bad decision. I am glad that they now realized it too.

**Installation**

Before installation, I changed BIOS setting so that hard-disk is in "compatibility"mode. I downloaded, burned to CD, and then loaded the MEPIS 7.0rc5 LiveCD with a portable USB CD-ROM, because X61 doesn't have an internal CD-ROM (it's a tiny machine). Clicking "Install MEPIS" icon on the desktop started the installation. The installation was smooth as always. I did not touch the 4GB Thinkpad reserved partition, so Thinkpad's Recover and Rescue function should be fine. In case I need to send in the laptop for warranty service, I can always turn it back to factory state.

**Graphics and Network**

The integrated Intel X3100 graphic chip was not recognized after installation. So I had to work in 640x480 at the beginning. To fix that, I need to get the Intel graphic driver from Debian "testing" pool. First thing first, get a network connection. This version of MEPIS has already gotten the Intel 3945ABG wireless driver installed. After fiddling with the MEPIS Network Assistant software for a few minutes, I got the wireless network working. Installed the Intel graphic driver:

` apt-get install xserver-xorg-video-intel`

Then edit */etc/X11/xorg.conf*, changed driver to "intel" . So the device section looks like this:

` Section "Device" Identifier      "Generic Video Card" Driver          "intel" BusID           "PCI:0:2:0" EndSection`

Hit ctrl-alt-backspace to restart X, and I got a nice 1024x768 desktop.

**Sound**

The loaded MEPIS kernel version is 2.6.22.1, which still has some bugs that prevent the integrated Intel AD1984 sound chip from working. There are two solutions, both involve changing the kernel. One can download a patch and rebuild snd-hda-intel module to fix it, or can get the latest kernel 2.6.23, which has already fixed the bugs. I sort of did both: I got a valina kernel source 2.6.22.9, applied some patches, and built my own kernel (I omitted the steps here. I can write a guide later if anyone interested).

The reason I did not go with 2.6.23 is that I want the [-ck patch](http://members.optusnet.com.au/ckolivas/kernel/). -ck patch has always been on my Linux desktops because it's better than mainline kernel in term of UI responsiveness. The latest-ck patch is for 2.6.22. It's sad that the author of this patch, [Con Koliva, has left kernel hacking](http://apcmag.com/6735/interview_con_kolivas). So this is also the last -ck patch I will ever get to use. Of course, after plugging in the new kernel, I got the voice back.

**Fingerprint Reader**

This X61 has a Fingerprint Reader, which of course can be used for authentication purpose. For this, an open source driver [ThinkFinger](http://thinkfinger.sourceforge.net/) can be used. Downloaded, unpacked, *./configure, make, make install*. Tried out the command line tf-tool to enroll and verified my fingerprint, and it worked. Also, I can use console login and su with a finger swipe.

Nice, now I wanted to use it in GUI applications, for example, using a finger swipe to login, to unlock the screensaver, etc. ThinkFinger uses PAM for these purposes. Unfortunately, KDE does not support PAM authentication well, as [the guide on ThinkWiki](http://www.thinkwiki.org/wiki/How_to_enable_the_fingerprint_reader_with_ThinkFinger) suggested. Here, the flexibility of open source software kicked in. It turns out that I could just use gnome's display manager GDM, instead of the KDE's default KDM. GDM support ThinkFinger very well. So I installed gdm.

` apt-get install gdm`

During the installation, it even asked me to choose between gdm and kdm. Aftr I chose gdm, restart X, I could use my finger to login! Once logged in, I still get a KDE desktop with no loss of functionality. How about screen lock/unlock? Well, I have to remove KDE's kscreensaver, and installed xscreensaver. It handles ThinkFinger very well.

In summary, all the hardware of Thinkpad X61 were supported by Linux. I am happy with this result.  
What about the memory usage I was complaining about Vista? Well, some people say that KDE is bloated, but compared with Vista, it's nothing. After booting up my fully loaded KDE desktop, the memory stands at 170MB. Look at Vista's 700MB, how about that for a comparison?
