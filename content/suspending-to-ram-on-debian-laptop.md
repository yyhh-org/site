---
Title: Suspending to RAM on Debian laptop
Date: 2008-04-17 23:39
Author: Huahai
Category: notebook
Tags: Linux
Slug: suspending-to-ram-on-debian-laptop
Alias: /blog/2008/04/suspending-ram-debian-laptop
Lang: en
---

I am tracking Debian sid on my Thinkpad laptop, a few months ago it started to use *pm-utils* and broke suspending to RAM (sleep) functionality. Basically, the machine would go to sleep then immediately resume.  
It turned out that this problem can be easily fixed by creating a file */etc/pm/config.d/local*, and put in a line

SUSPEND\_MODULES="e1000"

The reason is that *pm-utils* by default does not unload Ethernet card module *e1000*, so the machine would be waken up by Ethernet card activities.
