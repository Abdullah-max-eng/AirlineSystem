from django.contrib import admin
from .models import *


class AirportAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "city", "country")


# Register your models here.
admin.site.register(FlightModel)
admin.site.register(AirportsModel, AirportAdmin)
admin.site.register(AirlinesModel)
admin.site.register(PassengersModel)
admin.site.register(TicketsModel)
