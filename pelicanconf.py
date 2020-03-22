#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'dplus members'
SITENAME = 'dplus blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME = 'themes/bootstrap2'
# OUTPUT_PATH = 'output'
# PATH = 'content'

# # Custom Home page
# DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
# # PAGINATED_DIRECT_TEMPLATES = (('blog',))
# TEMPLATE_PAGES = {'home.html': 'index.html',}

# ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'