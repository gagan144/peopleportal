#!/bin/bash

# ----- Helpers -----
function terminateIfFailed(){
    local exit_code=$1

    if [ ! $exit_code -eq 0 ]; then
        echo "[ERROR] Command was not successfully executed. Aborting..."
        exit $exit_code
    fi
}
# ----- /Helpers -----


echo "----------------------------------------------"
echo "|               PeoplePortal                 |"
echo "|              Django Web App                |"
echo "----------------------------------------------"
echo ""


# Change directory
cd /app

# Wait for few seconds for postgres to boot up
echo "[INFO] Heuristically waiting for few seconds for services to boot up..."
sleep 10s


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
DJ_USERNAME="admin"
DJ_EMAIL="admin@example.com"
DJ_PASSWORD="admin"
python manage.py shell -c "from django.contrib.auth import get_user_model; UserModel=get_user_model(); UserModel.objects.create_superuser('${DJ_USERNAME}', '${DJ_EMAIL}', '${DJ_PASSWORD}') if not UserModel.objects.filter(username='${DJ_USERNAME}').exists() else None"
terminateIfFailed $?
echo "[INFO] Success! Superuser created."


# Run uwsgi server
echo "[INFO] Starting uwsgi server..."
uwsgi --ini /app/uwsgi.ini

