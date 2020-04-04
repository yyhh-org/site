---
Title: Firefox Hangs
Date: 2007-12-06 10:52
Author: Huahai
Category: notebook
Tags: Firefox
Slug: firefox-hangs
Alias: /blog/2007/12/firefox-hangs
Lang: en
---

Although Firefox is considered very safe and stable, it sometimes hangs. In the past, when it hung, my solution was to remove the whole *~/.mozilla/firefox* directory. It worked every time (reinstalling Firefox doesn't help). Of course, I would always backup my *bookmarks.html* and other files under the *chrome* sub-directory first. Then I had to reinstall the add-ons when I got a working firefox. It turned out I shouldn't have taken such a drastic action. According to [this firefox documentation](https://kb.mozillazine.org/Firefox_hangs), *sessionstore.js* files are often the culprit. Removing them usually works for me.
