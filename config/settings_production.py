# -*- coding: utf-8 -*-
#from config.settings import *
#from settings import *

# does gunicorn use TESTING and DEVELOPMENT?  It sure looks like it.

# flask core settings
DEBUG = False
TESTING = False

SECRET_KEY = 'token'

DEVELOPMENT = False

# Flask-WTF settings
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True

MAIL_USERNAME = 'you@email.com'
MAIL_PASSWORD = 'password'

CELERY_BROKER_URL = 'redis://:password@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:password@redis:6379/0'

