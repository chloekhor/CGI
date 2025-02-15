from django.db import models

class History(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    target = models.IntegerField()
    result = models.IntegerField()
    suggestion = models.TextField(blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'history'  # Ensure this matches your table name in MySQL

class Profile(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Hashed password recommended
    profile_picture = models.CharField(max_length=255, blank=True, null=True)  # Store image path

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'profile'