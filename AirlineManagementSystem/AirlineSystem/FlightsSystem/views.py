from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import *
import os
from django import forms
from django.conf import settings
from .forms import *


# Create the subdirectory for passport photos
# subdirectory = 'passport_photos'
# media_root = settings.MEDIA_ROOT
# upload_to = os.path.join(media_root, subdirectory)
# if not os.path.exists(upload_to):
#     os.makedirs(upload_to)


# Create your views here.

def ListofTickets(request):
    AllTickets = TicketsModel.objects.all()

    if (request.method == "POST"):
        # form implementaiton
        return render(request, "FlightsSystem/ListofTickets.html", {
            "allTickets": AllTickets,
            "status": "Data added",
            "AddTicketForm": AddaTicketForm(),
            "AddANotherTicketFomr": AddAnotherTicketForm(),
        })

    return render(request, "FlightsSystem/ListofTickets.html", {
        "allTickets": AllTickets,
        "AddTicketForm": AddaTicketForm()
    })


def anAirporstDetails(request, AirPort_ID):
    Airport = AirportsModel.objects.get(pk=AirPort_ID)
    return render(request, "FlightsSystem/anAirPortDetials.html", {
        "AirID": AirPort_ID,
        "Arrivals": Airport.arrivals.all(),
        "Departures": Airport.departures.all()
    })


def AllAirports(request):
    allAirports = AirportsModel.objects.all()
    return render(request, "FlightsSystem/AllAirports.html", {
        "all": allAirports
    })


def pDetails(request, Pid):
    passenger = PassengersModel.objects.get(pk=Pid)
    return render(request, "FlightsSystem/pDetails.html", {
        "Flights": passenger.flights.all(),
        "Passenger": passenger,
        "count": passenger.flights.count()

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
            # passport_number = Myform.cleaned_data['passportNumber']
            passport_image = Myform.cleaned_data['passport_image']
            flights = Myform.cleaned_data['ListOfAllFlights']
            passenger = PassengersModel(
                first=first_name,
                last=last_name,
                passportCountry=passport_country,
                # passportNumber=passport_number,
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
