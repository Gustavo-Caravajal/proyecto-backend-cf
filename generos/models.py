from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre =  models.CharField(max_length=100,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre