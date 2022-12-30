# Moneytolia Case - Todo App

### Activate venv

    source venv/bin/activate # linux
    .\venv\Scripts\activate # windows

### Install requirements

    pip install -r requirements.txt

### Migrate database

    python manage.py migrate


### Run server

    python manage.py runserver

### Documentation

    http://127.0.0.1:8000/doc/

### Technologies

- Python Django
- Rest Framework
- Django Filters
- DRF Simple JWT
- Swagger for documentation

### App Workflow

In this project, users can register and login. When they log in, the API gives them access token and refresh token. This token is required because all other endpoints require login. User can create todo. To delete/edit/see todos, you must be the owner of that todo or have admin privileges. Admins can also bring a random todo or see a list of all todo's. Also, users can only see the list of their own todo.

