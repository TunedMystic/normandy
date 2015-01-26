"""
Django production settings.
"""
#from __future__ import absolute_import

from base import *

import os

# Debug Settings

DEBUG = TEMPLATE_DEBUG = False

# --- Host Configuration
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['.herokuapp.com', '.nitrousbox.com', 'localhost', '127.0.0.1']
# --- /Host Configuration