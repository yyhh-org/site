---
Title: Set mailto handler in Firefox
Date: 2007-11-16 22:25
Author: Huahai
Category: notebook
Tags: Firefox, Linux
Slug: set-mailto-handler-in-firefox
Alias: /blog/2007/11/set-mailto-handler-firefox
Lang: en
---

In order to click "mailto:" links on Web pages to launch an email program, Firefox (or Iceweasel on Debian) needs to be told which email program to use. 

To do this, type "about:config" in Firefox's address bar, type in "mailto" in filter, look if "network.protocol-handler.external.mailto" preference has value "true". By default, it's true. If not, set it to be true. Then check if "network-protocol-handler.app.mailto" exists or not. By default it's not. We need to create one: right click, select "New"-&gt;"String", then type in "network-protocol-handler-app.mailto", then type in the path name of your email program. In my case, it's "/usr/bin/kmail". That's it, Firefox should now be able to launch the email program when a "mailto:" link is clicked.
