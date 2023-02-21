from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100,null=False,unique=True)
    founded_year = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
