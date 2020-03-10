---
Title: "Centralized authentication with LDAP + NFS + Samba (Part II: NFS)"
Date: 2005-01-17 05:00
Author: Huahai
Category: notebook
Tags: SysAdmin, Linux
Slug: centralized-authentication-with-ldap-nfs-samba-part-ii-nfs
Alias: /blog/2005/01/centralized-authentication-ldap-nfs-samba-part-ii-nfs
Sereis: ldap-nfs-samba
Lang: en
---

NFS (Network File System) is an old Unix technology that enables a machine to mount a remote file system. This is desirable for centralized authentication, as the user can access the same home directory no matter which machine he uses.

**Server**

Install NFS server:  

```
apt-get install nfs-kernel-server
```

Edit /etc/exports, put in lines such as

```
/home *.dept.school.edu(rw,no_subtree_check)
```

to export directories to allow machines on local network have access to /home and its subdirectories.

Start the server:

```
/etc/init.d/nfs-kernel-server start
```

If you have a personal firewall running on the machine, you will need to configure it so NFS traffic can be served from this machine. On MEPIS Linux, go to Guarddog->Protocol->Local->Network File System - Sun Microsystems, and check the box, apply; For client, goto the Internet zone, instead of Local zone, check the same box. Since NFS is highly vulunrable for exploitation, you should make sure your whole subnetwork is behind a firewall.

**Client**

We would like to automatically mount the NFS volume when a user is trying to access it. am-utils, an automounter, will do this. Get and install it:  
```
apt-get install am-utils  
```

* use NIS: no  
* use net map: yes  
* use passwd map: no

Edit /etc/am-utils/amd.conf,  
Uncomment nfs-proto = udp, for better performance  
Add two lines:

```
[/homes]  
map_name = /etc/am-utils/amd.homes
```

If user joe's home directory is on machine yoda, we can create a file amd.homes, which contains lines such as:

```
joe host!=yoda;type:=nfs;rhost:=yoda;rfs:=/home;sublink:=${key};opts:=rw,intr,nosuid,grpid 
host==yoda;type:=link;fs:=/home;sublink:=${key};opts:=rw,intr,nosuid,grpid
```

Copy this file to all your machines.

Create the mount point:

```
mkdir /homes
```

What this does, is to mount a user's home directory on the NFS server (/home/joe) to this NFS client machine, at /homes/joe, whenever /homes/joe is requested. Usually, it happens when user login. Of course, /homes/joe should be this user's default home directory.

```
ls /homes/joe
```

If everythings are working, you should be able to see the content of /home/joe on the NFS server.

One more thing, what if the user login to his/her NFS server itself? To avoid a potential problem, the automounter amd should be launched with option -r, so that it will inherent the local file system /home/joe, instead of attempting mount it as a NFS. To achieve this, edit /etc/init.d/am-utils:

append -r to the end of the line :

```
/etc/sbin/amd -F /etc/am-utils/amd.conf $dnsdomain $AMDARGS
```

to

```
/etc/sbin/amd -F /etc/am-utils/amd.conf $dnsdomain $AMDARGS -r
```

For some system, you may want to comment out this two lines so that amd can start:

```
echo "$0: please setup your domainname" 1>&2  
exit 1
```

Now restart amd:

```
/etc/init.d/am-utils restart
```

===============  
Debian package used  
===============  
Server:  
nfs-kernel-server 1:1.0.6-3.1  
-----------------------------  
Client:  
am-utils 6.0.9-3.1
