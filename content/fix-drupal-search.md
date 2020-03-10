---
Title: Fix Drupal Search
Date: 2011-07-10 19:18
Author: Huahai
Category: notebook
Tags: SysAdmin, Drupal
Slug: fix-drupal-search
Alias: /blog/2011/07/fix-drupal-search
Lang: en
---

Today I tried to search "clojure" using the search box at the top right corner, but could not find anything. I know I wrote a few posts on Clojure recently, so there must be something wrong with the search functionality here. This is a Drupal site, and this should be an easy fix. Indeed, I quickly figured out the problem and solved it.Here is what Idid.

After I login to the administrative interface, I saw lots of cron related errors at the **/admin/logs/watchdog** page: "*Cron has been running for more than an hour and is most likely stuck.*" A google search suggests that this is a common problem. One of the possible reasons is that there are too many things for cron to do so that it cannot finish them within the time limit or it runs out of the memory. The solution is to reduce the amount of work a cron job has to do. Since the indexing of the content on this site is done with a cron job, I checked the indexing setting at **/admin/settings/search** page. Sure enough, the option **Items to index per cron run:** was set at 100, so I changed it to 10 instead.

I then tried to manually run cron job at **/admin/logs/status** page, but it didn't work. It turned out that it is necessary to clear the cron related variables in the MySQL database Drupal uses. To do that, I logined into my hosting company's *phpmyadmin* interface, searched for "**cron\_last**" and "**cron\_semaphore**". There was no "cron\_semaphore", but there was a "cron\_last" entry, so I deleted it. Manually ran cron again, now it said "*Cron ran successfully*". After several manual runs to get the indexing status to be 100% done, now I can do a search on "clojure", and get the posts to show up. Nice.
