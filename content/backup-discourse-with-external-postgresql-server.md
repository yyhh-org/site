Title: Backup Discourse with External PostgreSQL Server
Date: 2018-01-21 05:58
Author: Huahai
Category: notebook
Tags: SysAdmin, Discourse, PostgreSQL
Slug: backup-discourse-with-external-postgresql-server
Alias: /blog/2018/01/backup-discourse-external-postgresql-server
Lang: en

[Discourse](https://www.discourse.org/) is a modern forum software that is quite popular in the technology circle. One can install a Discourse server easily with the recommended method of using docker. All the services needed by the Discourse server, e.g. Postgresql and Redis, will be running inside a docker container, which is fine for a small installation. However, if one has already an external Postgresql server running, e.g. on AWS RDS, and would like to use that instead, Discourse may have trouble doing backups, and you may receive an email from Discourse:

> [2018-01-21 03:39:44] pg_dump: server version: 9.6.5; pg_dump version: 9.5.10
>
> [2018-01-21 03:39:44] pg_dump: aborting because of server version mismatch
>
> [2018-01-21 03:39:44] EXCEPTION: pg_dump failed

 

The main problem is that the Postgresql client in Discourse docker image is old, currently at version 9.5, whereas most of the world has moved on to version 9.6, and some even to version 10. 

The Discourse people are not very helpful on their forum regarding this issue. So here's a solution:

We need to update the Postgresql version in the Discourse docker container to whatever version your external Postgresql server is. Fortunately, it is fairly simple. First, get into the running container:

    :::bash
    sudo ./launcher enter app

Then update postgresql to the version you want, e.g.

    :::bash
    apt-get install postgresql-9.6

Now link pg_dump to the right version:

    :::bash
    ln -s /usr/lib/postgresql/9.6/bin/pg_dump /usr/bin/pg_dump

After this, you should be able to perform backup successfully in the UI.  
