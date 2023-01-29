from django.urls import path
from . import views

app_name = "wingCo"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("airport/<int:airport_id>", views.airport, name="airport")
]