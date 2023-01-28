from django.shortcuts import render

from .models import Flight, Airport, Passenger

# Create your views here.
def index(request):
    return render(request, "wingCo/index.html",{
        "flights": Flight.objects.all(), 
        "airports": Airport.objects.all(),
        "passengers": Passenger.objects.all() 
    })