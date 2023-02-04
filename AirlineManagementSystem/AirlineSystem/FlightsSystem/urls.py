from django.urls import path
from . import views

app_name = "FlightsSystem"
urlpatterns = [
    path("", views.index, name="index"),
    path("AllFLights", views.AllFLights, name="AllFLights"),
    path("<int:flight_id>", views.aFlightDetails, name="aFlightDetails"),
    path("AddPassenger", views.addpassenger, name="addpassenger"),
    path("AllPassengers", views.AllPassengers, name="AllPassengers"),
    path("<int:Pid>/APassenger", views.pDetails, name="pDetails")
]
