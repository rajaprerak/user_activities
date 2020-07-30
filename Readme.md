# Django based application to serve API of user activities
> https://user-activity-ftl.herokuapp.com/



[![Website shields.io](https://img.shields.io/badge/website-up-yellow)](http://rajaprerak.github.io/)
[![Ask Me Anything !](https://img.shields.io/badge/ask%20me-linkedin-1abc9c.svg)](https://www.linkedin.com/in/rajaprerak/)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Table of Contents 📚

- [Installation](#installation)
- [File Hierarchy](#filehierarchy)
- [Populate Database](#populatedatabase)
- [Features](#features)
- [Deployment](#deployment)
- [Migration(Optional)](#migration)
- [Developer](#developer)
- [License](#license)

## Installation 📦

>pip install -r requirements.txt

#### Clone

>git clone https://github.com/rajaprerak/user_activities.git

#### Run server locally

```shell
$ python manage.py runserver
```
> Go to localhost:8000

## FileHierarchy 📄
* **manage.py** - Run code
* **requirements.txt** - Required package information 
* **Procfile** - Contains commands that are executed in heorku on startup.
* **db.sqlite3** - Our database file
* **user_activities** folder
    * **settings.py** - It holds configuration values that your webapp needs.
    * **urls.py** - URL mapping file
    * **wsgi.py** - Used both by Django’s development server and in production WSGI deployments
* **activity** folder (app that we created inside our project)
    * **models.py** - Contains class that represent table in our database.
    * **admin.py** - Register the models that we created.
    * **serializers.py** - Convert query datatypes to python datatype that can be easily rendered to json or xml content type.
    * **urls.py** - URL mapper for our app views.
    * **views.py** - Takes web request and returns a web response.
    * **management/commands/** folder
        * **populate.py** - File contains custom management commands to populate the database with dummy data.
* Basic information for creating django project
    * To create project
        >django-admin starproject user_activities
    * To create app within project
        >python manage.py startapp activity
    * To create your own superuser to handle admin functionality
        >python manage.py createsuperuser
    * Create migration for all application installed in your project
        >python manage.py makemigrations
    * Apply migrations to the database
        >python manage.py migrate
    * Run code
        >python manage.py runserver

## PopulateDatabase 📮
* I have made use of Django custom management command to populate our database with some dummy data.
* The file is present in app folder(activity/management/commands/populate.py)
* To populate the database, run following command.
>python manage.py populate
## Features 📋
⚡️ **GET** request to get user activities in json format.\
⚡️ **POST** request to add users to the list.

## Deployment 🔗
* The application is deployed using heroku.
* Heroku reads from **Procfile** to run our application.
* All the required packages are present in **requirements.txt** file.
> https://user-activity-ftl.herokuapp.com/



## Migration 🔃
* Migration is django's way of propogating the changes you make to your models(updating database, creating new table, adding new fields). 
* Suppose you want to update the model or change some of the fields, you need to apply migration after doing the change. You are required to run following commands if you change code in **models.py**
>python manage.py makemigrations
>python manage.py migrate
>python manage.py runserver
>Go to localhost:8000

## Developer ✨

| <a href="https://rajaprerak.github.io" target="_blank">**Prerak Raja**</a> |
| :---: |
| [![Prerak Raja](https://github.com/rajaprerak.png?size=100)](https://rajaprerak.github.io)    
| <a href="https://rajaprerak.github.io" target="_blank">Porfolio Website</a> |  

## License 📜

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
