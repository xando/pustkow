import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "/home/services/virtualenvs/pustkow_osiedle/lib/python2.6/site-packages/" )))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ['DJANGO_SETTINGS_MODULE'] = 'pustkow_osiedle.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
