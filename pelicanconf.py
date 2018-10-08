#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kosuke Futamata'
SITENAME = "Kosuke Futamata's page"
SITETITLE = "Kosuke Futamata's page"
#SITEURL = 'matasuke.github.io'

THEME = './Flex'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Japanese Blog', 'http://matasuke.hatenablog.jp/'),
         ('Qiita', 'https://qiita.com/Matasuke_f'),
        )
# Social widget
SOCIAL = (('twitter', 'https://twitter.com/matasuke_f'),
          ('github', 'https://github.com/matasuke'),
          ('facebook', 'https://www.facebook.com/matasukef'),
          ('slideshare', 'https://www.slideshare.net/KosukeFutamata/presentations'),
          ('linkedin', 'https://www.linkedin.com/in/kosuke-futamata-862b68124/'),
        )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


SITETITLE = 'Kosuke Futamata'
SITESUBTITLE = 'Software Engineer'
SITELOGO = 'images/profile.jpg'
SITEDESCRIPTION = "This web site is about kosuke futamata's portfolio"
BROWSER_COLOR = '#333'
OG_LOCALE = 'ja_JP'
COPYRIGHT_NAME = 'Kosuke Futamata'
COPYRIGHT_YEAR = '2018'
#CC_LICENSE = ()
#MAIN_MENU = True
#MENUITEMS = (())
#FAVICON
GITHUB_CORNER_URL = 'https://github.com/matasuke'

SUMMARY_MAX_LENGTH = 10000

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ["render_math", "tipue_search", "tag_cloud", "related_posts"]
