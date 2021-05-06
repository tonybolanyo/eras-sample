# Roomusu: a fullstack exercise

## Technologies

### Backend

- Django
- Django Rest Framework

## Run project locally

You need docker installed on your system.

Make copies of this files to create env vars for docker containers:

- postgres.env.sample => postgres.env
- pgadmin.env.sample => pgadmin.env
- django.env.sample => django.env

Before run docker containers you need to create some volumes manually:

```
docker volume create --name=db-data
docker volume create --name=db-admin
```

These volumes contains database files and pg-admin files.

Now you can use docker-compose to build docker images and run the application:

```
docker-compose build
docker-compose up -d
```

For import data you can run a custom command in django docker:

```
docker-compose exec django python manage.py fetch_init_data
```

This wil download the file and insert/update data in database, appling some
simple transformations.
