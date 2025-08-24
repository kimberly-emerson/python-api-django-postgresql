# python-api-django-postgresql

![GitHub Tag](https://img.shields.io/github/v/tag/kimberly-emerson/python-api-django-postgresql?include_prereleases&style=flat-square&logo=github&labelColor=black&color=%2300c950)

---

<div align="center">

[![Python Badge](https://img.shields.io/badge/python-3.13.7-3670A0?style=flat-square&labelColor=blue&logo=python&logoColor=white&color=white)](https://www.python.org/) [![Django Badge](https://img.shields.io/badge/django-5.2.5-4?logo=django&style=flat-square&labelColor=%23092E20&color=white)](https://www.djangoproject.com/) [![Django REST Framework Badge](https://img.shields.io/badge/django--rest--framework-3.16.1-blue?style=flat-square&labelColor=black&logo=django&logoColor=white&color=white)](https://www.django-rest-framework.org/) <br />
[![Swagger Badge](https://img.shields.io/badge/Swagger-Docs-%23Clojure?style=flat-square&logo=swagger&labelColor=7FFF00&color=white&logoColor=black)](https://drf-yasg.readthedocs.io/en/stable/readme.html) [![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-3.17-316192?logo=postgresql&labelColor=blue&color=white&logoColor=white)](https://www.postgresql.org/) [![pytest](https://img.shields.io/badge/pytest-8.4.1-white?style=flat-square&logo=pytest&logoColor=white&label=pytest)](https://docs.pytest.org/en/stable.html) [![PDM](https://img.shields.io/badge/PDM-2.25.5-white?labelColor=mediumpurple&logo=pdm&logoColor=white)](https://pdm.fming.dev)
</div>

## Overview

This repository showcases a modular, production-ready Django REST API powered by PostgreSQL and enriched with robust authentication, error handling, and auto-generated documentation.

### Key Features

- Clean *RESTful architecture* using **Django** and **Django REST Framework**
- JWT-based authentication with multi-method support (JWT, session, token)
- Centralized error handling via `drf-standardized-errors`
- Auto-generated **Swagger** & **ReDoc** docs with deep linking and JWT integration
- Environment-driven configuration using `.env` and `python-decouple`
- Multi-schema **PostgreSQL** support for domain-separated data access
- Structured Django logging with separate debug, info, and error channels

## 𝄜 Data Pipeline

The API is powered by a PostgreSQL database populated via a robust Python-driven ETL pipeline. The source data originates from the `AdventureWorks2022` SQL Server database and is seamlessly migrated into the `aw_sales` PostgreSQL schema using the companion repo:

The ETL process:
- Creates PostgreSQL schemas and tables with SQL CREATE queries
- Extracts raw sales and customer data from SQL Server with SQL SELECT queries
- Loads the extracted data into PostgreSQL with SQL INSERT queries for fast, reliable API access

Whether you're building dashboards, running analytics, or integrating with other services, this setup ensures the data is structured, accessible, and production-ready.

## #️⃣ Technology Stack

|Layer|Technology|
|---|---|
|Language|[![Python Badge](https://img.shields.io/badge/python-3.13.7-3670A0?style=flat-square&labelColor=blue&logo=python&logoColor=white&color=white)](https://www.python.org/)|
|Web Framework|[![Django Badge](https://img.shields.io/badge/django-5.2.5-4?logo=django&style=flat-square&labelColor=%23092E20&color=white)](https://www.djangoproject.com/)|
|REST Framework|[![Django REST Framework Badge](https://img.shields.io/badge/django--rest--framework-3.16.1-blue?style=flat-square&labelColor=black&logo=django&logoColor=white&color=white)](https://www.django-rest-framework.org/)|
|Database|[![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-3.17-316192?logo=postgresql&labelColor=blue&color=white&logoColor=white)](https://www.postgresql.org/)|
|Authentication|[![{} JWT](https://img.shields.io/badge/%7B%7D%20Simple%20JWT-Auth-white?style=flat-square&labelColor=2ea44f&color=ffffff&logoColor=white)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)|
|Error Handling|![DRF Standardized Errors](https://img.shields.io/badge/drf--standardized--errors-0.15.0-white?style=flat-square)|
|Testing|[![pytest](https://img.shields.io/badge/pytest-8.4.1-white?style=flat-square&logo=pytest&logoColor=white&label=pytest)](https://docs.pytest.org/en/stable.html)|
|Documentation|[![Swagger Badge](https://img.shields.io/badge/Swagger-Docs-%23Clojure?style=flat-square&logo=swagger&labelColor=7FFF00&color=white&logoColor=black)](https://drf-yasg.readthedocs.io/en/stable/readme.html)|
|Dependency Management|[![PDM](https://img.shields.io/badge/PDM-2.25.5-white?labelColor=mediumpurple&logo=pdm&logoColor=white)](https://pdm.fming.dev)|
|Environment|[![DotEnv Badge](https://img.shields.io/badge/16.0.1-0?label=dotenv&style=flat-square&logo=dotenv&labelColor=black&logoColor=white&color=white)](https://pypi.org/project/python-dotenv/)|

## ✅ Project Setup Instructions

### Initialize and Create Django Project

Create a clean, structured Django project with PDM and prep it for PostgreSQL-powered development:

1. **Initialize the project and add Django**  
   Fire up your workspace with:  
   ```powershell
   pdm init -p core django
   ```  
   This creates a new project folder named `core` and installs Django as a dependency—clean, isolated, and ready to build.

2. **Rename for clarity and context**  
   Give the project a meaningful name that reflects its purpose:  
   ```bash
   rni core python-api-django-postgresql
   ```  
   Now the folder says exactly what it does.

3. **Enter the project directory**  
   Time to dive in:  
   ```bash
   cd python-api-django-postgresql
   ```

4. **Create the Django app**  
   Scaffold the `api` app where the endpoints will live:  
   ```powershell
   python manage.py startapp api
   ```

5. **Activate the virtual environment**  
   Lock in the dependencies and isolate the dev environment:  
   ```powershell
   . .venv\Scripts\activate
   ```

```powershell
# initializes and creates a django project named `core`, and adds Django as a dependency
pdm init -p core django
# renames the folder to `python-api-django-postgresql`
rni core python-api-django-postgresql
# changes into the new project directory
cd python-api-django-postgresql
# creates new Django app in project directory
python manage.py startapp api
# activate .venv
. .venv\Scripts\activate
```

### GitHub Repository Setup

Let’s take the freshly scaffolded Django + PostgreSQL project and turn it into a public-facing, contributor-ready GitHub repository:

1. **Initialize Git locally**  
   Start version control in the project folder:  
   ```powershell
   git init
   ```

2. **Create the GitHub repo and link it**  
   Push the local project to GitHub with a public repo named `python-api-django-postgresql`:  
   ```powershell
   gh repo create python-api-django-postgresql --public --source=.
   ```

3. **Verify the remote origin**  
   Confirm the repo is properly linked:  
   ```powershell
   git remote --verbose
   ```

4. **Add a clear, searchable description**  
   Help contributors and recruiters understand the project at a glance:  
   ```powershell
   gh repo edit --description 'Python API demo project'
   ```

5. **Tag the tech stack and tooling**  
   Boost discoverability and contributor context with relevant topics:  
   ```powershell
   gh repo edit --add-topic api
   gh repo edit --add-topic python
   gh repo edit --add-topic django
   gh repo edit --add-topic django-rest-framework
   gh repo edit --add-topic drf-yasg
   gh repo edit --add-topic drf-standardized-errors
   gh repo edit --add-topic postgresql
   gh repo edit --add-topic pytest
   gh repo edit --add-topic jwt-auth
   gh repo edit --add-topic pdm
   ```

```powershell
# initialize repo
git init
# create repo
gh repo create python-api-django-postgresql --public --source=.
# verify remote origin
git remote --verbose
# add repo description
gh repo edit --description 'Python API demo project'
# add repo topics
gh repo edit --add-topic api
gh repo edit --add-topic python
gh repo edit --add-topic django
gh repo edit --add-topic django-rest-framework
gh repo edit --add-topic drf-yasg
gh repo edit --add-topic drf-standardized-errors
gh repo edit --add-topic postgresql
gh repo edit --add-topic pytest
gh repo edit --add-topic jwt-auth
gh repo edit --add-topic pdm
```

### GitHub Project Setup

Ready to launch a new initiative and track the first improvement? Use the GitHub CLI to streamline project creation and issue management—all from the command line.

1. **Create a New Project** 
    Creates a fresh GitHub project under the specified owner (user or organization). Replace `[project-owner]` with your GitHub username or org name, and `[project-title]` with a clear, descriptive name for the project.

```powershell
gh project create --owner [project-owner] --title "[project-title]"
```

2. **Log an Enhancement Issue**
    Creates a new issue tagged as an enhancement, links it to your project board, and assigns it to you. Perfect for tracking improvements, refactors, or new features.

```powershell
gh issue create --title "[issue-title]" --project "[project-name]" --label "enhancement" --assignee "@me"
```

```powershell
# create project
gh project create --owner [project-owner] --title [project-title]
# create issue
gh issue create --title [issue-title] --project [project-name] --label 'enhancement' --assignee '@me'
```

### 📦 Install Dependencies

This package list equips the Django REST Framework API project with everything needed for secure authentication, robust error handling, dynamic filtering, PostgreSQL integration, and clean environment management.

| Package                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `djangorestframework`           | Core toolkit for building Web APIs with Django.                            |
| `djangorestframework-simplejwt` | Lightweight JWT authentication for DRF.                                    |
| `drf-yasg[validation]`          | Swagger/OpenAPI generation with request/response validation.               |
| `drf-standardized-errors`       | Consistent, spec-compliant error formatting for DRF responses.             |
| `psycopg2`                      | PostgreSQL adapter for Python; enables Django to connect to PostgreSQL.    |
| `python-dotenv`                 | Loads environment variables from `.env` files into Python applications.    |
| `django-cors-headers`           | Handles Cross-Origin Resource Sharing (CORS) for Django APIs.              |
| `django-filter`                 | Adds dynamic filtering support to DRF views and querysets.                 |
| `python-decouple`               | Separates settings from code using environment variables and `.env` files. |
| `pytest`        | Core testing framework for Python            | 
| `pytest-django` | Django plugin for `pytest`|


```powershell
pdm add djangorestframework
pdm add djangorestframework-simplejwt
pdm add drf-yasg[validation]
pdm add drf-standardized-errors
pdm add psycopg2
pdm add python-dotenv
pdm add django-cors-headers
pdm add django-filter
pdm add python-decouple
pdm add pytest
pdm add pytest-django
```

### Create Super User

Generate an account that unlocks full access to the Django Admin dashboard—perfect for managing models, users, and backend configurations with ease.
python manage.py createsuperuser --username [your_username] --email [your_email]

The superuser will have:
- Full CRUD access to all registered models
- Permissions to manage users, groups, and roles
- Visibility into backend data without touching the code

```powershell
python manage.py createsuperuser --username [username] --email [email]
```

### 📁 Create Files and Folders

ℹ️ The commands used to create the files and folders are PowerShell [aliases](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-alias?view=powershell-7.5).

❗ Execute the commands in the project's root folder -- `python-api-django-postgresql`.

#### Folders

```powershell
md api/config
md api/models
md api/schemas
md api/views
md api/utils
```

#### Files

ℹ️ `db.sqlite3` is removed because the file is created on initialization and the project uses PostgreSQL instead.  

ℹ️ `/api` Python files are removed because the project structure contains folder and modular models, schemas, views, etc.

```powershell
ri db.sqlite3
ri api/__init__.py
ri api/admin.py
ri api/apps.py
ri api/models.py
ri api/tests.py
ri api/views.py
ni api/router.py
ni api/config/swagger.py
ni api/urls.py
ni api/schemas/group_serializer.py
ni api/schemas/user_serializer.py
ni api/views/group_viewset.py
ni api/views/user_viewset.py
ni logs
ni tests
ni .env
ni .env.example
```

### Project Settings

#### .env Files

The .env files (`.env` and `.env.example`) should contain the following environment variables.

❗Change the environment variables to match the required database and project structure requirements.

```yaml
# Application Environment
APP_ENV=local
APP_DEBUG=true
APP_URL=http://localhost:8000

# Database Configuration
DB_CONNECTION=postgresql
DB_HOSTNAME=localhost
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=[database]
DB_USERNAME=[username]
DB_PASSWORD=[password]

# Directory Path
ROOT_DIR=/
APP_DIR=/api
CORE_DIR=/core
LOGS_DIR=/logs

# Logging
LOG_LEVEL=DEBUG

# Authentication
SECRET_KEY=[key]
```

#### core/settings.py

The `settings.py` file is the central configuration hub for a Django project. It defines key parameters that control how the application behaves across environments.

**Core responsibilities include:**
- **Environment setup:** Specifies `DEBUG`, `ALLOWED_HOSTS`, and environment-specific flags.
- **App registration:** Lists installed apps via `INSTALLED_APPS`.
- **Middleware stack:** Configures request/response processing layers in `MIDDLEWARE`.
- **Database settings:** Defines database engine, name, credentials, and connection options.
- **Static & media files:** Sets paths for serving static assets and user-uploaded content.
- **Authentication & security:** Manages password validators, session settings, and secret keys.
- **Internationalization:** Controls language, timezone, and localization behavior.

##### Add Imports

```python
# loads values from `.env` files instead of hardcoding them
from decouple import config
```

##### Secret Key

> ℹ️ Generate with `django.core.management.utils.get_random_secret_key()` for strong entropy.

The `SECRET_KEY` is a critical setting in Django’s `settings.py` file used for cryptographic signing. It ensures the integrity and security of:
- Session cookies
- Password reset tokens
- CSRF protection
- Any data signed by Django’s internal mechanisms

❗ Instead of keeping the `SECRET_KEY` hard coded by Django on project setup, move it to the `.env` file and retrieve it using `config()`.

```python
SECRET_KEY = config('SECRET_KEY')
```

##### Allowed Hosts

`ALLOWED_HOSTS` should explicitly list the domain names the Django app is allowed to serve. This protects against HTTP Host header attacks by rejecting requests with unexpected or spoofed host headers.

```python
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
```

##### Installed Apps

Activate the Django app and its third-party integrations, by listing them in the `INSTALLED_APPS` dictionary.

```python
INSTALLED_APPS = [
    # ...
    # third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    "drf_standardized_errors",
    # project apps
    "api",
]
```

##### Root URL Configuration

- Points Django to the module containing the `urlpatterns` list.
- Acts as the entry point for all incoming HTTP requests.
- Enables Django to resolve URLs by matching request paths against patterns defined in `core/urls.py`.

```python
ROOT_URLCONF = "core.urls"
```

##### Database

Connects Django to a PostgreSQL database, with a custom schema search path for multi-schema querying.

> ℹ️ The `search_path` option allows Django to query across multiple PostgreSQL schemas (people, production, sales, public) without schema-qualified table names.

```python
# set database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USERNAME'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOSTNAME'),
        'PORT': config('DB_PORT'),
        "OPTIONS": {
            "options": "-c search_path=people,production,sales,public"
        },
    }
}
```

##### Logging

The `LOGGING` dictionary configures logging across the API.

- **Captures logs across environments** with granular control over verbosity and destinations.
- **Separates concerns** by routing debug, info, and error messages to dedicated log files.
- **Keeps the console clean** during development, thanks to smart filtering with `require_debug_true`.

```python
# define the `ROOT_DIR` constant
from pathlib import Path
from decouple import config

ROOT_DIR = Path(__file__).resolve().parent.parent
```

```python

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    'handlers': {
        'console': {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f"{ROOT_DIR}\\{config('LOGS_DIR')}\\debug.log",
            'formatter': 'verbose',
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f"{ROOT_DIR}\\{config('LOGS_DIR')}\\app.log",
            'formatter': 'verbose',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': f"{ROOT_DIR}\\{config('LOGS_DIR')}\\error.log",
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_info', 'file_error'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'file_info', 'file_error'],
            'level': 'ERROR',  # Log HTTP 4xx and 5xx errors
            'propagate': False,
        },
        'api': {  # Custom logger for your DRF app
            'handlers': ['console', 'file_info', 'file_error'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```

##### drf_yasg

###### REST_FRAMEWORK

`REST_FRAMEWORK` defines how Django REST Framework (DRF) API handles authentication and access control.

- Supports multiple auth methods for flexibility across environments (e.g., JWT for APIs, session for admin, token for legacy clients).
- Restricts access to authenticated users by default, enforcing secure API usage.
- Plays well with Swagger/OpenAPI when paired with proper security schemes.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
```

###### SWAGGER_SETTINGS

`SWAGGER_SETTINGS` customizes how `drf-yasg` presents authentication in auto-generated Swagger UI.

- Adds JWT support to Swagger UI: Enables users to authorize requests using a *Bearer* token.
- Disables session-based auth: Prevents Swagger from prompting for login credentials via Django sessions.
- Improves developer experience: Makes it easy to test secured endpoints directly from the Swagger interface.

```python
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"',
        }

    },
    'USE_SESSION_AUTH': False,
}
```

###### REDOC_SETTINGS

`REDOC_SETTINGS` customizes how **ReDoc** renders OpenAPI documentation in the browser.

```python
REDOC_SETTINGS = {
   'LAZY_RENDERING': False,
   'HIDE_HOSTNAME': False,
   'EXPAND_RESPONSES': 'all',
   'PATH_IN_MIDDLE': False,
}
```

###### DRF_YASG_SETTINGS

`DRF_YASG_SETTINGS` enhances the usability of your auto-generated Swagger documentation by enabling deep linking.

- Enables anchor links for each endpoint and section in the Swagger UI.
- Allows users to bookmark or share direct URLs to specific parts of the API documentation.
- Improves navigation for large specs by making each operation individually addressable.

```python
DRF_YASG_SETTINGS = {
    'DEEP_LINKING': True,
}
```

##### drf_standardized_errors

> ℹ️ Create consistent, clean error messaging across the API. Just head over to `config/swagger.py` and define a custom `error_responses` dictionary. This allows centralized error formats—so contributors don’t have to reinvent the wheel for every view. Once the dictionary is set, simply reference it in views and viewsets to keep the Swagger docs sharp, readable, and standardized.

To activate centralized error handling across the API, plug `drf_standardized_errors` into the `REST_FRAMEWORK` dictionary.

This hands off all API exceptions to `drf_standardized_errors`, ensuring consistent, structured responses for every error—perfect for debugging, client-side handling, and contributor clarity.


```python
REST_FRAMEWORK = {
    # ...
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler"
}
```

Add the `DRF_STANDARDIZED_ERRORS` dictionary for:

- **Centralized Exception Handling**  
  Define exactly how exceptions are captured, filtered, and reported (yes, even to tools like Sentry). You can subclass the handler to fine-tune which errors get logged or ignored.

- **Consistent Error Formatting**  
  Customize the structure of your error responses with a formatter class that ensures every client-facing message is clean, predictable, and easy to parse.

- **Schema-Aware Error Responses**  
  Automatically generate OpenAPI 3-compliant error schemas for key status codes like `400`, `401`, `404`, and `500`. Nested fields, list indices, and dynamic dict keys are all handled with precision—no more guessing what `extra_data.42` means.

- **Debug Mode Flexibility**  
  Keep traceback visibility when `DEBUG=True`, or flip the switch to test standardized errors even during development.

- **Contributor-Friendly API Docs**  
  With clear `attr` naming conventions and schema suffixes, your docs stay readable and your serializers stay conflict-free—especially in complex, nested validation scenarios.

```python
DRF_STANDARDIZED_ERRORS = {
    # class responsible for handling the exceptions. Can be subclassed to change
    # which exceptions are handled by default, to update which exceptions are
    # reported to error monitoring tools (like Sentry), ...
    "EXCEPTION_HANDLER_CLASS": "drf_standardized_errors.handler.ExceptionHandler",
    # class responsible for generating error response output. Can be subclassed
    # to change the format of the error response.
    "EXCEPTION_FORMATTER_CLASS": "drf_standardized_errors.formatter.ExceptionFormatter",
    # enable the standardized errors when DEBUG=True for unhandled exceptions.
    # By default, this is set to False so you're able to view the traceback in
    # the terminal and get more information about the exception.
    "ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": False,
    # When a validation error is raised in a nested serializer, the 'attr' key
    # of the error response will look like:
    # {field}{NESTED_FIELD_SEPARATOR}{nested_field}
    # for example: 'shipping_address.zipcode'
    "NESTED_FIELD_SEPARATOR": ".",

    # The below settings are for OpenAPI 3 schema generation

    # ONLY the responses that correspond to these status codes will appear
    # in the API schema.
    "ALLOWED_ERROR_STATUS_CODES": [
        "400",
        "401",
        "403",
        "404",
        "405",
        "406",
        "415",
        "429",
        "500",
    ],

    # A mapping used to override the default serializers used to describe
    # the error response. The key is the status code and the value is a string
    # that represents the path to the serializer class that describes the
    # error response.
    "ERROR_SCHEMAS": None,

    # When there is a validation error in list serializers, the "attr" returned
    # will be sth like "0.email", "1.email", "2.email", ... So, to describe
    # the error codes linked to the same field in a list serializer, the field
    # will appear in the schema with the name "INDEX.email"
    "LIST_INDEX_IN_API_SCHEMA": "INDEX",

    # When there is a validation error in a DictField with the name "extra_data",
    # the "attr" returned will be sth like "extra_data.<key1>", "extra_data.<key2>",
    # "extra_data.<key3>", ... Since the keys of a DictField are not predetermined,
    # this setting is used as a common name to be used in the API schema. So, the
    # corresponding "attr" value for the previous example will be "extra_data.KEY"
    "DICT_KEY_IN_API_SCHEMA": "KEY",

    # should be unique to error components since it is used to identify error
    # components generated dynamically to exclude them from being processed by
    # the postprocessing hook. This avoids raising warnings for "code" and "attr"
    # which can have the same choices across multiple serializers.
    "ERROR_COMPONENT_NAME_SUFFIX": "ErrorComponent",
}
```

## 💬 Contributing

I welcome and appreciate all contributions—whether it's fixing a bug, improving documentation, or adding new features. If you have an idea for a significant change or enhancement, please open an issue first to start a conversation.

Once we’ve discussed your proposal, feel free to submit a pull request. Be sure to follow the coding standards and include relevant tests where applicable. I'm excited to collaborate and grow this project together!

## ⚖️ License

[![MIT License Badge](https://img.shields.io/badge/MIT-License-white?labelColor=goldenrod&logo=os&logoColor=white)](https://pdm.fming.dev)

This project is licensed under the MIT License.

You are free to:
- Use the code for personal or commercial projects
- Modify and distribute it
- Learn from it and build upon it

Just make sure to:
- Include the original license and copyright
- Avoid holding the original authors liable for any issue
