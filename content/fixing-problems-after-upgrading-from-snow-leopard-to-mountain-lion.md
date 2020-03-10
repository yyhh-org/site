---
Title: Fixing Problems after Upgrading from Snow Leopard to Mountain Lion
Date: 2012-09-24 00:28
Author: Huahai
Category: notebook
Tags: Software, OSX 
Slug: fixing-problems-after-upgrading-from-snow-leopard-to-mountain-lion
Alias: /blog/2012/09/fixing-problems-after-upgrading-snow-leopard-mountain-lion
Lang: en
---

The IT department of my company has been urging us Mac users to upgrade OSX to Lion a long time ago. After getting a few papers submitted last week, I finally got around to upgrade the Snow Leopard for my Macbook Pro work machine. Since I couldn't find Lion on Apple Store any more, I decided to go straight to Mountain Lion. The download and installation went smoothly, and most things seemed to work after the upgrade. Here are a few things that broke and the fixes I found.

### SSH with public key

Mountain Lion changed a few things that broke password-free SSH access to and from OSX using public/private key pairs.

*SSH from Mountain Lion to older SSH severs:*

Mountain Lion upgraded openssh client to version 5.9p1. SSH to some older version of ssh server would not work ("Connection reset by peer") due to ciphers being too long. We can use a shorter one by adding to file "~/.ssh/config".

    :::cfg
    Host address\_of\_your\_ssh\_server  
    Ciphers aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,aes192-cbc,aes256-cbc,arcfour

This problem is a known issue of openssh. I remember did this fix for my Linux machines.

*SSH to Mountain Lion:*

This one took me a lot of googling to find the [cause](http://www.hkwebentrepreneurs.com/2012/08/password-free-ssh-on-os-x-mountain-lion.html). Basically, Mountain Lion changed /etc/sshd\_config file, so that openssh server only checks "~/.ssh/authorized\_keys" now, instead of checking both that and "~/.ssh/authorized\_keys2". To fix this, all we need to do is to rename the later to the former.

    :::bash
    $ mv ~/.ssh/authorized_keys2 ~/.ssh/authorized_keys

I find this change rather annoying, as it adds little benefit but creates a lot of troubles. For example, it broke my backup solution. I am using [backuppc](http://backuppc.sourceforge.net/) to backup this Macbook to a central backup server through password-less SSH. It took me a while to debug when backuppc reported the problem.

### Homebrew

Running "brew doctor" would show the information needed to fix homebrew. Basically, one had to install xcode 4.5, install command line tools, install X, and so on. A lot of downloads and wait time.

### Latex

All the latex programs were not in path any more. Since my latex distribution was pretty old anyway. I chose to download the latest version of MacTex to install. It took a long time to download though.

### Lotus Notes

Mountain Lion has its own Notes.app now, which conflicts with Lotus Notes. During upgrading, Lotus Notes will be moved to be under a directory "/Application/Lotus Notes Local" or something similar. All you need to do is to find Notes.app in there, and rename it something else, e.g. "LNotes.app", and move it back to be under "/Application".

### Java

Java is not installed by default. When using applications require it, you will be prompted to install.

In conclusion, the upgrade from Snow Leopard to Mountain Lion works reasonablly OK, but be prepared to fix some problems. I think the upgrade experience of OSX is not better than Linux, as both require a similar amount of tweakings and searching solutions. However, upgrading in OSX costs money. If this was not on company tab and by their urging, I would not have bothered.
