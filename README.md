# Python API Demo

![GitHub Tag](https://img.shields.io/github/v/tag/kimberly-emerson/python-api-django-postgresql?include_prereleases&style=flat-square&logo=github&labelColor=black&color=%2300c950)

---

<div align="center">

[![Django Badge](https://img.shields.io/badge/django-5.2.5-4?logo=django&style=flat-square&labelColor=%23092E20&color=white)](https://www.djangoproject.com/) [![Django REST Framework Badge](https://img.shields.io/badge/django--rest--framework-3.16.1-blue?style=flat-square&labelColor=black&logo=django&logoColor=white&color=white)](https://www.django-rest-framework.org/) [![Swagger Badge](https://img.shields.io/badge/-Swagger-%23Clojure?style=flat-square&logo=swagger&logoColor=white)](https://drf-yasg.readthedocs.io/en/stable/readme.html) [![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-3.17-316192?logo=postgresql&labelColor=blue&color=white&logoColor=white)](https://www.postgresql.org/) [![PDM](https://img.shields.io/badge/PDM-managed-white?labelColor=mediumpurple&logo=pdm&logoColor=white)](https://pdm.fming.dev)
</div>

This demo project features clean, modular RESTful services, robust data validation, seamless database integration, and a structure designed for easy expansion and maintainability.

## 📅 Data

The data for this API is supplied by a PostgreSQL database created using the [python-etl-sql-postgres](https://github.com/kimberly-emerson/python-etl-sql-postgres) repo. It performs a full ETL (Extract, Transform, Load) pipeline using Python to migrate data from the **AdventureWorks2022** SQL Server database to the **AW_Sales** PostgreSQL database.

## #️⃣ Technology Stack

|Layer|Technology|
|---|---|
|Language|[![Python Badge](https://img.shields.io/badge/python-3.13.7-3670A0?style=flat-square&labelColor=blue&logo=python&logoColor=white&color=white)](https://www.python.org/)|
|Web Framework|[![Django Badge](https://img.shields.io/badge/django-5.2.5-4?logo=django&style=flat-square&labelColor=%23092E20&color=white)](https://www.djangoproject.com/)|
|REST Framework|[![Django REST Framework Badge](https://img.shields.io/badge/django--rest--framework-3.16.1-blue?style=flat-square&labelColor=black&logo=django&logoColor=white&color=white)](https://www.django-rest-framework.org/)|
|Database|[![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-3.17-316192?logo=postgresql&labelColor=blue&color=white&logoColor=white)](https://www.postgresql.org/)|
|Authentication|<img src="https://img.shields.io/badge/JWT-Auth-orange.svg" alt="JWT Auth">|
|Testing||
|Documentation|[![Swagger Badge](https://img.shields.io/badge/-Swagger-%23Clojure?style=flat-square&logo=swagger&logoColor=white)](https://drf-yasg.readthedocs.io/en/stable/readme.html)|
|Dependency Management|[![PDM](https://img.shields.io/badge/PDM-managed-white?labelColor=mediumpurple&logo=pdm&logoColor=white)](https://pdm.fming.dev)|
|Environment|[![DotEnv Badge](https://img.shields.io/badge/16.0.1-0?label=dotenv&style=flat-square&logo=dotenv&labelColor=black&logoColor=white&color=white)](https://pypi.org/project/python-dotenv/)|

## ✅ Project Setup Instructions

### Initialize and Create Django Project

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
gh repo edit --add-topic postgresql
gh repo edit --add-topic jwt-auth
gh repo edit --add-topic pdm
```

### GitHub Project Setup

```powershell
# create project
gh project create --owner kimberly-emerson --title python-api-django-postgresql
# create issue
gh issue create --title "Project Setup" --project "python-api-django-postgresql" --label 'enhancement' --assignee '@me'
```

### 📦 Install Dependencies

```powershell
pdm add djangorestframework
pdm add djangorestframework-simplejwt
pdm add drf-yasg[validation]
pdm add psycopg2
pdm add python-dotenv
pdm add django-cors-headers
pdm add django-filter
pdm add python-decouple
```

### Create Super User

```powershell
python manage.py createsuperuser --username username --email email
```

### 📁 Create Files and Folders

ℹ️ The commands used to create the files and folders are PowerShell [aliases](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-alias?view=powershell-7.5).

❗ Execute the commands in the project's root folder -- `python-api-django-postgresql`.

#### Folders

```powershell
md api/config
md api/models
md api/schemas
md api/templates
md api/views
md utils
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
ni api/templates/base.html
ni api/views/group_viewset.py
ni api/views/user_viewset.py
ni logs
ni tests
ni .env
ni .env.example
```

### Project Settings

#### .env Files

The .env files (.env and .env.example) should contain the following environment variables.

❗Change the DB_NAME, DB_USERNAME, and DB_PASSWORD environment variables for the target PostgreSQL database.

```yaml
# Application Environment
APP_ENV=local
APP_DEBUG=true
APP_URL=http://localhost:3000

# Database Configuration
DB_CONNECTION=postgresql
DB_HOSTNAME=localhost
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=database
DB_USERNAME=username
DB_PASSWORD=password

# Directory Path
APP_DIR=/api
CORE_DIR=/core
LOGS_DIR=/logs

# Authentication
SECRET_KEY=key
```

#### core/settings.py

##### Add Imports

```python
from decouple import config
```

##### Secret Key

```python
SECRET_KEY = config('SECRET_KEY')
```

##### Allowed Hosts

```python
ALLOWED_HOSTS = ['*']
```

##### Installed Apps

```python
INSTALLED_APPS = [
    # ...
    # third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    # project apps
    "api",
]
```

##### Root URL Configuration

```python
ROOT_URLCONF = "core.urls"
```

##### Database

Modify the Django `core/settings.py` file to configure the PostgreSQL database settings. Replace the existing configuration.

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

##### drf_yasg

Add `REST_FRAMEWORK`, `SWAGGER_SETTINGS`, `REDOC_SETTINGS` to configure `rest_framework`and `drf-yasg`.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
    ),
}

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

REDOC_SETTINGS = {
   'LAZY_RENDERING': False,
}

DRF_YASG_SETTINGS = {
    'DEEP_LINKING': True,
}
```

## 💬 Contributing

I welcome and appreciate all contributions—whether it's fixing a bug, improving documentation, or adding new features. If you have an idea for a significant change or enhancement, please open an issue first to start a conversation.

Once we’ve discussed your proposal, feel free to submit a pull request. Be sure to follow the coding standards and include relevant tests where applicable. I'm excited to collaborate and grow this project together!

## ⚖️ License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/mit)

This project is licensed under the MIT License.

You are free to:
- Use the code for personal or commercial projects
- Modify and distribute it
- Learn from it and build upon it

Just make sure to:
- Include the original license and copyright
- Avoid holding the original authors liable for any issue
