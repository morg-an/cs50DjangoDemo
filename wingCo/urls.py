from django.urls import path
from . import views

app_name = "wingCo"
urlpatterns = [
    path("", views.index, name="index")
]