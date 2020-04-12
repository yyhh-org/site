---
Status: published
Title: Screen Saver Option Disabled on Windows 7/XP
Date: 2012-08-01 17:07
Author: Yunyao
Category: notebook
Tags: Software, Windows
Slug: screen-saver-option-disabled-on-windows-7xp
Alias: /blog/2012/08/screen-saver-option-disabled-windows-7-xp
Lang: en
---

For unknown reason, my machines would suddenly disable their screen saver options (e.g. with the "on resume, display log on screen" check box grayed out). Whenever this happens, it would trigger the security alert and I will get a warning from the IT department to fix the issue.

I am tired of having to hunting down the answer every time and therefore I am recording it here.

The following method is what usually works for me.

1\. Go to "Start" type in "regedit"

2\. Go to

\[HKEY\_CURRENT\_USER\\Software\\Policies\\Microsoft\\Windows\\Control Panel\\Desktop\]

Delete the "ScreenSaverIsSecure" value.
