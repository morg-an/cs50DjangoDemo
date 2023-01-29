from django.shortcuts import render

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