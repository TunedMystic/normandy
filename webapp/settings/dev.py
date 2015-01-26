"""
Django development settings.
"""
#from __future__ import absolute_import

from base import *

import os

# --- Debug Settings ---
DEBUG = TEMPLATE_DEBUG = True
# --- /Debug Settings ---


# Django-Debug-Toolbar Settings

show_toolbar = lambda x: True

INSTALLED_APPS += ("debug_toolbar",)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_CONFIG = {
  'SHOW_TOOLBAR_CALLBACK': 'webapp.settings.dev.show_toolbar',
}