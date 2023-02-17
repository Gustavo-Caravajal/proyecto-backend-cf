from django.db import models
from editoriales.models import Editorial
from autores.models import Autor


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