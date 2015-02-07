"""
Django development settings.
"""

from base import *

import os

# --- Debug Settings ---
DEBUG = TEMPLATE_DEBUG = True
# --- /Debug Settings ---


# --- Email Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# --- /Email Configuration ---


# --- Django-Debug-Toolbar Settings ---
show_toolbar = lambda x: True

INSTALLED_APPS += ("debug_toolbar",)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_CONFIG = {
  'SHOW_TOOLBAR_CALLBACK': 'webapp.settings.dev.show_toolbar',
}
# --- /Django-Debug-Toolbar Settings ---
