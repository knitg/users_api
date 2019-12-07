#!/bin/bash
# Migrate the database first
echo "Migrating the database before starting the server"
python manage.py makemigrations
python manage.py migrate
# Start Gunicorn processes
echo "Starting Gunicorn."
exec gunicorn --bind 0.0.0.0:8030 -w 3 users_api.wsgi

# exec python manage.py runserver