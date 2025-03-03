# from django.db import models


# class Users(models.Model):
#     id = models.CharField(max_length=36, primary_key=True, editable=False)
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     photo_url = models.TextField()

# class History(models.Model):
#     date = models.DateTimeField()
#     target = models.IntegerField()
#     result = models.IntegerField()
#     suggestion = models.TextField()
#     photo = models.CharField(max_length=255)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'history'  # Ensure this matches your table name in MySQL