from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Make sure password is store after Hashed
        if not self.password_hash.startswith('pbkdf2_sha256$'):
            self.password_hash = make_password(self.password_hash)
            #pbkdf2_sha256 is using PBKDF2 + SHA256 hashing method to hashing
            #default 600'000 times of hashing
            #Django default random generate 16byte salt, and +salt before hashing
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

