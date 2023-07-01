# pauliceia_tabelao

* Python versão 3.10

:: Terminal 1

- Criar enviroment

python -m venv pauliceia_env

- Ativar (no gitbash)
source pauliceia_env/Scripts/activate

- Instalações

pip install django

pip install psycopg2

:: Terminal 2

psql -U postgres

CREATE USER pauliceiaAdm WITH PASSWORD 'user123';

ALTER USER pauliceiaAdm WITH SUPERUSER;

:: Terminal 1 (bash)

django-admin startproject projeto_pauliceia

cd projeto_pauliceia

django-admin startapp "tabelaoapp"



settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'pauliceiaAdm',
        'PASSWORD': 'user123',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}


:: Terminal

python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser

tabadm
user@123


settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tabelaoapp',
]

--criar pasta static na pasta do app

STATIC_URL = 'restaurant/static/'

STATICFILES_DIRS = [
    "restaurant/static",
]

urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tabelaoapp.urls')),
]

<!-- <li><a href="{% url 'form_2' %}">Tabelão</a></li> -->
<!-- <li><a href="{% url 'layer' %}">Layers</a></li> -->   