"""
Django settings for webapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import dotenv
from getenv import env

dotenv.read_dotenv(dotenv = ".env")


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
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'Darth <vader@%s>' % PROJECT_DOMAIN
# --- /Email Configuration ---


# --- Manager Configuration ---
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Darth Vader', env("ADMIN_EMAIL", "")),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
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
)

CUSTOM_APPS = (
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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    }
}
# --- /Database Configuration ---


# --- Internationalization Configuration ---
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

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
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
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


# --- Logging Configuration ---
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'production_only': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'development_only': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'readable_sql': {
            '()': 'project_runpy.ReadableSqlFilter',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)-8s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)-8s [%(name)s:%(lineno)s] %(message)s',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'default': {
            'level': 'DEBUG',
            'class': 'config.lib.colorstreamhandler.ColorStreamHandler',
        },
        'console_dev': {
            'level': 'DEBUG',
            'filters': ['development_only'],
            'class': 'config.lib.colorstreamhandler.ColorStreamHandler',
            'formatter': 'simple',
        },
        'console_prod': {
            'level': 'INFO',
            'filters': ['production_only'],
            'class': 'config.lib.colorstreamhandler.ColorStreamHandler',
            'formatter': 'simple',
        },
        'file_log': {
            'level': 'DEBUG',
            'filters': ['development_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(ROOT_DIR, 'logs/log.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'file_sql': {
            'level': 'DEBUG',
            'filters': ['development_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(ROOT_DIR, 'logs/sql.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['production_only'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    # Catch-all modules that use logging
    # Writes to console and file on development, only to console on production
    'root': {
        'handlers': ['console_dev', 'console_prod', 'file_log'],
        'level': 'DEBUG',
    },
    'loggers': {
        # Write all SQL queries to a file
        'django.db.backends': {
            'handlers': ['file_sql'],
            'filters': ['readable_sql'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Email admins when 500 error occurs
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
# --- /Logging Configuration ---
