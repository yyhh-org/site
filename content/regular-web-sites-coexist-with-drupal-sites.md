---
Status: published
Title: Regular Web sites coexist with Drupal sites
Date: 2007-11-16 01:31
Author: Huahai
Category: notebook
Tags: Drupal
Slug: regular-web-sites-coexist-with-drupal-sites
Alias: /blog/2007/11/regular-web-sites-coexist-drupal-sites
Lang: en
---

This site is primarily powered by Drupal, i.e. it is a PHP site. However, we have a few Web directories that serves regular HTML pages. Since I installed Drupal in document root, access to these directories becomes an issue. 

The main problem is that directory index file resolution is broken, because Drupal changed the default directory index file from *index.html* to *index.php*. So a Web request to these regular HTML directories results in an error. What's more, this error is very misleading, instead of saying "404 Page not found", it says "403 Access denied". But in fact, these pages are still accessible if full URL with .html suffix are given, it's only that index.php is not there.

To fix this, per-directory *.htaccess* file needs to be created for these directories. In my case, *.htaccess* were already created for these directories, but I couldn't edit them, because they were created automatically by my hosting company's tool, which required root privilege to change. So I had to disable access control on these directories to remove these .htaccess files. Then, I created my own .htaccess files. In addition to authentication directives, the critical change was to add a line:

  `DirectoryIndex index.html`

Now the default index file for these directories are changed back to *index.html*. Problem solved.
