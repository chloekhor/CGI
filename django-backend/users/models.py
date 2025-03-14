from django.db import models
from django.utils import timezone
import uuid  

class Users(models.Model):
    name = models.CharField(max_length=255) 
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=512, blank=True, null=True)  

    reset_token = models.CharField(max_length=255, blank=True, null=True)
    reset_token_expiry = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'users'

class History(models.Model):
    date = models.DateTimeField(auto_now_add=True)  # Auto stores creation timestamp
    target = models.JSONField()  # Stores JSON data for target
    result = models.JSONField()  # Stores JSON data for analysis result
    summary = models.TextField()  # Renamed from 'suggestion' (Stores recommendations/summary)
    fullAnalysis = models.JSONField()  # Newly added column for a more detailed analysis
    photo = models.CharField(max_length=255)  # Can store file path or URL
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='history')  # Fixed ForeignKey

    class Meta:
        db_table = 'history'  # Custom table name

    def __str__(self):
        return 
