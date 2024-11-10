# CS527-Railway-Booking
## Instructions for TA - Project part 2 submission
1. Make sure Python is installed and install the required libraries by using `pip install -r requirements.txt`.
2. Create a database called 'railway' in your mySQL workbench by querying `CREATE DATABASE railway`.
3. Navigate to `webapp\webapp\settings.py` and change the credentials of the database to match your own.
4. Navigate into the folder containing `manage.py` and run `python manage.py makemigrations` and then `python manage.py migrate`. Then run the file: `railway.sql` in your mySQL workbench.
5. Run `python manage.py runserver` to start hosting the web application.
6. The site will be hosted locally and you will be able to access the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
7. Sign in on the login page using username: `admin` and password: `pass`.

## Project Overview
#### Layout
This repo contains the Django project folder named `webapp` and the web application folder named `railway`. `manage.py` is the executable to run the web application.

#### Activating the virtual environment (Optional)
It is highly recommended to create a venv for this project. \
Windows Users: \
Venv's can be created by running `python -m venv venv_name`. \
Consult [Python Venv](https://docs.python.org/3/library/venv.html) to create and run venvs. \
Install the required libraries by using `pip install -r requirements.txt`. \
Please do not create a venv in this folder or push a venv onto the repo.

#### Running the project locally
1. Create a database called 'railway' in your mySQL workbench by querying `CREATE DATABASE railway`.
2. Navigate to `webapp\webapp\settings.py` and change the credentials of the database to match your own.
3. Navigate into the folder containing `manage.py` and run `python manage.py makemigrations` and then `python manage.py migrate`. Then run the file: `railway.sql` in your mySQL workbench.
4. Run `python manage.py runserver` to start hosting the web application.
5. The site will be hosted locally and you will be able to access the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

#### Project Overview
* `railway.sql` contains the database schema to be run locally on your mySQL server. Please keep all your database changes in this file (that includes all data inserts and deletes). You will have to run the file every time you pull (if there are changes).
* `webapp\railway\views.py` is where you will be writing a majority of your backend code such as querying data and sending data to the frontend.
* `webapp\railway\urls.py` is where you can link views and html pages to a url of your choosing.
* Ignore `webapp\railway\models.py` since we are using mySQL and I thought it would be easier for everyone if we choose not to use Django's ORM. Though if you would like to use it, please let me know.
* `webapp\railway\templates\railway\` contains all of our html files.
* `webapp\railway\static\railway\`contains all of our css, js, and misc. media files.
