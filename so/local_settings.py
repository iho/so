#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      },
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'django_db',
#        'USER': 'django_user',
#        'PASSWORD': 'qwerty',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    },
#}
### Tests

