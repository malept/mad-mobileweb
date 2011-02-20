# Import global settings to make it easier to extend settings. 
from django.conf.global_settings import *
# Import the project module to calculate directories relative to the module
# location.
import os
import madpub

PROJECT_ROOT, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(madpub.__file__))
)
# This assumes the project is installed in the src directory of a virtualenv.
VAR_ROOT = os.path.join(os.path.dirname(os.path.dirname(PROJECT_ROOT)), 'var')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'

ROOT_URLCONF = 'madpub.conf.urls'

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE_CLASSES += (
    'django.middleware.csrf.CsrfViewMiddleware',
    'madpub.middleware.IEWebStandardsMiddleware',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'kv>S-Y>8B9)Zd[4!W-{5s#1BS[:.1::O'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, PROJECT_MODULE_NAME, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, PROJECT_MODULE_NAME, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_assets',
    'madpub.apps.main',
)
