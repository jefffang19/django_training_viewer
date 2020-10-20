from django.db import models

# Create your models here.
class Data(models.Model):
    loss = models.FloatField()
    acc = models.FloatField()