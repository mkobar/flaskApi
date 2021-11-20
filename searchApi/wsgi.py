# run this with gunicorn:
#  gunicorn 'searchApi.wsgi'
#
# from
# https://stackoverflow.com/questions/25319690/how-do-i-run-a-flask-app-in-gunicorn-if-i-used-the-application-factory-pattern
#

from searchApi.app import create_app

application = create_app("config.settings_production")

# added guard - as gunicorn should not need it
# application.run()
