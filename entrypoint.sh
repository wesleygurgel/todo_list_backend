#!/bin/bash

echo "Aplicando migrações..."
python manage.py migrate

echo "Verificando se as fixtures já foram carregadas..."
python - <<END
import os
import django
from django.core.management import call_command

# Configura o Django para ser usado no script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tasks.models import Task

if not Task.objects.exists():
    print("Carregando fixtures...")
    call_command("loaddata", "tasks/fixtures/tasks.json")
else:
    print("Fixtures já carregadas.")
END

exec "$@"
