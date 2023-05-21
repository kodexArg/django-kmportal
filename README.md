# KM 1151 Enterprise Portal
This is a Django project for a Fuel Station Enterprise website, which includes a main homepage, a minimalistic nav-bar, and user authentication. The site uses a MySQL Docker database in development, and will eventually move to RDS AWS database in production. The project is designed to be basic but professional-looking, and uses ~~Bootstrap 5~~ **Materialize** for styling.
## Disclaimer
### Language
Although this site is written in English but it will be implemented in Argentina, having **Spanish** as main language (and probably Portuguese and English in the future). For this reason, dictionaries labeled as dialog{} will be used within the code (hard-coded) to alleviate the use of any brave person who wants to take advantage of it in another language.
### Current state of the project
**This project is currently a work in progress and is not yet ready for production use**. There may be bugs, incomplete features, and other issues that need to be resolved. Use at your own risk and please report any issues or suggestions to the project team. Thank you for your understanding and patience as we work to improve and finalize the site.
## Roadmap
1. Create the homepage with pictures and information of the Enterprise.
2. Implement a minimalistic nav-bar that appears on every page of the site. **🗸**
3. Develop a user authentication system, allowing users to connect through Google or Instagram OAuth. All pages should be secured to prevent unauthorized access. **🗸** (50%:Google)
4. Set up a MySQL Docker database for development **🗸**.
5. Build out additional modules for specific tasks.
6. Fine-tune the visual styling with a single base.css file. **🗸**
7. Implement any required JavaScript.
8. Write tests and debug the code.
9. Deploy the project to production (Migrate to RDS AWS database in production)
## Skeleton 
```
**/**
├── app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── navbar.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── module/
│   │   │   ├── page1.html
│   │   │   └── page2.html
│   │   └── ...
│   ├── views.py
│   ├── urls.py
│   └── ...
── static/
│   ├── css/
│   ├── js/
├── portal/ 
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
└── manage.py
```
## Packages and Libraries
The following packages and libraries are used in this project:
- Django: A high-level Python web framework.
- mysqlclient: The database connector
- python-dotenv: A library for working with environment variables.
- django-allauth: A Django package that provides user authentication and social login with OAuth providers.
- pytest: A Python testing framework.

Please note that some additional packages may be required depending on the specific features and functionality you choose to implement.

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

```