from django.test import TestCase, Client
from django.db.models import Max
from .models import FlightModel, PassengersModel, AirportsModel
# Create your tests here.


class FlightsTest(TestCase):
    def setUp(self):  # this will create a copy a database with dummy data as below
        # Create Airports
        a1 = AirportsModel.objects.create(
            code="AAA", city="City A", country="Country A")
        a2 = AirportsModel.objects.create(
            code="BBB", city="City B", country="Country B")

        # Create a flight
        FlightModel.objects.create(origin=a1, distination=a2, duration=100)
        FlightModel.objects.create(origin=a1, distination=a1, duration=200)
        FlightModel.objects.create(origin=a1, distination=a2, duration=-100)

    def test_departures_count(self):
        a = AirportsModel.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = AirportsModel.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)

    def test_is_valid_Flight(self):
        a1 = AirportsModel.objects.get(code="AAA")
        a2 = AirportsModel.objects.get(code="BBB")
        f = FlightModel.objects.get(
            origin=a1, distination=a2, duration=-100)

        self.assertFalse(f.is_valid_flight())

    def test_AllFlights(self):
        c = Client()
        response = c.get("/AllFLights/")
        # will be 302 since it is not giving the allflights page directly but login page
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(response.context['AllFlights'].count(), 3)

    def test_flightid(self):
        c = Client()
        response = c.get("/1/")
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(response.context['countPassenger'], 0)
