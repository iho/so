#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

import getpass
import os

from django.core.urlresolvers import reverse, reverse_lazy

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS = True

#SESSION_ENGINE = 'redis_sessions.session'

#DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER

ROOT_URLCONF = 'so.urls'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's^fu1d4fe($5@&9@allfjxkwu!0esp!fsnki3io!n2l+t5u-xl'

# SECURITY WARNING: don't run with debug turned on in production!

TEMPLATE_DEBUG = DEBUG = True

ALLOWED_HOSTS = ['*']
CRISPY_TEMPLATE_PACK = 'foundation-5'


# All auth
# http://django-allauth.readthedocs.org/en/latest/#configuration
#ACCOUNT_SIGNUP_FORM_CLASS = 'question.forms.SignupForm'
# Application definition
# ACCOUNT_AUTHENTICATION_METHOD (=”username” | “email” | “username_email”)
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_PASSWORD_MIN_LENGTH = 8
ACCOUNT_USERNAME_MIN_LENGTH = 3
#LOGIN_REDIRECT_URL = '/profiles/home'
# ACCOUNT_SIGNUP_FORM_CLASS (=None) # для дня рождения etc
ACCOUNT_USERNAME_BLACKLIST = ['root', 'admin']
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
# All auth
LOGIN_REDIRECT_URL = reverse_lazy('profiles')
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


#
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_db',
        'USER': 'test_user',
        'PASSWORD': 'test_db',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)


# python -m smtpd -n -c DebuggingServer localhost:1025
# or sudo apt-get install postfix
# Internationalization

# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

STATIC_URL = '/static/'
TEMPLATE_DIRS = ('templates',)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGGING = {
    'version': 1,
}
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'question',
    'south',
    'taggit',
    'imagekit',
    #'rest_framework',
    'crispy_forms',
    'crispy_forms_foundation',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'compressor',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)


SOCIALACCOUNT_PROVIDERS = \
    {'google':
     {'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
      'AUTH_PARAMS': {'access_type': 'online'}},
     'openid':
     {'SERVERS':
      [dict(id='yahoo',
            name='Yahoo',
            openid_url='http://me.yahoo.com'),
       dict(id='hyves',
            name='Hyves',
            openid_url='http://hyves.nl'),
       dict(id='google',
            name='Google',
            openid_url='https://www.google.com/accounts/o8/id')]
      }
     }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
COMPRESS = True
COMPRESS_ENABLED = True
AUTH_USER_MODEL = 'question.User'
ALLOWED_HOSTS = ['.singularity.su.', '.localhost.', '.django.', '.singularity.su', '.localhost', '.django']

if getpass.getuser() == 'ihor':
    DEBUG = True
    from local_settings import *
    print('local')
else:
    DEBUG = False
    TEMPLATE_DEBUG = False
    print('production')


if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
    )
