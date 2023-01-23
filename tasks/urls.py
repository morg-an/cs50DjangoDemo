from django.urls import path
from . import views

app_name = "tasks" #use to avoid namespace collision (e.g., url tasks:index)
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]