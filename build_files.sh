#!/bin/bash
set -e

# Print python version for logs
python --version

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Try to run migrations if DB is configured (won't break build if DB missing)
python manage.py migrate --noinput || true

echo "Build finished"
