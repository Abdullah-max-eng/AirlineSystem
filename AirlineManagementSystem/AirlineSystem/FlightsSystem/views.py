from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import *
import os
from django import forms
from django.conf import settings
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# These are new changes


def LoginPage(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            # return redirect('admin:index')
            return redirect('FlightsSystem:index')
        else:
            messages.info(request, "Username or password in incorrect")

    return render(request, 'FlightsSystem/Login.html')


def LogoutUser(request):
    logout(request)
    return redirect('FlightsSystem:Login')


def RegistrationPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request, f"Account was created for {user}")
            return redirect('FlightsSystem:Login')

    context = {'form': form}
    return render(request, 'FlightsSystem/Register.html', context)


@login_required(login_url='FlightsSystem:Login')
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


@login_required(login_url='FlightsSystem:Login')
def anAirporstDetails(request, AirPort_ID):
    Airport = AirportsModel.objects.get(pk=AirPort_ID)
    return render(request, "FlightsSystem/anAirPortDetials.html", {
        "AirID": AirPort_ID,
        "Arrivals": Airport.arrivals.all(),
        "Departures": Airport.departures.all()
    })


@login_required(login_url='FlightsSystem:Login')
def AllAirports(request):
    allAirports = AirportsModel.objects.all()
    return render(request, "FlightsSystem/AllAirports.html", {
        "all": allAirports
    })


@login_required(login_url='FlightsSystem:Login')
def pDetails(request, Pid):
    passenger = PassengersModel.objects.get(pk=Pid)
    return render(request, "FlightsSystem/pDetails.html", {
        "Flights": passenger.flights.all(),
        "Passenger": passenger,
        "count": passenger.flights.count()

    })


@login_required(login_url='FlightsSystem:Login')
def AllPassengers(request):
    allPassengers = PassengersModel.objects.all()
    count = allPassengers.count()
    return render(request, "FlightsSystem/AllPassengers.html", {
        "allPassengers": allPassengers,
        "count": count
    })


@login_required(login_url='FlightsSystem:Login')
def index(httprequest):
    return render(httprequest, 'FlightsSystem/index.html')


# @login_required(login_url='FlightsSystem:Login')
def AllFLights(httprequest):
    AllFlights = FlightModel.objects.all()
    return render(httprequest, 'FlightsSystem/AllFlights.html', {
        "AllFlights": AllFlights
    })


# @login_required(login_url='FlightsSystem:Login')
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


@login_required(login_url='FlightsSystem:Login')
def anAirlineDetails(request, AirNum):
    airline = AirlinesModel.objects.get(pk=AirNum)
    return render(request, 'FlightsSystem/anAirlineDetails.html', {
        "airline": airline,
        "flights": airline.flights

    })


@login_required(login_url='FlightsSystem:Login')
def ListofAirlines(request):
    if (request.method == "POST"):
        pass  # Not implemented yet
    else:
        return render(request, "FlightsSystem/ListofAirlines.html", {
            "AllAilines": AirlinesModel.objects.all()
        })


@login_required(login_url='FlightsSystem:Login')
def addpassenger(request):
    if request.method == "POST":
        Myform = AddPassengerForm(request.POST, request.FILES)
        if Myform.is_valid():
            first_name = Myform.cleaned_data['Firstname']
            last_name = Myform.cleaned_data['LastName']
            passport_country = Myform.cleaned_data['passportCountry']
            passport_image = Myform.cleaned_data['passport_image']
            flights = Myform.cleaned_data['ListOfAllFlights']
            passenger = PassengersModel(
                first=first_name,
                last=last_name,
                passportCountry=passport_country,
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
