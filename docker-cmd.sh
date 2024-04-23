#!/bin/sh
# vim:sw=4:ts=4:et

/usr/local/bin/python /backend/manage.py collectstatic --noinput

USER_EXISTS="from django.contrib.auth import get_user_model; User = get_user_model(); exit(User.objects.exists())"
/usr/local/bin/python /backend/manage.py shell -c "$USER_EXISTS" && /usr/local/bin/python /backend/manage.py createsuperuser --noinput

if [ "$1" = "--debug" ]; then
  /usr/local/bin/python /backend/manage.py runserver "0.0.0.0:$DJANGO_DEV_SERVER_PORT"
else
  /usr/local/bin/gunicorn "backend.wsgi:application" --bind "0.0.0.0:$GUNICORN_PORT" --workers "$GUNICORN_WORKERS" --timeout "$GUNICORN_TIMEOUT" --log-level "$GUNICORN_LOG_LEVEL"
fi
