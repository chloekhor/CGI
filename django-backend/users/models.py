from django.db import models
import uuid  

class Users(models.Model):
    name = models.CharField(max_length=255) 
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=512, blank=True, null=True)  


    class Meta:
        db_table = 'users'
