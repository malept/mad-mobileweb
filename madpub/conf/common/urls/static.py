"Serves up static media when using runserver"

import sys
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = []

# Serve up static media if we're running the local development server.
if 'runserver' in sys.argv or \
   'runserver_plus' in sys.argv or \
   'testserver' in sys.argv:
    urlpatterns += staticfiles_urlpatterns()
