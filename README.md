# KM 1151 Enterprise Portal
This Django-based Fuel Station Enterprise website features a homepage, a minimalistic navbar, and user authentication. The site utilizes an RDS AWS database in the production environment and is styled using **Tailwind**.
### Language
Although this site is written in English but it will be implemented in Argentina, having **Spanish** as main language (and probably Portuguese and English as alt languages). For this reason, dictionaries labeled as dialog{} will be used within the code (hard-coded) to alleviate the use of any brave person who wants to take advantage of it in another language.
### Current state of the project
**This project is currently a work in progress and is not yet ready for production use**. There may be bugs, incomplete features, and other issues that need to be resolved. Use at your own risk and please report any issues or suggestions to the project team. Thank you for your understanding and patience as we work to improve and finalize the site.
## Roadmap
1. Develop a homepage featuring images and information about the Enterprise.
2. Implement a minimalistic navbar accessible on every page of the site. **🗸**
3. Develop a user authentication system with Google or Instagram OAuth, ensuring all pages are secured against unauthorized access. **🗸** (50%:Google)
4. Set up an RDS AWS database for the production environment. **🗸**
5. Implement a ticketing system for customers.
6. Create additional modules for various tasks.
7. Refine the visual styling with a singular `base.css` file and **Tailwind**. **🗸**
8. Include Continuous Integration/Continuous Deployment with GitHub Actions. **🗸**
9. Generate comprehensive documentation to implement the project in EC2.
10. Develop a pump operator's application to attend to orders.
11. Setup Nginx+Gunicorn!
12. Transition the project to a production environment.
## Skeleton 
```
**/**
├── extras
│ ├── ddbb
│ ├── docs
│ ├── scripts
│ └── tailwind
└── portal
├── app
│ ├── migrations
│ ├── templates
│ └── templatetags
├── locale
│ ├── en
│ ├── es
│ └── pt
├── portal
└── static
├── css
├── images
├── js
├── svg
├── tailwind
└── videos_background
```
## Packages and Libraries
## Packages and Libraries

This project utilizes the following primary packages and libraries:

- Django: A high-level Python web framework that allows for clean, rapid development.
- mysqlclient: A Python DB API-2.0 compliant interface to MySQL.
- python-dotenv: A package that makes it easy to work with environment variables, particularly useful for handling application secrets.
- django-allauth: A comprehensive Django package that handles user authentication, including social login with OAuth providers.
- pytest: A robust Python testing framework, making it easy to write simple and scalable test cases.
- gunicorn: A Python WSGI HTTP Server for UNIX.
- whitenoise: A library for simplified static file serving for Python web apps.
- loguru: A library that provides a straightforward and powerful logging for Python.
- beautifulsoup4: A library for pulling data out of HTML and XML files, useful in web scraping.
- Django-livereload-server: A Django app that integrates livereload with the Django development server.
- Pillow: A Python Imaging Library, handy for adding image processing capabilities to your Python interpreter.

Please note that the specific packages and libraries required for your project may vary based on the features and functionalities you choose to implement.

In addition to these Python packages, some system-level packages are also required. If you're using an Ubuntu machine, you may need to install the following:
- python3-dev: Includes the header files you need to build Python extensions.
- libmysqlclient-dev: This package contains the development files of the MySQL library and is needed for mysqlclient.
- default-libmysqlclient-dev: This is a transitional package depending on the default MySQL variant and is also required for mysqlclient.
You can install these packages on your Ubuntu machine using the following command:
'''
sudo apt-get install python3-dev libmysqlclient-dev default-libmysqlclient-dev
'''
## Installation
### ToDo
_step  by step guide_
_script to create mysql users and database_
### Manual steps
#### ENVIRONMENT VARIABLES
These are the environment variables this project uses (.env file under development stage).
Here you provide the required string to connect to your database 'km1151' with any user.
```
SECRET-KEY=super-secret-password
DEBUG=True

MYSQL_DDBB=km1151
MYSQL_USER=...
MYSQL_PASS=...
MYSQL_HOST=...
MYSQL_PORT=...

SITE_ID=..
```
## CI/CD with GitHub Actions
This project uses GitHub Actions for Continuous Integration/Continuous Deployment (CI/CD), as defined in the workflow file located at `.github/workflows/pull-ec2.yml`.

In this workflow, whenever a push is made to the `main` branch, a series of operations are automatically triggered:

1. The code is checked out from the repository.

2. Commands are executed over SSH on an EC2 instance, which include:
   - Logging the deployment trigger event and time.
   - Pulling the latest code from the `main` branch.
   - Upgrading pip and installing the project requirements.
   - Running Django migrations.
   - Logging the completion of the update.


In order to make it work you need an already configured Ec2 with a cloned project in /home/***/django-kmportal with:

- An active connection to a database (I'm using RDS in production).
- An existing `km1151` database with the user credentials provided in the `.env` file mentioned earlier in the manual installation steps.
Please note that before implementing this GitHub Actions workflow, the project was already set up and functioning correctly on the EC2 instance. Therefore, the GitHub Actions workflow is primarily used for updating the EC2 instance with the latest changes from the repository, not for initial setup of the project.

## Setting Up the Database and Django Admin
After setting up your environment and installing all necessary packages, you'll need to configure your database and set up Django Admin.
1. **Create a Super User**
You can create a super user who can access the admin site with the following command:
   ```shell
   python manage.py createsuperuser
   ```
You will be prompted to enter a username, email address, and password for the super user.
2. **Access the Admin Site**
Once the super user has been created, you can start the development server with:
   ```shell
   python3 manage.py runserver 0.0.0.0:8000
   ```
Then, navigate to http://localhost:8000/admin in your web browser. Use the credentials of the super user to log in.
3. **Configure the Domain from the Django Admin**
Once you're logged in to the admin panel, navigate to "Sites" under the "SITES" section. Click on the existing site and replace "example.com" with your own domain name in both "Domain name" and "Display name" fields. Then, click "Save".
__Setup Google as Social Authentication Provider__
To setup Google as your social authentication provider, go to "Social applications" under the "SOCIAL ACCOUNT" section and click "Add social application".
__Fill in the following details:__
- Provider: Choose "Google" from the dropdown.
- Name: Enter "Google".
- Client ID: Check the value in .env (You can get this number from your database)
- Secret Key: Enter your Secret Key. (This can also be obtained from the Google Cloud Console)
- After entering these details, click on "Save".
Now, your Django admin site is configured and ready to handle authentication using Google

### ToDo-cument:
you can stop reading from now on... No, seriously, this is garbage, i'm not even sure if I'm going to use it:
- nginx installation on prod
- gunicorn installation on prod
- open ports in aws security group
```
sudo apt install gunicorn nginx
cd /home/ubuntu/django-kmportal/
```
test:
```
gunicorn portal.wsgi:application --bind 0.0.0.0:8080
```.

current nginx confguration (where are the logs you ...)
```
server {
    listen 80;
    server_name km1151.duckdns.org; # Replace with your domain or IP addres

    location ^/static/ {
            autoindex on;
            alias /home/ubuntu/django-kmportal/local-cdn/static/;
        }

    location / {
            proxy_pass http://localhost:8080;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
        }
}
```.

And I really should be reading this https://flowbite.com/docs/getting-started/django/