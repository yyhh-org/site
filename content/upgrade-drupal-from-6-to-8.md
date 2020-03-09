Title: Upgrade Drupal from 6 to 8
Date: 2017-11-21 23:46
Author: Huahai
Category: notebook
Tags: SysAdmin, Drupal
Slug: upgrade-drupal-from-6-to-8
Alias: /blog/2017/11/upgrade-drupal-6-8
Lang: en

Since [Drupal 6 is no longer supported](https://www.drupal.org/forum/general/news-and-announcements/2015-11-09/drupal-6-end-of-life-announcement), I upgraded this site to the lasted version of Drupal 8.4.2 by following [the guide](https://www.drupal.org/docs/8/upgrade/upgrading-from-drupal-6-or-7-to-drupal-8). As you can see, the upgrade mostly worked. However, there are a few points of caution as well as some unresolved problems.

As [before](http://test.yyhh.org/blog/2011/07/upgrade-drupal-almost-zero-down-time), I setup a test site in a sub-directory (h/drupal) of the main site (/h) and assigned a domain name to the test site. The test site use a new empty database. The idea is to keep the old site running, and migrate the data from the old to the new. 

This blog is on a hosted service that allows direct SSH access, so it made things a lot easier.** **[Drush](http://www.drush.org/en/master/) helped a lot. To get drush to work, I had to modify the drush bootstrap script to use php7.1-cli, because the hosting server had many versions of PHP installed, and the default one is not even a command line interpreter.  I then created a bash alias in ~/.bash\_profile for the drush script, so that I could run drush anywhere. 
    
    :::bash
    alias drush='/h/drupal/vendor/bin/drush --root=/h/drupal'

With drush, migration was easy, with only a few commands.

First initialized the database.

    :::bash
    drush si standard --db-url=mysql://username:pasword@new.mysql.server/newdb --root=/h/drupal --db-prefix=drupal_ --locale=en

Now we found out all the modules enabled on the old site, and enabled them on the new site. 

    :::bash
    drush en migrate_upgrade migrate_tools migrate_plus rules config_update libraries tracker views_bulk_operations taxonomy_menu tagadelic mollom better_formats statistics pathauto mathjax profile

Not all the old modules exist in Drupal 8 any more. Some of them are folded into core, and some simply disappeared. With above, we also enabled three modules needed for doing the migration.

First created the migrate configurations.

    :::bash
    drush migrate-upgrade --legacy-db-url=mysql://username:password@old.mysql.server/olddb --legacy-root=http://yyhh.org --configure-only

At this point, one could run individual migration one by one, or one could run them all, which I did:

    :::bash
    drush mi --all

Most of the migrations worked. Two migrations failed with errors: 

>   upgrade\_d6\_filter\_format

> "Missing filter plugin: filter\_null.                        \[error\]"

This error turned out not to be a problem. All one needed to do is to save the formats again at the UI: "/admin/config/content/formats". Otherwise, the content of the posts will not show due to missing filter "filter\_null". Saving the formats in the UI got ride of the errors.

>   upgrade\_d6\_taxonomy\_term\_translation

> "Drupal\\Core\\Database\\IntegrityConstraintViolationException: SQLSTATE\[23000\]: Integrity constraint violation: 1048 Column 'langcode' cannot be null:..."

Basically, all the taxonomy terms failed to translate due to missing language code. Since all my terms are in English, this was not a problem either.

Now the new site was up and running. The look of the site was of course horrible. I had to install a new theme and created a sub-theme. Then did all the work of creating views, blocks, and links with the UI. Now we have a functioning site. Cool!

A few cautions though:

-   Do not enable "taxonomy\_breadcrumb", otherwise the page will error out. I think it's because the migrated taxonomy terms miss some fields. I did not investigate further since I would not use it any more.
-   Do not enable "comment\_notify", the migration may error out. I did not investigate since there's no need to migrate this.
-   No need to enable "blog". The functionality of blog module could be easily reproduced by creating one's own views. The "blog" module does not work well with migrated posts any way.

An unsolved problem is that the "popular content" links are all out of whack due to the loss of all old statistics. This is a [known issue](https://www.drupal.org/node/2500521) that has not been resolved as of today. The fix, however, will be available in Drupal 8.5. So if the node counts are important to you, hold the migration until 8.5 is released on March 7, 2018.

Overall, the upgrade is a smooth experience, in the sense that source code modification was not necessary, nor was changing the database data. I am glad the Drupal is getting better and better.
