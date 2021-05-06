#!/bin/bash

# Start Django

function manage_app () {
  # Create and apply migrations
  python manage.py makemigrations
  python manage.py migrate
}

function start_development() {
  # Use integrated server for development
  echo "Starting dev server..."
  manage_app
  # Uncomment for remote debugging
  # python manage.py runserver --noreload --nothreading 0.0.0.0:8000
  # uncomment if you're using celery
  # nohup celery -A <project> worker -Q ${MONITOR_QUEUE} -l info &
  python manage.py runserver 0.0.0.0:8000
  echo "... dev server running"
}

function start_production() {
  # Use gunicorn for production
  echo "Starting server..."
  manage_app
  python manage.py collectstatic --no-input
  # uncomment if you're using celery
  # nohup celery -A <project> worker -Q ${MONITOR_QUEUE} &
  gunicorn roomusu.wsgi:application -w 4 -b 0.0.0.0:8000 --chdir=/app --log-file -
  echo "... server running"
}

if [ ${PRODUCTION} == "False" ]; then
  start_development
else
  start_production
fi
