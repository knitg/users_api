#!/bin/bash
# Migrate the database first
echo "Migrating the database before starting the server"
python manage.py makemigrations
python manage.py migrate
# Start Gunicorn processes
echo "Starting Gunicorn."
# exec gunicorn -b 0.0.0.0:8000 --access-logfile - "config.wsgi:application"
exec python manage.py runserver