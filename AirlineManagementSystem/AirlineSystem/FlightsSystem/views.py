from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import *
import os
from django import forms
from django.conf import settings
from .forms import *


# Create the subdirectory for passport photos
subdirectory = 'passport_photos'
media_root = settings.MEDIA_ROOT
upload_to = os.path.join(media_root, subdirectory)
if not os.path.exists(upload_to):
    os.makedirs(upload_to)


# Create your views here.

def pDetails(request, Pid):
    return render(request, "FlightsSystem/pDetails.html", {
        "passengerID": Pid

    })


def AllPassengers(request):
    allPassengers = PassengersModel.objects.all()
    count = allPassengers.count()
    return render(request, "FlightsSystem/AllPassengers.html", {
        "allPassengers": allPassengers,
        "count": count
    })


def index(httprequest):
    return render(httprequest, 'FlightsSystem/index.html')


def AllFLights(httprequest):
    AllFlights = FlightModel.objects.all()
    return render(httprequest, 'FlightsSystem/AllFlights.html', {
        "AllFlights": AllFlights
    })


def aFlightDetails(httprequest, flight_id):
    Flight = FlightModel.objects.get(pk=flight_id)
    if Flight:
        passengers = Flight.passengers.all()
        countpassenger = passengers.count()

        return render(httprequest, 'FlightsSystem/aFlightDetails.html', {
            "flight": Flight,
            "passengersInThisFlight": passengers,
            "countPassenger": countpassenger,
        })
    else:
        # Handle the case where the flight with the given flight_id does not exist
        return HttpResponseNotFound('Flight not found')


def addpassenger(request):
    if request.method == "POST":
        Myform = AddPassengerForm(request.POST, request.FILES)
        if Myform.is_valid():
            first_name = Myform.cleaned_data['Firstname']
            last_name = Myform.cleaned_data['LastName']
            passport_country = Myform.cleaned_data['passportCountry']
            passport_number = Myform.cleaned_data['passportNumber']
            passport_image = Myform.cleaned_data['passport_image']
            flights = Myform.cleaned_data['ListOfAllFlights']
            passenger = PassengersModel(
                first=first_name,
                last=last_name,
                passportCountry=passport_country,
                passportNumber=passport_number,
                passport_photo=passport_image
            )
            passenger.save()
            passenger.flights.set(flights)
            return render(request, "FlightsSystem/addpassenger.html", {
                "form": AddPassengerForm(),
                "info": "Data Added"
            })
        else:
            return render(request, "FlightsSystem/addpassenger.html", {
                "form": Myform,
                "errors": Myform.errors
            })
    newform = AddPassengerForm()
    return render(request, "FlightsSystem/addpassenger.html", {
        "form": newform,
        "info": "First made Form"
    })
