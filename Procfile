web: gunicorn financialgraph.wsgi
worker: celery worker --app=financialgraph.taskapp --loglevel=info
