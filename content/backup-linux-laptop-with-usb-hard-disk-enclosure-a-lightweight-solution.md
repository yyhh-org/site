---
Status: published
Title: "Backup Linux Laptop with USB Hard-disk Enclosure: a Lightweight Solution"
Date: 2007-11-12 00:00
Author: Huahai
Category: notebook
Tags: Linux
Slug: backup-linux-laptop-with-usb-hard-disk-enclosure-a-lightweight-solution
Alias: /blog/2007/11/backup-linux-laptop-usb-hard-disk-enclosure-lightweight-solution
Lang: en
---

Most of Linux laptop users have done some customizations on the system so it works the way we wanted. Now we want to save the fruit of our hard labor in case bad things happen. We want to backup not just the */home* directory, but the whole */* directory, minus some runtime generated files. In the past I have used some heavy-weight applications such as [unison](https://www.cis.upenn.edu/~bcpierce/unison/) and [backuppc](https://backuppc.sourceforge.net/). These worked well, but they required setting up servers that run all the time. For my Thinkpad laptop, I decided to use a simple and lightweight solution, but still keeping the nice features such as data compression, exclude files, and incremental backup. A script called [rdiff-backup](https://www.nongnu.org/rdiff-backup/) seems to do the trick, and KDE has a GUI front end called [keep](https://www.kde-apps.org/content/show.php?content=32984) for it.

I use a hand-disk in a USB Enclosure as my backup storage. When I need backup, I simply plug it in. However, I found that *rdiff-backup* really like that filesystem on the backup media is the same as the source media, or there will be some errors. Using *gparted*, I formatted one of the disk partitions as an *ext3* filesystem for Linux backup. The other partition on the hard-disk is *ntfs*, for Windows backup. Now I needed to properly mount the disk when I plug it it. The default automount service provided by *udev* and *hal* doesn't seem to cut it here. So I wrote an udev rule specifically for this USB enclosure, and mount its two partitions under special mount points */mnt/backup1* and */mnt/backup2*.

First, we need to find out the "idVender" and "idProduct" values for the USB Enclosure, so our udev rule will be invoked when this particular device is plugged in.

`lsusb`

will just do that. The ID field reads something like "06e1:0834", where the former number is vendor id, and later product id. With this information, my udev rule */etc/udev/rules.d/80\_usb\_backup\_disk.rules* is shown below:

` # # udev rules file for ADS Tech USB Harddisk Enclosure, used for backup # SYSFS{idVendor}=="06e1", SYSFS{idProduct}=="0834", NAME="backup%n"`

What this rule does is to create device nodes under */dev* when this USB enclosure is plugged in, and the names of the nodes start with "backup", followed by numbers that reflect the partitions on the disk. In my case, I got */dev/backup1* and */dev/backup2* because I have two partitions on my disk. Of course, you need to reboot for the rule to take effect.

Now we need to mount it correctly. Let's first create two mount points for these two partitions. As root,

`mkdir /mnt/backup1 mkdir /mnt/backup2`

The simplest method for automount is to edit */etc/fstab*, add entry for each partition:

` /dev/backup1 /mnt/backup1 ext3 users,noauto,noatime 0 0 /dev/backup2 /mnt/backup2 ntfs-3g users,exec,noauto,umask=000 0 0`

The first entry is for the first partition, it has a Linux ext3 filesystem. The second entry for Windows, and it uses the new *ntfs-3g* user space program to read/write NTFS file system. For some reason, the ext3 filesystem mounted this way does not allow normal user to create directory in it even though "users"option is set. However, it does not matter much since I run *keep* as root anyway, for we are backing up the whole root directory.

**Updated 11/26/2007 08:42:52 AM (EST)** After update to a newer version of ntfs-3g, I got a "fusemount" error regarding permission.  

`chmod 4755 $(which ntfs-3g)`

as root fixed it.

**Updated 11/30/2007 01:57:27 AM (EST)** I accidentally deleted my address book folder today, but I was able to restore the folder with rdiff-backup. KDE address book is stored under *~/.kde/share/apps/kabc*, to restore it from backup, I used the following command as root:  

`rdiff-backup -r 3D /mnt/backup1/Huahai-X61/home/huahaiy/.kde/share/apps/kabc /home/huahaiy/.kde/share/apps/kabc`

</p>
</p>
