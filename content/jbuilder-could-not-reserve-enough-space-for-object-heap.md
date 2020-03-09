Title: JBuilder "could not reserve enough space for object heap"
Date: 2005-01-10 05:00
Author: Huahai
Category: notebook
Tags: Programming, Java
Slug: jbuilder-could-not-reserve-enough-space-for-object-heap
Alias: /blog/2005/01/jbuilder-could-not-reserve-enough-space-object-heap
Lang: en

I have been using Borland programming environment since 1994, beginning with its Turbo C 2.0, then Borland C++, and now JBuilder. This company has always produced programmer friendly products. Comparing with other products, Borland's offering are always the most natural, and the easiest to get the job done. At least to me.  

Well, I mostly do Java programming these days. I have used all sorts of Java IDEs over the years. VisualCafe, VisualAge, NetBean, Eclipse, and so on. At the end, I still decided to settle on the tried -and-true Borland product: JBuilder.  

For my personal projects, I need a free IDE. JBuilder now offer a free downloadable version called JBuilder 2005 Foundation. I have been very pleased with it.  

Today, I decide to install it on my work machine, a Dell OptiPlex GX270, Pentium 4 CPU 3.00GHz with 1GB memory, running WindowXP. After download and installation, when I clicked on the JBuilder icon, a splash screen showed up and immediately disappeared, but nothing else happened.  

To figure out why, I opened up Windows command line, and ran JBuilder.exe, the error messages readed: 

>Error occurred during initialization of VM  
>Could not reserve enough space for object heap  

Okay, it must be a Java Virtual Machine heap size issue, the max size is too small. I quickly found out that I can edit jubilder.config file in the JBuilder bin directory to fix it. Change "vmmemmax 75%" to "vmmemmax 256M", save the file, and relaunch JBuilder. Everything works now.  

I've installed JBuilder on many other machines and encountered no such problem before. The reason for the problem on this machine, I guess, is somehow the JVM bundled with JBuilder miscalculated the maximum heap size from this 75% due to large memory of this machine (1GB). Changing it to a fixed size such as 256M avoided this calculation.
