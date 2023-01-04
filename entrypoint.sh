#!/bin/sh

# echo 'Applying migrations...'
# python manage.py wait_for_db --settings=PasswordGenerator.settings.development
# python manage.py migrate --settings=PasswordGenerator.settings.development

echo 'Running server...'
#gunicorn --env DJANGO_SETTINGS_MODULE=PasswordGenerator.settings.production PasswordGenerator.wsgi.application --bind 127.0.0.1:8000
python manage.py runserver 0.0.0.0:8000 --settings=PasswordGenerator.settings.development 


