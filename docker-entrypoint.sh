#!/bin/sh
# vim:sw=4:ts=4:et

set -e

if [ -z ${POSTGRES_DB+x} ]; then
  echo "PostgreSQL is not used. Skipping wait-for-it...";
  echo "Using SQLite. Creating database...";
else
  echo "Using PostgreSQL. Waiting for it to be ready...";
  /usr/local/bin/wait-for-it -s "$POSTGRES_HOST:$POSTGRES_PORT" -t 60
  echo "PostgreSQL is ready.";
fi
/usr/local/bin/python /backend/manage.py makemigrations --noinput
/usr/local/bin/python /backend/manage.py migrate --noinput

exec "$@"
