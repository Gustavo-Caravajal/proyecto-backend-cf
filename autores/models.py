from django.db import models

class Autor(models.Model):
    nombre_completo = models.CharField(max_length=100,null=False,unique=True)
    año_nacimiento = models.IntegerField(null=False)
    pais_origen = models.CharField(max_length=50,null=False,unique=False)
    años_experiencia = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre_completo
