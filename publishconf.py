#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://yyhh.org'
RELATIVE_URLS = False

FEED_ALL_ATOM = '/feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "yyhh-org"
GOOGLE_ANALYTICS = "UA-110381421-1"

ARTICLE_URL = '/blog/{date:%Y}/{date:%m}/{slug}'
ARTICLE_LANG_URL = '/{lang}/blog/{date:%Y}/{date:%m}/{slug}'

PAGE_URL = '/{slug}'
PAGE_LANG_URL = '/{lang}/{slug}'
