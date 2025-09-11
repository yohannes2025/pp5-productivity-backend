#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install project dependencies from requirements.txt
echo "Installing project dependencies..."
pip install -r requirements.txt

# Run collectstatic to gather all static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create a superuser non-interactively if the environment variable is set
# This is a workaround for the free tier's lack of shell access
if [[ -n "$DJANGO_SUPERUSER_USERNAME" && -n "$DJANGO_SUPERUSER_PASSWORD" ]]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --no-input --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL"
fi

echo "Build process completed successfully!"