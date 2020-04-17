---
Status: published
Title: "Centralized authentication with LDAP + NFS + Samba (Part I: LDAP)"
Date: 2005-01-17 05:00
Author: Huahai
Category: notebook
Tags: SysAdmin, Linux
Slug: centralized-authentication-with-ldap-nfs-samba-part-i-ldap
Series: ldap-nfs-samba
Lang: en
---

Ok, what is centralized authentication? Why bother? Well, if each person in your home or organization uses her/his own computer only, no need for this. However, if you or your organization have a bunch of machines and people need to login to different machines at different times, you've got a problem. Do you want to setup an account for each person on each machine? What about people's files? People would like to have access to their files no matter where they login. For this kind of environment, centralized authentication is the way to go.

I am setting up a centralized authentication environment for a small work group, it consists of 7 or so Debian Linux boxes, 2 Sun Solaris boxes, and 5 Windows 2k/XP machines. Since the budget is tight, I will use all open source solution for this setup, namely, OpenLDAP, NFS and Samba.

The actual setup proved to be quite easy, but took us a few days to figure it out, mostly due to the scant documentation available. I hope this series of posts can help alleviate this problem. The first installment deals with seting up LDAP server and client on Debian Linux machines. Most of the steps assume you have root privilige.

**LDAP Server**

One Linux machine will be used as a dedicated LDAP server for the whole workgroup. It is a Pentium III 1GB with 256MB (an old IBM NetVista, manufactured around 2000), running SimplyMEPIS 2004-6.

Get and install OpenLDAP server (slapd): 

```
apt-get install slapd
```

* Enter your DNS domain name: dept.school.edu, this does not have to be a real domain name, just something makes sense.  
* Enter the name of your organization: whatever name you like for your organization (or your home)  
* Admin password: this is the root password for this LDAP directory, don't forget this  
* Allow LDAPv2 protocol: no, since this is a new environment, no backward compatibility needed

This will install and start the OpenLDAP server.

Now get some useful LDAP utilities: `apt-get install ldap-utils`

To start populate the LDAP directory, let's import some initial data. We can use migrationtools: 

```
apt-get install migration_tools
cd /usr/share/migrationtools
```

edit migrate_common.ph:

```
$DEFAULT_BASE = "dc=dept,dc=school,dc=edu" # use your own information here  
$IGNORE_UID_BELOW = 1000;  
$IGNORE_GID_BELOW = 100;

./migrate_base.pl > base.ldif  
./migrate_group.pl /etc/group > group.ldif  
./migrate_passwd.pl /etc/passwd > passwd.ldif
```

The migration scripts do not actually check the encryption methods used for password, and it simply use {crypt} for userPassword field. You will need to edit passwd.ldif, change {crypt} to {md5} if your system use md5 encryption, which is usually true.

Now let's use LDAP utilies to load these ldif (LDAP data interchange format) files into our server:

```
ldapadd -x -h localhost -W -D 'cn=admin,dc=dept,dc=school,dc=edu' -c -f base.ldif  
ldapadd -x -h localhost -W -D 'cn=admin,dc=dept,dc=school,dc=edu' -c -f group.ldif  
ldapadd -x -h localhost -W -D 'cn=admin,dc=dept,dc=school,dc=edu' -c -f passwd.ldif
```

Let's check if these are loaded in the LDAP directory:

```
ldapsearch -x -h localhost -b 'dc=hci,dc=albany,dc=edu'
```

There should be a lot of information being printed out, and they should just look like the content of those ldif files.

This pretty much finished the LDAP server setup. Finally, configure the firewall so LDAP port is open. Note that this LDAP server is NOT configured as a LDAP client, so oridnary LDAP users are not able to login to this machine. This enhances the security I think.

We now need to configure the client machines to use this LDAP server for authentication.

**LDAP Client**

This test client machine is a highend home grown graphics workstation, running the same SimplyMEPIS Linux as the LDAP server machine. We need to get ldap-utils and migrationtools for this client machine too, since there are some accounts on this machine need to be migrated to the LDAP server. We basically did the same thing as that on the server for the migration, only changed the host name from localhost to the name of the LDAP Server.

Now let's enable authentication with LDAP. Get the necessary packages first:

```
apt-get install libnss-ldap  
```
* LDAP server host address: enter the IP address of the LDAP server  
* distinguished name of the search base: dc=dept,dc=school,dc=edu  
* LDAP version to use: 1, version 3  
* database requires login: no, you don't have to login to browse the directory, better performance.  
* make configuration readable/writable by owner only: yes

Now edit /etc/nsswitch.conf, insert "ldap" in front of "compat" for passwd, group and shadow:

```
passwd: ldap compat  
group: ldap compat  
shadow: ldap compat
```

This way, system will check with LDAP directory first for user information.

If you have a user who does not have an account on this machine, but has an entry in LDAP directory, suppose this user's uid is 1005, a way of checking if nsswitch is working is:

```
touch /tmp/test  
chown 1005 /tmp/test  
ls -l /tmp/test
```

In the output, if the uid 1005 is replaced by the user name, nsswitch is working, or someting went wrong. The reason is that the system has to check with LDAP to know what user name this uid 1005 is mapped to, since this user does not exist on this machine at all.

```
apt-get install libpam-ldap  
```
* Make local root Database admin: no, since we don't want local machine's root to be equivent to the root of the whole network managed by the LDAP directory.  
* Database requires loggin in: no  
* Local crypt to use when changing password: 6. md5. We want the local machine encrypt the password first before sending it to the LDAP server for storage.

You may want to chmod 644 libnss-ldap.conf, so users other than root can also read the file.

```
cd /etc/pam.d
```

Edit common-account, common-auth and common-password, so they looks like this:

```
auth sufficient pam_ldap.so  
auth required pam_unix.so nullok_secure try_first_pass
```

Basically, this let PAM (Pluggable Authentication Modules) try to authenticate with LDAP first, if it fails, fall back to the local machine's accounts.

At this point, you should be able to login with LDAP. Again, the way to test is to login as a user that does NOT exist on this client machine, but exists in LDAP directory.

**sshd**

Login via SSH needs a bit more tweaks. Edit /etc/ssh/sshd_config

```
PasswordAuthentication no  
ChallengeresponseAuthentication yes  
PAMAuthenticationViaKbdInt yes  
UsePAM yes
```

**nscd**

To speed things up, it is better to install nscd (name service cache daemon) package:  

```
apt-get install nscd
```

This finishes this part of the guide.  

=====================  
Debian packages used:  
=====================  
Server: SimplyMEPIS 2004-6  
slapd 2.1.30-3  
ldap-utils 2.1.30-3  
migrationtools 46-1  
------------------------------  
Client: SimplyMEPIS 2004-6  
ldap-utils 2.1.30-3  
migrationtools 46-1  
libnss-ldap 220-1  
libpam-ldap 169-1  
nscd 2.3.2.ds1-20  
ssh 1:3.8.1p1-8
