import os
import sys

virtualenv = os.path.join(os.path.dirname(__file__), ".virtualenv/bin/activate_this.py")
execfile(virtualenv, dict(__file__=virtualenv))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ["DJANGO_SETTINGS_MODULE"] = "pustkow.settings"
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
