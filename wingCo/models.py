from django.db import models

# https://docs.djangoproject.com/en/4.1/ref/models/fields/

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.SmallIntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.first} {self.last}"

class Airport(models.Model):
    city = models.CharField(max_length=64)
    airportCode = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.id}: {self.city} ({self.airportCode})"

# in db.sqlite3, these tables are stored as wingCo_airport, wingCo_flight, and wingCo_passenger