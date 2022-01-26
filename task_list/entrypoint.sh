#! /bin/bash

python manage.py makemigrations 

python manage.py migrate 

python manage.py collectstatic --no-input

gunicorn task_list.wsgi:application --bind 0.0.0.0:8000 --reload -w 4