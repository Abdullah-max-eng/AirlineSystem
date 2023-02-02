from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import *
import os
from django.conf import settings


# Create the subdirectory for passport photos
subdirectory = 'passport_photos'
media_root = settings.MEDIA_ROOT
upload_to = os.path.join(media_root, subdirectory)
if not os.path.exists(upload_to):
    os.makedirs(upload_to)


# Create your views here.
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
