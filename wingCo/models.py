from django.db import models

# https://docs.djangoproject.com/en/4.1/ref/models/fields/

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.SmallIntegerField()

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

class Airport(models.Model):
    city = models.CharField(max_length=64)
    airportCode = models.CharField(max_length=3)