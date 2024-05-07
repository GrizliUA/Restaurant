## Install all required dependencies from requirements.txt, especially:
    pip install -r requirement.txt

## Commands to create migrationg with db
    cd restaurant_api
    python manage.py migrate
    python manage.py makemigrations

## Creating superuser
    python manage.py createsuperuser
    username: root
    email: root@root.com
    password: root
    password2: root

## Command to run server
    python manage.py runserver
