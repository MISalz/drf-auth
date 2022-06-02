LAB - Class 33
# Project: DRF_auth
**Author:** Michelle Salazar
----
## Problem Domain

**Features - Django**

Add JWT Authentication to your API.
Install needed libraries in project configuration and/or site settings.
Keep any pre-existing authentication so DRF Browsable API still usable.
Install needed libraries in project configuration and/or site settings.

**Features - Docker**

Switch to using Gunicorn instead of Django’s built in development server.
mind the number of workers to avoid sluggishness
Warning You will run into styling issues when you switch over to Gunicorn.
On Django side you’ll need to properly handle static files using Whitenoise

**Storage Options**

Your choice of SQLite or PostgreSQL
Adjust docker-compose.yml so that data is persisted in a volume outside of container.
These steps are different depending on whether SQLite or PostgreSQL is being used.


## Links and Resources

• back-end server url (when applicable)<br>

• front-end application (when applicable)

## Setup

docker compose up --build =builds new docker project 
docker compose -h = help
docker compose up  = runs docker file, create and start containers. -> run app


**PORT -** Port Number
local host: http://0.0.0.0:8000/

**DATABASE_URL -** URL to the running Postgres instance/db

*How to initialize/run your application (where applicable)*

• e.g. python main.py

## How to use your library (where applicable)

pip freeze > requirements.txt

## Tests


## ThunderClient, etc.

List the routes (including HTTTP method and note whether token is required) for:

localhost/admin/<br>
localhost/api/v1/snacking/<br>
localhost/api-auth/<br>
localhost/api/token/ <br>
localhost/api/token/refresh/<br>

**get tokens**<br>
localhost/api/token/ <br>
  -> Body Tab<br>
    ->JSON<br>
     -- copy/paste<br>
      {<br>
        "username":"admin",<br>
        "password":"Tree_hug5"<br>
        }<br>

**refresh tokens**<br>
localhost/api/token/refresh/<br>

**CRUD routes for resource**<br>
localhost/api/v1/snacking/<br>
  -> Auth tab<br>
    -> Bearer<br>
      -- copy/paste refresh token from post/api/token<br>
      

## Links



---
*Notes:*