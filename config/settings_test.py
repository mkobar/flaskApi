# -*- coding: utf-8 -*-
#from config.settings import *

# flask core settings
DEBUG = False
TESTING = True
DEVELOPMENT = True
#SERVER_NAME = '127.0.0.1:5000'    # gives cookie error
# NOTE: .dev has HSTS set to force https - .devil does not
SERVER_NAME = 'localhost.devil:5001'    # required for pytest
SECRET_KEY = 'insecurekey'  # required for csrf

# flask wtf settings
WTF_CSRF_ENABLED = False

# flask mongoengine settings
MONGODB_SETTINGS = {
    'DB': 'flask_test'
}

# password hash method
PROJECT_PASSWORD_HASH_METHOD = 'md5'
