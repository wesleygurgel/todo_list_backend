#!/bin/bash

echo "Aplicando migrações..."
python manage.py migrate

echo "Verificando se as fixtures já foram carregadas..."
python manage.py shell -c "from tasks.models import Task; exit(1 if Task.objects.exists() else 0)" || python manage.py loaddata tasks/fixtures/tasks.json

exec "$@"
