from django.db import models

class History(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    target = models.IntegerField()
    result = models.IntegerField()
    suggestion = models.TextField(blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'history'  # Ensure this matches your table name in MySQL