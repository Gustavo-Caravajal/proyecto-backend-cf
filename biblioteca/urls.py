"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/authors',include('autores.urls')),
    path('api/v2/authors',include('autores.urls')),
    path('api/v2/publishers',include('editoriales.urls')),
    path('api/v3/authors',include('autores.urls')),
    path('api/v3/publishers',include('editoriales.urls')),
    path('api/v3/books',include('libros.urls')),
    path('api/v4/authors',include('autores.urls')),
    path('api/v4/publishers',include('editoriales.urls')),
    path('api/v4/books',include('libros.Api.v4.urls')),
    path('api/v4/genres',include('generos.urls')),
]
