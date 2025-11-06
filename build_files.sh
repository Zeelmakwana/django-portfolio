#!/bin/bash
set -e
echo "Python version:"
python --version

# Make sure pip is up to date
python -m pip install --upgrade pip

# Install python dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files into staticfiles/ (used by vercel.json)
python manage.py collectstatic --noinput

# Try to run migrations, but don't fail the build if DB isn't configured
python manage.py migrate --noinput || true

echo "Build finished"
