from madpub.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'madpub.conf.dev.urls'

MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mad',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}
