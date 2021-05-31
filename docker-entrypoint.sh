#!/bin/bash

# ----- Helpers -----
function terminateIfFailed(){
    local exit_code=$1

    if [ ! $exit_code -eq 0 ]; then
        echo "[ABORT] Aborting..."
        exit $exit_code
    fi
}
# ----- /Helpers -----


# Change directory
cd /app


# Apply django migrations
echo "[INFO] Applying django migrations..."
python manage.py migrate
terminateIfFailed $?
echo "[INFO] Success! Migrations completed."


# Collect static files
echo "[INFO] Collecting static files..."
python manage.py collectstatic --noinput
terminateIfFailed $?
echo "[INFO] Success! Static files created."


# Initialize system
echo "[INFO] Initializing system..."
python manage.py initialize_system
terminateIfFailed $?
echo "[INFO] Success! System initialized."


# Create superuser
echo "[INFO] Creating superuser 'admin' ..."
python manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'admin')"
echo "[INFO] Done!"


# Run uwsgi server
echo "[INFO] Starting uwsgi server..."
uwsgi --ini /app/uwsgi.ini

