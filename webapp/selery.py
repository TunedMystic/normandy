import os
from celery import Celery
from getenv import env

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{0}'.format(env('DJANGO_SETTINGS_MODULE')))
from django.conf import settings

app = Celery('webapp')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
