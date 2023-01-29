from django.shortcuts import render
from django.http import HttpResponseRedirect
# reverse takes the name of a view in urls.py and gets the path - helpful to avoid hardcoding urls
from django.urls import reverse

from .models import Flight, Airport, Passenger

# Create your views here.
def index(request):
    return render(request, "wingCo/index.html",{
        "flights": Flight.objects.all(), 
        "airports": Airport.objects.all(),
        "passengers": Passenger.objects.all() 
    })

def flight(request, flight_id):
    #can use pk for primary key (or id also works)
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "wingCo/flight.html", {
        "flight": flight,
        #flight.passengers works becuase of the related name in models.py
        "passengers": flight.passengers.all()
    })

def airport(request, airport_id):
    airport = Airport.objects.get(pk = airport_id)
    return render(request, "wingCo/airport.html", {
        "airport": airport,
    })

def book(request, passenger_id):
    passenger = Passenger.objects.get(pk = passenger_id)
    if request.method == "POST":
        flight = Flight.objects.get(pk=int(request.POST["flight"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("wingCo:flight", args=(flight.id,)))
    elif request.method == 'GET':
        flights = Flight.objects.all()
        return render(request, "wingCo/book.html", {
            "passenger": passenger,
            "flights": flights        
        })