"""
Django production settings.
"""

from base import *
import os
from urlparse import urlparse
from getenv import env


# --- Debug Settings ---
DEBUG = TEMPLATE_DEBUG = False
# --- /Debug Settings ---


# --- Host Configuration
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['.herokuapp.com', '.nitrousbox.com', 'localhost', '127.0.0.1']
# --- /Host Configuration


# --- Email Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST', 'smtp.gmail.com')

# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = env('EMAIL_PORT', 587)

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = env('EMAIL_HOST_USER', 'your_email@example.com')

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')

# https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True
# --- /Email Configuration ---


# --- Database Configuration ---
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
  "default": dj_database_url.config(default = "postgres://action:@127.0.0.1:5432/webapp")
}
# --- /Database Configuration ---


# --- Cache Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
cacheUrl = urlparse(env("REDISTOGO_URL", "127.0.0.1:6379"))
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': "%s:%s" %(cacheUrl.hostname, cacheUrl.port),
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': cacheUrl.password,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            }
        },
    },
}
# --- /Cache Configuration ---
