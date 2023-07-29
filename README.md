# KM 1151 Enterprise Portal
This Django-based Fuel Station Enterprise website features a homepage, a minimalistic navbar, and user authentication. The site utilizes an RDS AWS database in the production environment and is styled using __**Tailwind**__ **Flowbite**!.
### Current state of the project
**This project is currently a work in progress and is not yet ready for production use**. There may be bugs, incomplete features, and other issues that need to be resolved. Use at your own risk and please report any issues or suggestions to the project team. Thank you for your understanding and patience as we work to improve and finalize the site.
## Roadmap
1. Develop a homepage featuring images and information about the Enterprise.
2. Implement a minimalistic navbar accessible on every page of the site. **🗸**
3. Develop a user authentication system with Google or Instagram OAuth, ensuring all pages are secured against unauthorized access. **🗸** (50%:Google)
4. Set up an RDS AWS database for the production environment. **🗸**
5. Implement a ticketing system for customers.
6. Create additional modules for various tasks:
  - "Fuel Orders" module **🗸**
  - "Cash Transfer" (named Extra-Cash) module **🗸**
  - "Enterprise" module **🗸**
  - "Drivers" module **🗸**
  - "Truck and Trailers" module **🗸**
  - "Ticketing" module
7. Refine the visual styling with a singular `base.css` file and **Tailwind**. **🗸**
8. Include Continuous Integration/Continuous Deployment with GitHub Actions. **🗸**
9. Generate comprehensive documentation to implement the project in EC2.
10. Develop a pump operator's application to attend to orders that includes:
  - Intranet Login System **🗸**
  - "Fuel Orders" module
  - "Cash Transfer" (named Extra-Cash) module
  - "Ticketing" module
11. Setup Nginx+Gunicorn! **🗸**
12. Transition the project to a production environment.
## Skeleton 
```
.
└── portal
    ├── app  * Main Application
    │   ├── migrations
    │   ├── templatetags
    │   └── views
    ├── locale  *(internationalization)*
    │   ├── en
    │   ├── es
    │   └── pt
    ├── portal
    ├── staff  * Intranet module
    │   ├── migrations
    │   └── templates
    ├── static
    │   ├── CACHE
    │   ├── css
    │   ├── images
    │   ├── js
    │   ├── src
    │   ├── svg
    │   └── videos_background
    ├── templates
    │   ├── base
    │   ├── components
    │   └── modules
    └── theme  * Used by Tailwind and Flowbite
        ├── static
        └── static_src

```
## Language
Although this site is written in English but it will be implemented in Argentina, having **Spanish** as main language (having Portuguese and English as alt languages). To facilitate the use of internationalization I have created a 'translations.py' script that, together with 'translations.json', keeps all the translations of the site in a single json (currently "en", "es" and "pt" ). In summary: to change any term or create new ones, it is enough to edit or create new keys in the json. PRO TIP: chat-gpt will do all the work if you offer it a key and text in your favorite language, asking it to fill in the rest.
it is necessary to run "python manage.py makemessages -a" before the translations and "python manage.py compilemessages" at the end (usually I shoot the line: ```python manage.py makemessages -a && python translations.py && python manage.py compilemessage```
## Packages and Libraries
This project utilizes the following primary packages and libraries:
- **Django**: A high-level Python web framework that allows for clean, rapid development.
- mysqlclient: A Python DB API-2.0 compliant interface to MySQL.
- python-dotenv: A package that makes it easy to work with environment variables, particularly useful for handling application secrets.
- **django-allauth**: A comprehensive Django package that handles user authentication, including social login with OAuth providers.
- pytest: A robust Python testing framework, making it easy to write simple and scalable test cases.
- gunicorn: A Python WSGI HTTP Server for UNIX.
- whitenoise: A library for simplified static file serving for Python web apps.
- loguru: A library that provides a straightforward and powerful logging for Python.
- Pillow: A Python Imaging Library, handy for adding image processing capabilities to your Python interpreter.
- **django-tailwind** with **Flowbite**. A perfect pairing for Django, especially in this project that relies on components (template tags)... And no, I'm not going to admit that I don't get along with javascript and I'm always looking for ways to avoid it. Fallacies...
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