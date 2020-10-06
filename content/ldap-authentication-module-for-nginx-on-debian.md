---
Status: published
Lang: en
Title: LDAP Authentication Module for Nginx on Debian
Date: 2020-10-04T23:33:54.502Z
Author: Huahai
Category: notebook
Tags: LDAP, Nginx, Debian
---
To control access to various internal Web sites of a company, a simple method is to enable LDAP authentication on the Web server, so that the company directory can be brought to bear and there is no need to create individual accounts for employees on different systems.

Nginx is one of the most popular free Web servers, it has a lot of built-in modules. Unfortunately, LDAP is not one of them, so we have to compile from the source. 

Here are the steps to build a nginx Debian package from source with LDAP module enabled, on Debian 10 buster. While at it, we will also add a nginx virtual host traffic status module. 

First install necessary tools:

```bash
sudo apt install dpkg-dev devscripts
```
Now get the source and dependency of nginx
```bash
sudo apt source nginx
sudo apt build-dep nginx
```
It is important to get the LDAP development library, as well as a few necessary libraries.

```bash
sudo apt install libldap2-dev libssl-dev libpcre3-dev
```


Clone `nginx-auth-ldap` and `nginx-module-vts` source code that we plan to compile into the nginx binary.
```bash
git clone https://github.com/kvspb/nginx-auth-ldap.git
git clone https://github.com/vozlt/nginx-module-vts.git
```

The part we need to change in the nginx source tree is the Debian rules, which govern how a Debian package is build.  Goes into the `debian` directory of the nginx source folder, and edit the `rules` file:
```bash
cd nginx-1.14.2/debian
vi rules
```
Add two lines to the end of `common_configure_flags`
```
   ... \
   --add-module=<path to>/nginx-auth-ldap \
   --add-module=<path to>/nginx-module-vts
```
Now goes back and build.
```bash
cd ..
debuild -b -uc -us
```
This may take a while. If the build is successful, the parent directory will now contains a bunch of .deb files and these can be installed with `dpkg -i`. First install nginx-common_1.14.2-*.deb, then libnginx-mod-*.deb, finally, nginx-light, full, or extras.  
