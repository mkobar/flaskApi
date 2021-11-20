from flask import Flask
from flask_cors import CORS

# from celery import Celery

import os
from flask import got_request_exception

from searchApi.blueprints.page.views import page
from searchApi.blueprints.api.raw import raw
from searchApi.blueprints.api.search import search
from searchApi.blueprints.api.api import api

# from searchApi.extensions import debug_toolbar, csrf
from searchApi.extensions import csrf


# application factory, see: http://flask.pocoo.org/docs/patterns/appfactories/
# def create_app(settings_override=None):
def create_app(config_pyfile=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    # add global CORS support
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)
    # only support config/settings files for config
    # app.config.from_object('config.settings')
    app.config.from_object(config_pyfile)
    # app.config.from_pyfile('settings.py', silent=True)
    # app.config.from_pyfile(config_pyfile, silent=True)
    # app.config.from_pyfile(config_pyfile, silent=False)

    # if settings_override:
    #    app.config.update(settings_override)

    # now log config being used
    app.logger.info("Debug status is: " + str(app.config["DEBUG"]))
    app.logger.info("Testing status is: " + str(app.config["TESTING"]))
    app.logger.info("Development status is: " + str(app.config["DEVELOPMENT"]))
    app.logger.info("Server Name is: " + str(app.config["SERVER_NAME"]))

    # @app.before_first_request
    app.logger.info("Starting app for flaskapi", "info")

    app.register_blueprint(page)
    app.register_blueprint(raw)
    app.register_blueprint(search)
    app.register_blueprint(api)
    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    #    debug_toolbar.init_app(app)
    #    mail.init_app(app)
    csrf.init_app(app)

    return None


# only used if: python searchApi/app.py
if __name__ == "__main__":
    app = create_app("config.settings")
    app.run(debug=True)  # nosec - for bandit testing in dev
