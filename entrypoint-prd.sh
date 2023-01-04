#!/bin/sh

echo 'Prd Running collectstatic...'
python manage.py collectstatic --no-input --settings=PasswordGenerator.settings.production

echo 'prd Applying migrations...'
python manage.py wait_for_db --settings=PasswordGenerator.settings.production
python manage.py migrate --settings=PasswordGenerator.settings.production

echo 'Prd Running server...'
#gunicorn --env DJANGO_SETTINGS_MODULE=PasswordGenerator.settings.production PasswordGenerator.wsgi.application --bind 127.0.0.1:8000
python manage.py runserver 0.0.0.0:8001 --settings=PasswordGenerator.settings.production
