#!/bin/bash

# Remove migrations flag
[[ -f /mnt/flags/migration_end ]] && rm /mnt/flags/migration_end

# wait for Postgres to start
function postgres_ready() {
python << END
import sys
import psycopg2
import os
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'postgres')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
print('Try DB connection:', DB_NAME)
try:
    conn = psycopg2.connect(
        dbname=DB_NAME, host=DB_HOST, port=DB_PORT,
        user=DB_USER, password=DB_PASSWORD)
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres not ready - WAITING ..."
  sleep 1
done

# Start app
>&2 echo "Postgres READY - run start script command"

/start.sh
