#!/bin/sh
python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=a/@1234567 \
    DJANGO_SUPERUSER_USERNAME=admin \
    DJANGO_SUPERUSER_EMAIL=admin@domain.com \
    ./manage.py createsuperuser \
    --no-input
