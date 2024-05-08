### Main
## How to run project
    docker pull craezy/restaurant_api:v2
    docker run -d -p 8000:8000 craezy/restaurant_api:v2

## Possible API's
    http://0.0.0.0:8000/admin/
    http://0.0.0.0:8000/api/site-auth/
    http://0.0.0.0:8000/api/auth/
    http://0.0.0.0:8000/^auth/
    http://0.0.0.0:8000/api/token/ [name='token_obtain_pair']
    http://0.0.0.0:8000/api/token/refresh/ [name='token_refresh']
    http://0.0.0.0:8000/api/token/verify/ [name='token_verify']
    http://0.0.0.0:8000/api/restaurant/
    http://0.0.0.0:8000/api/restaurant/<int:pk>/
    http://0.0.0.0:8000/api/menu/
    http://0.0.0.0:8000/api/menu/<int:pk>/
    http://0.0.0.0:8000/api/employee/
    http://0.0.0.0:8000/api/employee/<int:pk>/
    http://0.0.0.0:8000/api/today/menu/
    http://0.0.0.0:8000/api/vote/<int:employee_id>/<int:menu_id>/
    http://0.0.0.0:8000/api/today/top/


## Additional

# Install all required dependencies from requirements.txt, especially:
    pip install -r requirement.txt

# Commands to create migrationg with db
    cd restaurant_api
    python manage.py migrate
    python manage.py makemigrations

# Creating superuser
    python manage.py createsuperuser
    username: root
    email: root@root.com
    password: root
    password2: root

# Command to run server
    python manage.py runserver
