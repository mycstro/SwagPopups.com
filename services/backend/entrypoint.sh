#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver 0.0.0.0:8000
