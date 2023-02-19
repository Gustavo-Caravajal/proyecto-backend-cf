from django.db import models
from editoriales.models import Editorial
from autores.models import Autor
from generos.models import Genero

class Libro(models.Model):
    titulo = models.CharField(max_length=100,null=False,unique=False)
    año_publicacion = models.IntegerField(null=False)
    n_paginas = models.IntegerField(null=False)
    idioma = models.CharField(max_length=100,null=False,unique=False)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,related_name='libros_autor')
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE,related_name='libros_editorial')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo

class Libro_v4(models.Model):
    titulo = models.CharField(max_length=100,null=False,unique=False)
    año_publicacion = models.IntegerField(null=False)
    n_paginas = models.IntegerField(null=False)
    idioma = models.CharField(max_length=100,null=False,unique=False)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,related_name='libros_autor_v4')
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE,related_name='libros_editorial_v4')
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE,related_name='libros_genero')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo