## What’s contained in each file:
  - **manage.py** is what we use to execute commands on our terminal. We won’t have to edit it, but we’ll use it often.
  - **settings.py** contains some important configuration settings for our new project. There are some default settings, but we may wish to change some of them from time to time.
  - **urls.py** contains directions for where users should be routed after navigating to a certain URL.
  - **views.py**. This file contains a number of different functions, which are been compliting during web application process.
  - We already have a **urls.py** (in the same directory as **views.py**) file for the whole project, but it is best to have a separate one for each individual app.
  - Folders **templates/shop** and **static** are responsible for the front-end. The first one includes django *HTML* pages patterns, and in the second we can see other folders such as **font**, **img** and **shop** in which font I set to page, images and *CSS* code is stored accordingly.

## To run my application, you have to:
  - At first run **cd PROJECT_NAME**, where PROJECT_NAME is project’s directory (to navigate into it).
  - Then run **python manage.py makemigrations shop** and **python manage.py migrate** (to create database).
  - To get worked, run **python manage.py runserver**.
  - If you haven't installed a neccessary Python package that need to be installed in order to run web application, look requirements.txt file!

## Addition
  If you're the administrator of the site/cafe, you have to run **python manage.py createsuperuser** to create admin page, where admin is able to add menu positions and categories (to go to this page write **/admin** after service's main path).
