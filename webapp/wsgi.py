"""
WSGI config for webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from getenv import env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{0}'.format(env('DJANGO_SETTINGS_MODULE')))

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

application = Cling(MediaCling(get_wsgi_application()))
