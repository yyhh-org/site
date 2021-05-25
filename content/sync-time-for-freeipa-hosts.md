---
Status: published
Lang: en
Title: Sync time for FreeIPA hosts
Date: 2021-04-08T07:41:14.349Z
Author: Huahai
Category: notebook
Tags: FreeIPA
---
Recently, I upgraded the FreeIPA server for my network to the latest version (4.8.10). Some strange things related to authentication started to happen with some services on my network. 

For our Web site, netlify gotrue is used to enable users to login using SAML Single Sign-On. This started to fail due to this error:

> SAML response has invalid time

For our discourse based forum, users started to experience failure to login using Google Single Sign-On. Again, it is time related:

> Unable to verify authorization token due to server clock differences. Please try again.

So I check the time on the servers, they all have a few seconds differences from each other.

All my nodes use chronyd to manage NTP service. When run 
```bash
chronyc sources -v
```
I found that all of the NTP client show something like this:
```bash
210 Number of sources = 1

  .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
 / .- Source state '*' = current synced, '+' = combined , '-' = not combined,
| /   '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^? ipa.example.com         0   8     0     -     +0ns[   +0ns] +/-    0ns
```
It means that the NTP server is not reachable. No wonder the times are out of sync.

So I checked on my IPA server, it turns out that the new version of FreeIPA server default to disable the NTP server and does not allow external NTP clients to access. The NTP port `123` is not open:
```bash
ss -lnp | grep "123"
``` 
This shows nothing.

To fix, edit `/etc/chrony/chrony.conf`, and add 
```
allow all

local stratum 10
```
Then `systemctl restart chronyd` to restart the server. 

On the client nodes, do the same, now the time should be synced.

```bash
210 Number of sources = 1

  .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
 / .- Source state '*' = current synced, '+' = combined , '-' = not combined,
| /   '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^* ipa.example.com         4   7   377    73   +360us[ +447us] +/-   28ms
```

All those pesky authentication problems went away.