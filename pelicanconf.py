#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'yyhh.org'
SITENAME = 'yyhh.org'
SITESUBTITLE = 'Homepage of Yunyao and Huahai'
SITEURL = 'https://yyhh.org'

SITELOGO = 'images/yyhh.svg'
SITELOGO_SIZE = 52

READERS = {'html': None}

I18N_SUBSITES = {
    'zh': {
        'SITELOGO': '../images/yyhh.svg',
        'STATIC_PATHS': [
            '../images',
            '../extra'
        ],
        'BANNER': '../images/slide-image-1.jpg',
        'BANNER_SUBTITLE': '蕴瑶和华海的网上家园',
        'CUSTOM_CSS': '../static/css/custom.css',
        'LINKS': [
            ('标签', '/zh/tags.html'),
            ('档案', '/zh/archives.html'),
            ('English', '/')
        ]
    }
}

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

BANNER = 'images/slide-image-1.jpg'
BANNER_SUBTITLE = "Yunyao and Huahai's Online Home"

CUSTOM_CSS = 'static/css/custom.css'

TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}

STATIC_PATHS = [
    'images',
    'extra',
    'admin',
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/_headers': {'path': '_headers'},
}


PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = '{lang}/blog/{date:%Y}/{date:%m}/{slug}'
ARTICLE_LANG_SAVE_AS = '{lang}/blog/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{lang}/{slug}'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index..html'

# DISPLAY_ARCHIVE_ON_SIDEBAR = True
# DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_AUTHORS_ON_SIDEBAR = True

LINKS = [('Tags', '/tags.html'),
         ('Archive', '/archives.html'),
         ('中文','/zh/')]

# Social widget
# SOCIAL = (('twitter', 'https://twitter.com/yunyao_li'),
          # ('twitter', 'https://twitter.com/huahaiy'),)


DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-themes/pelican-bootstrap3'

BOOTSTRAP_THEME = 'readable'

SHOW_ARTICLE_AUTHOR = True
DISPLAY_SERIES_ON_SIDEBAR = True


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_alias', 'i18n_subsites', 'series', 'related_posts',
           'tipue_search', 'render_math', 'sitemap']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

SITEMAP = {'format': 'xml'}

PYGMENTS_STYLE = 'default'

IGNORE_FILES = ['.#*', '__pycache__']

CC_LICENSE = 'CC-BY-NC-SA'

SHARIFF = True
# SHARIFF_BACKEND_URL = 'https://yyhh.org/shariff'
SHARIFF_SERVICES = '[&quot;twitter&quot;,&quot;facebook&quot;,&quot;reddit&quot;,&quot;linkedin&quot;,&quot;pinterest&quot;]'
SHARIFF_BUTTON_STYLE = 'icon'
SHARIFF_LANG = 'en'
SHARIFF_ORIENTATION = 'horizontal'
SHARIFF_THEME = 'grey'
