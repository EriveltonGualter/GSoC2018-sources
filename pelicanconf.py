#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import join, expanduser

AUTHOR = u'Erivelton Gualter'
SITENAME = u"Erivelton's GSoC 2018"
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITESUBTITLE = 'PhD Student at Cleveland State University'
SITEURL = ''
#https://eriveltongualter.github.io/GSoC2018/index.html

PATH = 'content'
STATIC_PATHS = ['pdfs']

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# PYGMENTS_STYLE = 'igor'

#PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

LOAD_CONTENT_CACHE = False

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
#HOME_HIDE_TAGS = True

MENUITEMS = [('About', '/pages/about.html'),
	     ("Blog", "/blog.html"),]

PLUGIN_PATHS = [join(expanduser("~"), 'src', 'pelican-plugins'), "plugins"]
PLUGINS = ['pelican_youtube']

DISQUS_SITENAME = 'https-eriveltongualter-github-io-gsoc2018'

DEFAULT_METADATA = {'yeah': 'it is'}

COPYRIGHT_YEAR = 2018

DEFAULT_PAGINATION = 10

#THEME = 'Flex'
THEME = u'theme'
DIRECT_TEMPLATES = (('tag', 'category', 'blog'))
PAGINATED_DIRECT_TEMPLATES = (('index', 'blog', 'tag', 'category'))
# TEMPLATE_PAGES = {'home.html': 'index.html'}
PROFILE_IMAGE_URL = u'http://www.gravatar.com/avatar/85bba1ca66eb909a289448a90e88f53a?s=200'
TOP_IMAGE_URL = 'theme/images/gsococtave.png'

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

# Uncomment following line if you want document-relative URLs when developing\
RELATIVE_URLS = True
