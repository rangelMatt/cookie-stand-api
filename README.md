# Lab - Class 34: API Deployment

## Project: cookie-stand-api

### Author: Matt Rangel

### Date: 6/2/2022

### Links and Resources

- [Django](https://www.djangoproject.com)
- [Docker](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)
- [https://devcenter.heroku.com/articles/heroku-cli-commands](https://devcenter.heroku.com/articles/heroku-cli-commands)
- Morning Lecture

### Setup from template

- `clone down template`
- `rename .env_sample to .env`
- `docker compose run web bash`
- copy and paste/type`python -c 'import secrets; print(secrets:token_urlsafe()`
- Grab the key, update .env file with secret_key
- `run docker compose up`
- `docker compose run web bash`
- `python manage.py showmigrations`
- `docker compose up --build`
- `python manage.py migrate`
- `python manage.py runserver`
- `python manage.py startapp <app name>`
- `python manage.py makemigrations <app name>`
- `python manage.py migrate`
  - `python manage.py createsuperuser`
  - `UserName: <admin name>`
  - `password: <password>`
- `python manage.py runserver`
