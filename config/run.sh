cd /application
python manage.py makemigrations --settings=core.settings
python manage.py migrate --settings=core.settings
python manage.py initial_user --settings=core.settings
python manage.py runserver 0.0.0.0:8000