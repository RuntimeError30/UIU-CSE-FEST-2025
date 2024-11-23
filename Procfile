web: gunicorn csefest25.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn csefest25.wsgi