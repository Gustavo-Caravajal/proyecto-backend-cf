from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100,null=False,unique=True)
    año_fundacion = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
