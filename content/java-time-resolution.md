---
Status: published
Title: Java time resolution
Date: 2008-02-09 20:21
Author: Huahai
Category: notebook
Tags: Programming, Java, Vim
Slug: java-time-resolution
Alias: /blog/2008/02/java-time-resolution
Lang: en
---

I am writing a Java program to run psychology experiments. Since this is a generic program that may be configured for running some reaction time (RT) experiments, I am worried about the time resolution of Java. It turns out that I don't need to worry too much, except on Windows. 

On Linux, one millisecond time resolution can be consistently achieved using either *System.currentTimeMillis()* or *System.nanoTime()* call. 

On Windows, the former call can only get resolution on the order of ten millisecond, and the later one can get one millisecond most of the times, but can be far worse some times. You can download [this code](https://www.simongbrown.com/blog/2007/08/20/millisecond_accuracy_in_java.html) to test it out on your own system.

BTW, this test code apparently was edited on Windows, whose text files end each line with an extra character. In \*nix, it shows up as ^M. To remove them, use *:%s/^v^m//g* in vim, where ^v (control-v) is a control character (SYN).
