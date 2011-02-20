# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns

urlpatterns = patterns('madpub.apps.main.views',
    (r'^$', 'wizard'),
    (r'^success$', 'success'),
)
