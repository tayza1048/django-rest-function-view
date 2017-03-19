# Django Funciton View Tasks App

This is the working example adapted from https://godjango.com/41-start-your-api-django-rest-framework-part-1.

## Installation
- Create a virtual environment: `python -m venv --without-pip myvenv`
- Activate virtual environment: `source myenv/bin/activate`
- Download get-pip.py from https://packaging.python.org/installing/#install-pip-setuptools-and-wheel
- Install pip: `python get-pip.py`
- Install requirements: `pip install -r requirements.txt`

## Usage
- curl http://127.0.0.1:8000/api/tasks/
- curl -X POST http://127.0.0.1:8000/tasks/ -d "title=hello world&description=a whole new world"
- curl -X PUT http://127.0.0.1:8000/tasks/1 -d "title=hello world&description=be nice"
- curl -X PUT http://127.0.0.1:8000/tasks/1 -d "title=hello world&description=be nice&completed=True"
- curl -X DELETE http://127.0.0.1:8000/tasks/1

## Useful Commands
- `python -m django --version`
- `python manage.py makemigrations tasks`
- `python manage.py migrate`
- `python manage.py runserver`
- `python manage.py runserver 0.0.0.0:8000`
- `python manage.py shell`
- `python manage.py test tasks`
