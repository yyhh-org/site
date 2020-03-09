Title: Annoying sun.io.MalformedInputException when moving Java program from Windows to Linux
Date: 2007-11-06 20:31
Author: Yunyao
Category: notebook
Tags: Programming, Java
Slug: annoying-suniomalformedinputexception-when-moving-java-program-from-windows-to-linux
Alias: /blog/2007/11/annoying-sun-io-malformedinputexception-when-moving-java-program-windows-linux
Lang: en

These day I write Java programs on my local machine and then move them to a Linux server to run experiments. This routine works fine so far. However, when I ran one of the progams, which involves coping one file from one directory to another, I kept on the following error message:

>sun.io.MalformedInputException  
>at sun.io.ByteToCharUTF8.convert(ByteToCharUTF8.java)  
>at java.io.InputStreamReader.convertInto(InputStreamReader.java:127)  
>at java.io.InputStreamReader.fill(InputStreamReader.java:176)  
>at java.io.InputStreamReader.read(InputStreamReader.java:256)  
>at java.io.BufferedReader.fill(BufferedReader.java:158)  
>at java.io.BufferedReader.read1(BufferedReader.java:206)  
>at java.io.BufferedReader.read(BufferedReader.java:280)

First, I though it was because of the file format problem, since all the files to be moved were created on my local Windows machine. So I manually ran dos2unix command to all the files, but it didn't work. Then I tried to change my code so that it reads and write the files in UTF8 encoding. It still did not help. Finally, I found this post online ([http://www-128.ibm.com/developerworks/java/jdk/linux/142/runtimeguide.l…](http://www-128.ibm.com/developerworks/java/jdk/linux/142/runtimeguide.lnx.en.html)). Following its advice, I simply change LANG from *en\_US.UTF8* to *en\_US.* Problem solved!
