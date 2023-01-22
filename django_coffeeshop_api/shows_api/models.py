from django.db import models

# Create your models here.
class Show(models.Model):
    event = models.CharField(max_length=32)
    date = models.CharField(max_length=32)
    price = models.IntegerField()
