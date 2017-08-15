# Simple Django Template
Template for create the minimized Django Project.


## Description
First of all, this project structure is heavily inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django). I found is has a really good project structure, but I have problem where they intergrated many thing to the template, and I found myself removing most of the things from the project. This is why I try to make this cookiecutter as less intergration as possible.


## What you will get
- Django 1.11.4
- Django REST Framework 3.6.3
- Pre-configuration with PostgreSQL
- Multiple settings for local development and production


## Setup Guide

This template need the help from Cookie Cutter, so you should install it if you haven't yet.
```bash
$ pip install cookiecutter
```


Now you can run command below to create a new Django project.  
**Note:** Project directory will be created at the current directory you are in.
```bash
$ cookiecutter https://github.com/NorakGithub/cookiecutter-simple-django
```


You will be asked to enter some information regarding your project.
- **repo-name** This will be the name of your repository name, or you can call the root directory of you project.
- **project-name** This will be the name of your project directory. Project directory is where you store all your django source code.
- **database-name** The name of your database. This cookie cutter was pre-configuration with Postgres Database.


Then change to your repository directory and add git.
```bash
$ cd my-repository
$ git init
```


Now, before we can run our project we need to install the required packages.  
We recommend using [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to create environment for your multiple python project.
```bash
$ pip install requirement.txt
```


Run your project
```bash
$ python manage.py runserver
```

It's done! Now you can test your project running at **http://localhost:8000/**.


## Sample App
We have made a sample authentications Django app, just to give you some idea what the project structure should be. Feel free to remove if you don't need it.


#### Tip on removing sample app
- Remove this `repo-name/project-name/apps/authentications/` directory.
- Remove authentications from `INSTALLED_APP` list.
- Remove authentications url from `web_urls` in `repo-name/project-name/config/routers/web_urls.py`


## Project Structure Ideology
```
+-- root
|   +-- project name
|   |   +-- apps
|   |   +-- config
|   |   |   +-- settings
|   |   |   |   +-- base.py
|   |   |   |   +-- local.py
|   |   |   |   +-- production.py
|   |   |   +-- routers
|   |   |   |   +-- api_urls.py
|   |   |   |   +-- web_urls.py
|   |   |   +-- urls.py
|   |   +---locale
|   |   +---templates
```
#### Apps
- **apps** This directory is where all of your app should be


#### Settings
- **base.py** This will be the common settings that can be used in both local development and production
- **local.py** This is where you add the settings for only your local development
- **production.py** This is where you add the settings for your production running

#### Routers
 - **api_urls.py** This is where you list all your api urls
 - **web_urls.py** This is where you list all your web urls
 
#### URLs
- **urls.py** Your main url

#### Locale
- This is where you keep all of your localized file

#### Templates
- This is where you keep all your templates file that could be shared in multiple apps.
