Title: kmail hangs due to missing loopback interface
Date: 2007-11-22 01:50
Author: Huahai
Category: notebook
Tags: Linux
Slug: kmail-hangs-due-to-missing-loopback-interface
Alias: /blog/2007/11/kmail-hangs-due-missing-loopback-interface
Lang: en

My */etc/network/interfaces* got deleted when I removed *mepis-network* package. Everything was fine, except that kmail would hang since IP address 127.0.0.1 doesn't exist. It took me half an hour to figure it out. Had to create the file with these lines in it:

    :::cfg
    auto lo  
    iface lo inet loopback

Now things went back to normal.
