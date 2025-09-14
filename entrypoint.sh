#!/bin/sh
set -e
python manage.py collectstatic --noinput
python manage.py migrate
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
