---
Title: FreeIPA in AWS EC2
Date: 2017-12-07 23:34
Author: Huahai
Category: notebook
Tags: SysAdmin, AWS, DNS, FreeIPA
Slug: freeipa-in-aws-ec2
Alias: /blog/2017/12/freeipa-aws-ec2
Lang: en
---

FreeIPA is the open source version of RedHat's identity management solution, which nicely integrates several open sources services that are important for managing an intranet: 389 LDAP Directory Server, MIT Kerboros, NTP, DNS, SSSD and others. 

Most of my servers are virtual machines in AWS EC2. To manage such a cloud based intranet using freeIPA, some additional configuration is necessary. Here's how I got it to work.

DNS
---

The main problem of enabling freeIPA in EC2, is that every machine in EC2 has at least two kinds of of IP addresses. One is internal to the VPC only, e.g. the default VPC use IP addresses starting from <span style="font-family:Courier New,Courier,monospace;">172.31.\*.\*</span>; Another kinds of IP addresses are public IP addresses, which are different from the internal ones. A default install of freeIPA server and clients in EC2 will not work due to this dual IP addresses.

To install freeIPA, we first need to configure individual <span style="color:null;">hosts' </span><span style="color:#e74c3c;">/etc/hosts</span>, <span style="color:#e74c3c;">/etc/hostname</span> files, so they point to the full qualified DNS name of the hosts. After that, we are ready to add these names to DNS servers.

### Route53

We will bypass freeIPA's own DNS services, and use AWS Route53 DNS service. We need to setup three hosted zones for our network. One zone for the external IPs, one for internal IPs, and finally one for reverse lookup.

For internal and external hosted zones, in addition to the <span style="color:#e74c3c;">A</span> records that map DNS names to IPs, we also need to add <span style="color:#e74c3c;">TXT</span> and <span style="color:#e74c3c;">SRV</span> records that allow freeIPA to discover services. Eg. for the external zone: 

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_kerberos.example.com.</p></td><td><p>TXT</p></td><td><p>"EXAMPLE.COM"</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_kerberos-master._tcp.example.com.</p></td><td><p>SRV</p></td><td><p>0 100 88 ipa.example.com.</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_kerberos._tcp.example.com.</p></td><td><p>SRV</p></td><td><p>0 100 88 ipa.example.com.</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_kpasswd._tcp.example.com.</p></td><td><p>SRV</p></td><td><p>0 100 464 ipa.example.com.</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_ldap._tcp.example.com.</p></td><td><p>SRV</p></td><td><p>0 100 389 ipa.example.com.</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_kerberos-master._udp.example.com.</p></td><td><p>SRV</p></td><td><p>0 100 88 ipa.example.com.</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_kerberos._udp.example.com.</p></td><td><p>SRV</p></td><td><p>0 100 88 ipa.example.com.</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_kpasswd._udp.example.com.</p></td><td><p>SRV</p></td><td><p>0 100 464 ipa.example.com.</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>_ntp._udp.example.com.</p></td><td><p>SRV</p></td><td><p>0 100 123 ipa.example.com.</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

<table><tbody><tr class="odd"><td style="text-align: right;"><p>ipa.example.com.</p></td><td><p>A</p></td><td><p>99.99.99.99</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

 

Here we will install the freeIPA server on a machine with external IP <span style="font-family:Courier New,Courier,monospace;">99.99.99.99</span>, and the DNS name for the server is<span style="font-family:Courier New,Courier,monospace;"> ipa.example.com</span>.

Similar records need to be added the internal zone as well, just use the internal IP addresses.

Finally, the private reverse look up zone, named <span style="color:#e74c3c;"><span style="font-family:Courier New,Courier,monospace;">31.172.in-addr.arpa.</span>,</span> has records like these:

<table><tbody><tr class="odd"><td style="text-align: right;"><p>88.123.31.172.in-addr.arpa.</p></td><td><p><span style="color:#e74c3c;">PTR</span></p></td><td><p>ipa.example.com</p></td><td><p>-</p></td><td><p>-</p></td><td><p>300</p></td></tr></tbody></table>

Where <span style="font-family:Courier New,Courier,monospace;">172.31.123.88</span> is the internal IP address of the freeIPA server. 

We need to do these for all servers managed by freeIPA. It's a bit of work if there are not many machines. For large deployment, one may want to investigate automatized solution with AWS APIs.

### Test DNS

On a machine outside the VPC

    $ dig +short ipa.example.com

Should return the external IP of the machine.

Doing the same on an internal machine should return the internal IP of the machine.

Finally, test reverse lookup on an internal machine

    $ dig +short -x  172.31.123.88

Should return the DNS name of the machine.

FreeIPA Server Install
----------------------

I normally use Debian servers,  but there's currently no stable  freeIPA server available in Debian Stretch, so I installed a Fedora, which supports freeIPA natively.

Use a small EC2 instance that will be dedicated to running a freeIPA server.

    :::bash
    # yum install freeipa-server
    # ipa-server-install

And say "no" to DNS. The installation should be successful if all instructions are followed.

FreeIPA  Client
---------------

Since most of my machines are Debian, I had to install Debian freeIPA clients on them. Ubuntu Xenial universe repo has a version of freeIPA  client that is compatible with Debian Strech. So I installed them.

    :::bash
    # apt install freeipa-client
    # /etc/init.d/ntp stop
    # ipa-client-install

Notice that we must stop NTP daemon first if it's already running. Otherwise, the client installation will fail, because the freeIPA client expects to run its own NTP service that synchronizes with the freeIPA server. 

After a successful installation, the client is still not ready to use, because the Ubuntu installer configured <span style="color:#e74c3c;">/etc/sssd/sssd.conf</span> is currently broken: nss, pam,  and ssh needs to be added. Otherwise, the client cannot be connected to. A working example of <span style="color:#e74c3c;">/etc/sssd/sssd.conf</span> looks like this:

    [domain/example.com]

    cache_credentials = True
    krb5_store_password_if_offline = True
    ipa_domain = example.com
    id_provider = ipa
    auth_provider = ipa
    access_provider = ipa
    ipa_hostname = aclient.example.com
    chpass_provider = ipa
    ipa_server = _srv_, ipa.example.com
    ldap_tls_cacert = /etc/ipa/ca.crt
    [sssd]
    services = nss, sudo, pam, ssh

    domains = example.com
    [nss]
    homedir_substring = /home

    [pam]

    [sudo]

    [autofs]

    [ssh]

    [pac]

    [ifp]

    [secrets]

Restart sssd or simply reboot. Everything should work as expected.

    $ kinit admin
    $ ssh admin@ipa.example.com

Should login to the freeIPA server as admin user. 

    $ ssh admin@aclient.example.com

Should login to the client machine as admin user.

Congratulation, now you have single sign on (SSO) for your intranet in AWS EC2!

\[update: 10/23/208\]

Cross Cloud Intranet
--------------------

With minor modification, this same setup can be used to manage you Intranet with hosts spanning multiple cloud platforms!

For example, you can have some hosts reside on Google Cloud Platform (GCP) while the IPA server lives in AWS. To do that, the <span style="background-color:#e74c3c;">public</span> IP addresses of these ex-AWS hosts need to be entered in <span style="color:#e74c3c;">both</span> external and internal DNS realms in Route53. GCP nicely supports this setup because you can reserve as many static public IP addresses as you want in GCP.

For example, you can have a host on GCP with a public address 35.22.31.33, for which you assign a domain name "gcp1.example.com" in Route53. Then you run <span style="color:#e74c3c;">hostname gcp1.example.com</span> on this GCP host. After that, you should be able to install freeIPA client on it to enroll into your Intranet.

After install freeIPA client, another important modification, is to add the following directive in <span style="color:#e74c3c;">/etc/krb5.conf</span><span style="color:null;"> of all your ex-AWS hosts:</span>


    [libdefaults]
      ignore_acceptor_hostname = true

This directive tells Kerberos service of an accepting host to not verify its own hostname, because an ex-AWS host's attempt to discover its own hostname will yield a name that is different from the one you assigned in Route53. With this change, you should be able to access your ex-AWS hosts as if they are part of your Intranet. Your SSO should work on these ex-AWS hosts as well.
