from django.db import models

# Create your models here.


class AirportsModel(models.Model):
    code = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f" {self.city} ({self.code}), {self.country}"


class FlightModel(models.Model):
    origin = models.ForeignKey(
        AirportsModel, on_delete=models.CASCADE, max_length=30, related_name="departures")
    distination = models.ForeignKey(
        AirportsModel, on_delete=models.CASCADE, related_name="arrivals", max_length=30)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin}, {self.distination}, {self.duration}"


class PassengersModel(models.Model):
    first = models.CharField(max_length=10)
    last = models.CharField(max_length=20)
    passportCountry = models.CharField(max_length=30)
    passportNumber = models.IntegerField()
    passport_photo = models.ImageField(
        upload_to='passport_photos/', default='passenger_photos/default.jpg', null=True, blank=True)

    flights = models.ManyToManyField(
        FlightModel, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first}, {self.last}, {self.passportNumber}, {self.passportCountry}"


class AirlinesModel(models.Model):
    airlineName = models.CharField(max_length=30)
    flights = models.ForeignKey(
        FlightModel, on_delete=models.CASCADE, blank=True, null=True, related_name="airline")

    def __str__(self):
        return f"{self.airlineName}"


class TicketsModel(models.Model):
    TicketClassesChoice = [('Economy', 'Economy Class'),
                           ('Business', 'Business Class'), ("VIP", 'VIP Class')]
    ticketType = models.CharField(max_length=30, choices=TicketClassesChoice)
    passenger = models.OneToOneField(
        PassengersModel, on_delete=models.CASCADE, related_name="ticket")
    airline = models.ForeignKey(
        AirlinesModel, on_delete=models.CASCADE, related_name="tickets")
    flight = models.OneToOneField(
        FlightModel, null=True, on_delete=models.CASCADE, related_name="ticket")

    def __str__(self):
        return f"{self.ticketType}, {self.passenger}"
