from django.urls import path
from . import views
from django.contrib import admin

app_name = "FlightsSystem"
urlpatterns = [
    path("", views.index, name="index"),
    path("RegistrationPage/", views.RegistrationPage, name="RegistrationPage"),
    path("Logout/", views.LogoutUser, name="LogoutUser"),
    path("Login/", views.LoginPage, name="Login"),
    path("AllFLights", views.AllFLights, name="AllFLights"),
    path("<int:flight_id>", views.aFlightDetails, name="aFlightDetails"),
    path("AddPassenger", views.addpassenger, name="addpassenger"),
    path("AllPassengers", views.AllPassengers, name="AllPassengers"),
    path("<int:Pid>/a_Passenger", views.pDetails, name="pDetails"),
    path("AllAirports", views.AllAirports, name="AllAirports"),
    path("anAirlineDetails/<int:AirNum>",
         views.anAirlineDetails, name="anAirlineDetails"),
    path("ListofAirlines",
         views.ListofAirlines, name="ListofAirlines"),
    path("<int:AirPort_ID>/AirPortDetails",
         views.anAirporstDetails, name="anAirportDetial"),
    path("ListOfTickets",
         views.ListofTickets, name="ListofTickets")
]
