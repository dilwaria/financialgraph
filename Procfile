web: gunicorn config.wsgi:application
worker: celery worker --app=financialgraph.taskapp --loglevel=info
