from django.db import models

class Author(models.Model):
    full_name  = models.CharField(max_length=100,null=False,unique=True)
    birth_year = models.IntegerField(null=False)
    country_origin  = models.CharField(max_length=50,null=False,unique=False)
    years_experience = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
