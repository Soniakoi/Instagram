
# [Instagram]
#### Web clone of the Instagram app
#### July 29th, 2019
#### By **[SONIA WANGUI HABAMBA] 
## Description
This is a simple web clone of the instagram website. A user can create an account and sign into it.
The site supports uploading images, and following other users.
users can view photos uploaded by other users in the home page of app.
## Set Up and Installations
### Prerequisites
1. Django
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
### Activate virtual environment
Activate virtual environment using python3.6 as default handler
bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
### Install dependancies
Install dependancies that will create an environment for the app to run
pip3 install -r requirements.txt
### Create the Database
bash
psql
CREATE DATABASE insta;
### .env file
Create .env file and paste paste the following filling where appropriate:
python
SECRET_KEY = '<Secret_key>'
DBNAME = 'insta'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
### Run initial Migration
bash
python3.6 manage.py makemigrations insta
python3.6 manage.py migrate
### Run the app
bash
python3.6 manage.py runserver
Open terminal on localhost:8000
Testing the Application
To run the tests for the class files:
   $ python3.6 manage.py test
## Known bugs
Like and Follow functionality do not work
## Technologies used
   - Python 3.6
   - HTML
   - Bootstrap 4
   - JavaScript
   - Heroku
   - Postgresql
## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
| User is authenticated       | On homepage, click the sign up button | Redirected to the profile page.       |
| User can edit/add their profile details       | Clicks edit profile button |    Redirected to the profile page form template  |
|User can add image posts to their accounts      | Clicks on add button above gallery | Redirected to the forms page of adding posts      |
|User is able to navigate through the pages     | Clicks on the menu options in menu bar  | Navigation through the pages     |

## Support and contact details
Contact me on koisonia99@gmail.com for any comments, reviews or advice.
### License
[MIT](./License)
Copyright (c) 2019 **SONIA WANGUI HABAMBA**