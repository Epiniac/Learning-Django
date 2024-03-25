from django.db import models

# Create your models here.
class Duck(models.Model):
    fileID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    food = models.CharField(max_length=10)
    credit = models.IntegerField()