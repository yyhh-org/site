---
Title: Thinkpad Hotkeys in KDE4
Date: 2010-12-01 22:00
Author: Huahai
Category: notebook
Tags: Linux
Slug: thinkpad-hotkeys-in-kde4
Alias: /blog/2010/12/thinkpad-hotkeys-kde4
Lang: en
---

I have kept my Thinkpad X61 laptop up to date with Debian sid for a few years. The KDE4 in Debian sid is at version **4.4.5** at this moment, and I think it is mature enough for me to switch the laptop power management from [my own hacked up solution](/blog/2007/10/thinkpad-x61-hotkeys-solution-debian-linux) to a KDE integrated one. My old solution still works for the most part, but there are some glitches after repeated supsend-resume cycles. As the system keeps evolving, I suspect more things would break.

Power management in KDE4 is handled by PowerDevil, which is disabled if powersaved is running (my old solution relied on powersaved). First I uninstalled powersaved and reboot, sure enough, all Fn hotkeys stops working. Now I go to KDE **System Settings -&gt; Advanced -&gt; Power Management**, and see the PowerDevil seems to be in a health state. The problem is that the hotkey presses are intercepted by ACPI so KDE does not receive these events. To stop the interruption, I edit **/etc/modules** as root and comment out **thinkpad\_acpi** module, reboot. Now the Fn hotkeys should be registered in KDE, all we need to do is to make them do things we want. 

To set up global hotkeys, we go to **System Settings -&gt; Input Actions**, I add a new group called *My Shortcuts* and enabled it. Right-click *My Shortcuts*, **New-&gt;Global Shortcut-&gt;DBus Command**, I create a new entry *Hibernate*, and in the **Action** tab fill in needed dbus information for hibernating the system with PowerDevil (See screenshot). Basically, this is similar to issuing a console command "qdbus org.kde.powerdevil /modules/powerdevil suspend 4". Here, the parameter 4 is for hibernate (suspend to disk), 2 is for sleep (suspend to memory), and 1 for lock screen.  In the **Trigger** tab, click the button, and press Fn+F12, notice that KDE recognizes this key as a Suspend key. Now click **Apply**, the Fn+F12 hotkey is setup. Now try Fn+F12, the system should hibernate. So far, the hibernate-resume cycles seem to be clean and problem free for me. I am using 2.6.36 kernel. 

Overall, this seems to be easy enough. No scripts, no hacks.

<img src="https://farm6.static.flickr.com/5082/5224299173_5c53303d52.jpg" width="500" height="378" alt="hibernate-snapshot2" />
