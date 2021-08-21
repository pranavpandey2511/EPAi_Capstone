from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_no = models.CharField(max_length=12)