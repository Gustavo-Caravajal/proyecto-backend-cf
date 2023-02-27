### Creación del entorno
- python -m venv env

### Activación del entorno
- env\Scripts\activate

### Instalación de django
- pip install django

### Crear proyecto
- django-admin startproject biblioteca .

### Correr migraciones
- python manage.py migrate

### Crear migraciones (en caso que se necesite)
- python manage.py makemigrations

### Correr servidor
- python manage.py runserver

### Para crear un super usuario y acceder al admin:

- python manage.py createsuperuser 

### Para conectar a la base de datos:

- pip install psycopg2-binary

### Para instalar django rest framework

- pip install djangorestframework

### Para instalar todas las dependencias del proyecto

- pip install -r requirements.txt

### Para generar el archivo requirements.txt

- pip freeze > requirements.txt