# coding: utf-8

from cms.app import create_app
app = application = create_app(__name__)

# pip install gunicorn
# gunicorn cms.wsgi -w 10 -b "0.0.0.0:8080"
