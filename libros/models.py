from django.db import models
from editoriales.models import Publisher
from autores.models import Author
from generos.models import Genre

class Book(models.Model):
    title = models.CharField(max_length=100,null=False,unique=False)
    publication_year = models.IntegerField(null=False)
    n_pages = models.IntegerField(null=False)
    languaje = models.CharField(max_length=100,null=False,unique=False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='libros_autor')
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,related_name='libros_editorial')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class BookV4(models.Model):
    title = models.CharField(max_length=100,null=False,unique=False)
    publication_year = models.IntegerField(null=False)
    n_pages = models.IntegerField(null=False)
    languaje = models.CharField(max_length=100,null=False,unique=False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='libros_autor_v4')
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,related_name='libros_editorial_v4')
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name='libros_genero')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title