Title: Configure Jenkins to use FreeIPA LDAP Security Realm
Date: 2017-12-08 00:02
Author: Huahai
Category: notebook
Tags: SysAdmin, Jenkins, LDAP, FreeIPA
Slug: configure-jenkins-to-use-freeipa-ldap-security-realm
Alias: /blog/2017/12/configure-jenkins-use-freeipa-ldap-security-realm
Lang: en

The point of setting up freeIPA for an intranet is to enable single-sign-on (SSO) for all the internal services that requires authentication and authorization. [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol), originated from my *alma mater* University of Michigan, is one of the most widely accepted solutions to the problem. freeIPA can serve as a LDAP authentication and authorization provider to integrate with most of today's reputable server software. Jenkins is no exception.

There are plenty of guide of integrating OpenLDAP or other LDAP providers with Jenkins. However, there are not many guides on the particulars of integrating freeIPA with Jenkins. Here's how I got it to work.

Prepare freeIPA server
----------------------

First, we need to create an LDAP account for Jenkins to access the LDAP data. Create a file, e.g <span style="font-family:Courier New,Courier,monospace;">jenkins.ldif</span>

    dn: uid=jenkins,cn=sysaccounts,cn=etc,dc=example,dc=com
    changetype: add
    objectclass: account
    objectclass: simplesecurityobject
    uid: jenkins
    userPassword: secret
    passwordExpirationTime: 20380119031407Z
    nsIdleTimeout: 0

Now use it:

    $ ldapmodify -h ipa.example.com -p 389 -x -D "cn=Directory Manager" -W -f jenkins.ldif

Configure Jenkins
-----------------

Go to *Manage Jenkins* -&gt; *Configure Global Security* -&gt; *Security Realm*, and choose *LDAP*, and set the following:

    Server: ldap://ipa.example.com
    root DN: dc=example,dc=com
    User search base: cn=users,cn=accounts
    User search filter: uid={0}
    Group search base:
    Group search filter:
    Group membership: Search for LDAP groups containing user
        Group membership filter: (| (member={0}) (uniqueMember={0}) (memberUid={1}))
    Manager DN: uid=jenkins,cn=sysaccounts,cn=etc,dc=example,dc=com
    Manager Password: secret

Then click on *Test LDAP settings *and try login with an account, if results are all green, authentication is configured. Otherwise, try tweak the settings. 

Now on to authorization, pick any one of the strategies. For testing, pick *Anyone can do anything*, so we will not be locked out. Once tested, I chose *Matrix-based security*, which give fine controls. 

Once saved, one has to login to Jenkins with the SSO account of freeIPA, but that's the point, isn't it. 

Caution
-------

Once freeIPA is setup, it takes over the SSH sever and <span style="font-family:Courier New,Courier,monospace;">known\_hosts </span>file will not be updated in the account's <span style="font-family:Courier New,Courier,monospace;">.ssh</span> directory. Instead,  <span style="font-family:Courier New,Courier,monospace;">/var/lib/sss/pubconf/known\_hosts</span> is updated when ssh into another machine. This creates a bit of problem for setting up SSH based Jenkins slave when using <span style="font-family:Arial,Helvetica,sans-serif;">*Known host file Verification Strategy*</span>. A simple solution is to just copy the relevant host entry over. 
