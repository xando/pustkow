# -*- coding: utf-8 -*-
import os
 
PROJECT_ROOT = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Sebastian  Pawluś', 'sebastian.pawlus@gmail.com')
)
MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = PROJECT_ROOT+'/data/pustkow.db'

TIME_ZONE = 'Europe/Warsaw Poland'
LANGUAGE_CODE = 'pl-pl'

SITE_ID = 1

MEDIA_URL = '/site_media/'
MEDIA_ROOT = PROJECT_ROOT+'/site_media/'

ADMIN_MEDIA_PREFIX = '/media/'

TEMPLATE_DIRS = (
    PROJECT_ROOT+'/templates/'
)

SECRET_KEY = 'i!4e3$7w#!=o32kj2)k$*1pntjdb$%2rjo^ntyb@s4a%!k$%!)'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
    )

ROOT_URLCONF = 'pustkow.urls'

TEMPLATE_DIRS = (
    PROJECT_ROOT+'/templates/'
)

INSTALLED_APPS = (
    'django.contrib.flatpages',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',

    'sorl.thumbnail',
    
    'page',
)

THUMBNAIL_PREFIX = '__'
