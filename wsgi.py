#!/usr/bin/python
import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'HelloWorld.settings'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi',
    'HelloWorld'))

virtenv = os.environ['APPDIR'] + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'venv/lib/python3.3/site-packages')
virtualenv = os.path.join(virtenv, 'venv/bin/activate_this.py')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
# 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()