---
Status: published
Lang: en
Title: Fix FreeIPA httpd Let's Encrypt Certificate Update
Date: 2021-01-01T22:58:21.498Z
Author: Huahai
Category: notebook
Tags: FreeIPA,letsencrypt
---
For a public facing Web interface of FreeIPA server, it is desirable to use a 3rd party SSL certificate issued by a commonly accepted certificate authority, rather than using the server's own. [Let's Encrypt](https://letsencrypt.org/) provides free SSL certificate for this purpose.

To use Letsencrypt certificate with FreeIPA, [this script](https://github.com/freeipa/freeipa-letsencrypt) does a good job, and I have been using this for several years. 

## Problem

When the letsencrypt certificate was renewed last month, a problem occurred. The Apache httpd server used by FreeIPA could not start. The error in `/var/log/httpd/error_log` says:

> SSL Library Error: -8179 Certificate is signed by an unknown issuer

The next line says:

> Unable to verify certificate 'Server-Cert'. Add "NSSEnforceValidCerts off" to nss.conf so the server can start until the problem can be resolved.

So I did just that. Now the httpd server could start, and the Web UI did show up. However, one could not login, and the UI showed an "unknown error" message.

The error log says:

>  ipa: INFO: 401 Unauthorized: HTTPSConnectionPool(host='ipa.example.com', port=443): Max retries exceeded with url: /ipa/session/cookie (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:866)'),))

and 

>SSL Library Error: -12195 Peer does not recognize and trust the CA that issued your certificate

That's a bit frustrating. 

What's worse, in my attempt to reran the "renew-le.sh" script to see what's going on, I ran into the rate limit of letsencrypt service, which only allows 5 renewals per week. There's no way to reset that and I had to wait for a week.

## Fix

Today, a week has past, and I finally fixed the problem, after almost half a day.

It turned out that Let's Encrypt has been updating their Root and Intermediate certificates.  See details [here](https://letsencrypt.org/certificates/).

The old root certificate, `DSTRootCAX3.pem` is being phased out. In the past, I have been getting certificate from `X3` under it. However, the new certificate that I got is from `R3` under the new root `isrgrootx1.pem`. 

What's worse is that this new certificate was still issued with old root. What's missing, is an intermediate certificate that crossed signed with this old root, `lets-encrypt-r3-cross-signed.pem`. Without this, the certificate cannot be verified, hence the error.

So the solution, is to download https://letsencrypt.org/certs/lets-encrypt-r3-cross-signed.pem, then install it:

```bash
wget https://letsencrypt.org/certs/lets-encrypt-r3-cross-signed.pem

ipa-cacert-manage install lets-encrypt-r3-cross-signed.pem -n letsencryptr3-cross -t C,,
``` 
After this, if you attempt to run `ipa-certupdate`, it will fail:

> ipapython.admintool: DEBUG: The ipa-certupdate command failed, exception: NetworkError: cannot connect to 'https://ipa.example.com/ipa/json': [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:877)

> ipapython.admintool: ERROR: cannot connect to 'https://ipa.example.com/ipa/json': [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:877)

> ipapython.admintool: ERROR: The ipa-certupdate command failed.

It's like catch 22, because your httpd SSL certificate cannot be verified, you cannot update your ipa certificates, because it requires connecting to your httpd server over SSL, but it is already failed due to lack of proper certificate. What a stupid design!

Anyhow, I finally figured out a way around this, which is to manually edit `/etc/ipa/ca.cert`, and append all the certificates needed for the full chain: DSTRootCAX3.pem -> lets-encrypt-r3-cross-signed.pem -> cert.pem that was issued by letsencrypt, one after another. 

Restart server. Now `ipa-certupdate` is successful! All is well. 

## Some useful commands

In the process of figuring this out, I found a few commands that could be useful in the future to diagnose similar problems. 

To figure out what certificates FreeIPA knows about:
```
ldapsearch -Y GSSAPI -Q -b  cn=certificates,cn=ipa,cn=etc,dc=example,dc=com
```

To see what certificate httpd knows about:
```
certutil -L -d /etc/httpd/alias/
```
To install a certificate to httpd with name "Server-Cert":
```
certutil -A -d /etc/httpd/alias/ -n Server-Cert -t u,u,u -a -i file.pem
```

To test SSL connection:
```
openssl s_client -showcerts -verify 5 -connect ipa.example.com:443
```
