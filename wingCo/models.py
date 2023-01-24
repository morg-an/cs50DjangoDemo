from django.db import models

# https://docs.djangoproject.com/en/4.1/ref/models/fields/

# Create your models here.

class Airport(models.Model):
    city = models.CharField(max_length=64)
    airportCode = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.id}: {self.city} ({self.airportCode})"

class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    #cascade means coresponding flights would be deleted if the airport was deleted.
    #related name allows search in reverse direction (get all flights leaving from an origin)
    
    #destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.SmallIntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.first} {self.last}"

# in db.sqlite3, these tables are stored as wingCo_airport, wingCo_flight, and wingCo_passenger