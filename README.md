# Django Loan Application

## Table of contents
* [Django](https://docs.djangoproject.com/en/3.1/)
* [Docker](https://docs.docker.com/)
* [DRF](https://www.django-rest-framework.org/)

## General info
This project is simple bootstraped form with ML API which connects to machine learning model
and returns a response from ML model. The model file is in the research folder.	

## Main Technologies
Project is created with:
* Django: 3.1.5
* Django REST Framework: 3.12.2
* numpy: 1.16
* Postgres: 13
* tensorflow: 1.13.1
* Docker
	
## Setup
To run this project:

```
$ cd app
$ docker-compose build up -d
```

To build image:
```
$ docker-compose build
```

To run the container:
```
$ docker-compose up -d
```

To stop the container:
```
$ docker-compose stop
```

To bring down the container:
```
$ docker-compose down
```