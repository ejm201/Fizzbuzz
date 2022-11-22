# Fizzbuzz

Motivated by <https://fizzbuzz.docs.apiary.io> using the [Django REST Framework](https://www.django-rest-framework.org) .


## Endpoints
* GET /fizzbuzz to list all fizzbuzz objects
* GET /fizzbuzz/id to retrieve a single fizzbuzz object
* POST /fizzbuzz to create a new fizzbuzz object, currently has a bug where the User-Agent is not populating.

## Instructions

1. Create the python virtual env

```shell
python3 -m venv .venv
source [path to .venv]/bin/activate
```
2. Install dependencies

```shell
pip install django
pip install djangorestframework
```


3. Start the database and create superuser

```shell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the server with `python manage.py runserver`

