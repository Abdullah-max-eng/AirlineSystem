from django.urls import path
from . import views

app_name = "FlightsSystem"
urlpatterns = [
    path("", views.index, name="index")
]
