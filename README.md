# Django Blog

a simple blog I created to learn the the basic concepts of the Django framework.

## How To Install
1. Install Python and pip
2. Run `pip install django` in command line
3. Within the project directory, run `python manage.py makemigrations` and `python manage.py migrate` to create the database
4. Create Super User with `python manage.py createsuperuser` and enter superuser account details
5. Run `python manage.py runserver` to get the server up and running

## Things I learnt 
### 1. URL configurations
  - passing primary keys and other variables to url routes
  - including URL paths
  - using the Django project-app structure
 
### 2. Models and database migrations
  - creating custom models and overriding default methods 
  - implementing one-to-one and one-to-many functions between models
  - using signals to create Profile instances when a new User model is created and delete when the case may be
  - manipulating objects with the Python shell

### 3. Views
  - function-based views
  - class-based views
  - passing a dictionary of lists, objects or variables as context to a template
  
### 4. Templates
  - inheritance from base templates
  - passing content blocks from template to template
  - using variables, loops and conditions to manipulate HTML data
  
### 5. User authentication
  - making custom user login and signup forms 
  - logout pages
  - page redirects when user isn't authenticated

### 6. Static files
  - creating custom paths for static files to avoid repetition
  - loading css and js to templates
  
### 7. Pillow (in addition)
  - storing and handling filepaths as database fields
  - compressing uploaded images 
  
### Others
  - class mixins
  - using the Django administration to manage data
  - plugging in apps to project
  - customizing forms using crispy_forms
  - using date-time object fields
  - pagination
  
 ## Built with
 - [Sublime Text](https://www.sublimetext.com) - text editor
 - [Django](https://www.djangoproject.com) - web framework
 - [Pillow](https://pillow.readthedocs.io/en/5.3.x/) - Python imaging library
