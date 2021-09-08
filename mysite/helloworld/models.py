from django.db import models

# Create your models here.

class Age(models.Model):
    value = models.IntegerField(default=0)

class MyFirstModel(models.Model):
    name = models.CharField(max_length=45)
    number = models.IntegerField(default=0)
    age = models.ForeignKey(to=Age, default=0, on_delete=models.SET_DEFAULT)