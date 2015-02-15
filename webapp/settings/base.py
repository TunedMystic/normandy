"""
Django settings for webapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import dj_database_url
from getenv import env

TZ_LOCATION = 'America/New_York'


# --- Celery Configuration ---
# http://chase-seibert.github.io/blog/2010/07/09/djangocelery-quickstart-or-how-i-learned-to-stop-using-cron-and-love-celery.html
CELERY_TIMEZONE = TZ_LOCATION

CELERY_SEND_EVENTS = True

CELERY_TASK_RESULT_EXPIRES =  10
# --- /Celery Configuration ---


# --- Project Configuration ---
PROJECT_NAME = "Webapp"

PROJECT_DOMAIN = "%s.com" %(PROJECT_NAME.lower())
# --- /Project Configuration ---


# --- Directory Settings ---
# Absolute path to the settings directory.
SETTINGS_DIR = os.path.dirname(__file__)

# Absolute path to the project directory.
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)

# Absolute path to the root (repo) directory.
ROOT_DIR = os.path.dirname(PROJECT_DIR)
# --- /Directory Settings ---


# --- Secret Configuration ---
SECRET_KEY = env("SECRET_KEY", "abc")
# --- /Secret Configuration ---


# --- Debug Settings ---
DEBUG = TEMPLATE_DEBUG = True
# --- /Debug Settings ---


# --- Email Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'Darth <vader@%s>' % (PROJECT_DOMAIN)
# --- /Email Configuration ---


# --- Manager Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Darth Vader', env("ADMIN_EMAIL", "")),
)

# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# --- /Manager Configuration ---


# --- Application Configuration ---
DJANGO_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
  "rest_framework",
  # Token Authentication
  "rest_framework.authtoken",
  "pipeline",
)

CUSTOM_APPS = (
  "misc",
  "tweets",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS
# --- /Application Configuration ---


# --- Middleware Definition ---
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# --- /Middleware Definition ---


# --- Url Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'webapp.urls'
# --- /Url Configuration ---


# --- Wsgi Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'webapp.wsgi.application'
# --- /Wsgi Configuration ---


# --- Database Configuration ---
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
  "default": dj_database_url.parse("sqlite:///" + os.path.join(ROOT_DIR, "db.sqlite3"))
}
# --- /Database Configuration ---


# --- Cache Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# --- /Cache Configuration ---


# --- Rest_Framework Configuration ---
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'PAGINATE_BY': 10,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 50,
}
# --- /Rest_Framework Configuration ---


# --- Internationalization Configuration ---
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = TZ_LOCATION

USE_I18N = True

USE_L10N = True

USE_TZ = True
# --- /Internationalization Configuration ---


# --- Template configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.core.context_processors.tz",
  "django.contrib.messages.context_processors.messages",
  "django.core.context_processors.request",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)
# --- /Template configuration ---


# --- Static configuration (CSS, JavaScript, Images) ---
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    "pipeline.finders.PipelineFinder",
)
# --- /Static configuration (CSS, JavaScript, Images) ---


# --- Media configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# --- /Media configuration ---


# --- Login, Logout Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = '/'

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = '/login/'

# https://docs.djangoproject.com/en/dev/ref/settings/#logout-url
LOGOUT_URL = '/logout/'
# --- /Login, Logout Configuration ---


# --- User Model Configuration ---
AUTH_USER_MODEL = 'auth.User'
# --- /User Model Configuration ---


# --- Testing Configuration ---
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# --- /Testing Configuration ---


# --- Pipeline Configuration ---
# https://django-pipeline.readthedocs.org/en/latest/configuration.html

PIPELINE_CSS = {
    'bundleCSS': {
        'source_filenames': (
          'tweets/css/dashboard.css',
          'tweets/css/main.css',
        ),
        'output_filename': 'tweets/css/scrolls.css',
    },
}

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE_JS = {
    'bundleJS': {
        'source_filenames': (
          'tweets/js/abc.js',
        ),
        'output_filename': 'tweets/js/spells.js',
    }
}
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
# --- /Pipeline Configuration ---


# --- Logging Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'production_only': {
            '()': 'django.utils.log.RequireDebugFalse',
         },
        'development_only': {
            '()': 'django.utils.log.RequireDebugTrue',
         },
     },
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['production_only'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ROOT_DIR, 'logs/log.log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console', 'logfile'],
            'propagate': True,
            'level':'WARN',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'tweets': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}
# --- /Logging Configuration ---
