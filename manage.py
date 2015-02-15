#!/usr/bin/env python
import os
import sys
#from webapp.settings.base import get_env_setting
from getenv import env

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{0}'.format(env('DJANGO_SETTINGS_MODULE')))
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
