from django.conf.urls.defaults import *

urlpatterns = patterns('',
    ('', include('madpub.apps.main.urls')),
)
