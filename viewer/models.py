from django.db import models

# Create your models here.
class Data(models.Model):
    loss = models.FloatField()
    val_acc = models.FloatField()
    tr_acc = models.FloatField()