# -*- coding: utf-8 -*-

from django.conf import settings


class IEWebStandardsMiddleware(object):
    '''Inserts the X-UA-Compatible header into any HTML response.'''

    def process_response(self, request, response):
        response['X-UA-Compatible'] = getattr(settings,'X_UA_COMPATIBLE',
                                              'IE=edge,chrome=1')
        return response
