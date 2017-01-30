#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Fruit2(models.Model):
    name = models.CharField(max_length=100,primary_key=True)

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)