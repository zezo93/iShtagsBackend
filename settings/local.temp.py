# This is a temp for the local settings, make a copy for your self
# name it local.py, change settings as you machine required
# local.py should be like:

from __future__ import unicode_literals
from .base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ishtags-dev',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    },
 }
