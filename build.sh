#!/usr/bin/env bash
# Script hii inaendeshwa na Render kila mara unapo-deploy.
set -o errexit  # Simamisha mara moja endapo amri yoyote itashindwa

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py ensure_superuser
