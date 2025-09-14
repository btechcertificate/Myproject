#!/bin/sh
set -e

echo "Running collectstatic..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate


echo "Starting Gunicorn + Nginx..."
service nginx start
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
