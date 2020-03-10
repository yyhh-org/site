---
Title: Migrate DokuWiki to another server
Date: 2018-10-20 04:46
Author: Huahai
Category: notebook
Tags: SysAdmin, DokuWiki
Slug: migrate-dokuwiki-to-another-server
Alias: /blog/2018/10/migrate-dokuwiki-another-server
Lang: en
---

[DokuWiki](https://www.dokuwiki.org/dokuwiki) is one of the most easy-to-use open source Wiki software. It is a very good internal documentation tool for small or medium sized organizations.

Comparing with using Google Docs for the same purpose, one advantage of using a Wiki is that it is more searchable and navigable. In addition, Wiki software is often very extensible. In the case of DokuWiki, there are hundreds of plugins that can help with many aspects of doing documentation work. In my company, we not only use DokuWiki to keep technical documentations up to date , but also used it for administrative chores, such as filling out forms, keeping track of vacations, and so on.

On the technical side, DokuWiki is a PHP application that does not reply on a database backend. All the materials are in plain text files. So one of the claimed advantages is that it is easy to migrate a DokuWiki installation from one host to another, because you could simply zip up the file directory, move to another host and unzip. As it happened, as part of my company's migration from AWS to Google Cloud, I had a chance to test this claim for real. 

It turned out it was not as straightforward as [DokuWiki claims](https://www.dokuwiki.org/faq:servermove). Although in the end, it was really a very simple migration, after I figured out the proper steps.

At first, I did what the document suggested: simply moved the files over to another host, but the site failed to load. Pouring over the error messages in the logs, I realized that some of the installed plugins could not compile, but somehow they did not break the old site. After removing these broken plugins on the old site, I decided not to simply zipping up the file directory again. Instead, I did the following:

1\. Use a plugin called "Backup Tool" to zip up only essential configs and settings.

2\. Download the latest stable version of DokuWiki software bundle, unzip on the new host.

3\. Unzip the backup bundle created in step 1 **over** the fresh directory of DokuWiki created in step 2

4\. Load the site, success!

5\. However, the site reports some missing directories, such as media\_attic and media\_meta. Simply copying them from the old host to the new host fixes the problems.

6\. Mission accomplished!

I think the main problem with the "copy files over" approach is that many caches on the old site tend to mess things up. A fresh new start is a surer way to migrate.

 
