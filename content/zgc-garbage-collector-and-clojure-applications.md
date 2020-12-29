---
Status: published
Lang: en
Title: ZGC garbage collector and Clojure applications
Date: 2020-12-29T22:20:27.037Z
Author: Huahai
Category: notebook
Tags: JVM,Linux,Clojure
---
The main product of my startup is written in Clojure, a language that puts enormous pressure on the memory garbage collector due to the pervasive use of immutable data structures. The new Z garbage collector on JVM has been a blessing for us, as it has largely solved our memory problems. However, there are a few points that one needs to pay attention.

1. Large pages

We followed the suggestion on the [ZGC page](https://wiki.openjdk.java.net/display/zgc/Main#Main-EnablingLargePagesOnLinux) to enable large pages. 

Here is the easiest way to enable large page on Debian Linux: add "hugepages=9216" to `GRUB_CMDLINE_LINUX_DEFAUT` line in the `/etc/default/grub` file, issue `update-grub` as root, then reboot. This creates 9216 huge pages that are 2MB each (default), totaling 18GB.  In the JVM startup options, add `-XX:+UseLargePages` to enable large pages in JVM.

The ZGC page says "Configuring ZGC to use large pages will generally yield better performance (in terms of throughput, latency and start up time) and comes with no real disadvantage". Unfortunately, that is not always true.

As mentioned, our Clojure application puts a lot of pressure on GC. After the application has been up for a few days and after heavy loads, it will become extremely slow, resulting in customer complaints. We had to restart the application when that happened.

Disabling large pages (reverse the above steps) removed the problem. 

It appears that the culprit is memory fragmentation. As described [here](https://www.oracle.com/java/technologies/javase/largememory-pages.html), "for a system that has been up for a long time, excessive fragmentation can make it impossible to reserve enough large page memory." 

2. Number of Concurrent GC Threads

Since a Clojure application allocates tons of temporary objects then discards them, the garbage collector has more work to do. JVM's default setting of `-XX:ConcGCThreads` tends to be lower than necessary for a Clojure application under load. For example, by default, ZGC collector will only use one concurrent CG thread on a four core machine, which is definitely not enough. Setting the number to be two seems to be the minimum. I set it to three on our 8 core production servers. It seems to work well. 