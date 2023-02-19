from django import forms
from .models import *


class AddPassengerForm(forms.Form):
    # if we want to make a list to user to select from in django for, we can do the below but we will pass it in the template directrly
    AllFLights = FlightModel.objects.all()
    flight_choices = [(flight.id, "{} to {} Flight iD = {}".format(
        flight.origin, flight.distination, flight.id)) for flight in AllFLights]
    AllCountries = [
        ('AF', 'Afghanistan'),
        ('AL', 'Albania'),
        ('DZ', 'Algeria'),
        ('AS', 'American Samoa'),
        ('AD', 'Andorra'),
        ('AO', 'Angola'),
        ('AI', 'Anguilla'),
        ('AQ', 'Antarctica'),
        ('AG', 'Antigua and Barbuda'),
        ('AR', 'Argentina'),
        ('AM', 'Armenia'),
        ('AW', 'Aruba'),
        ('AU', 'Australia'),
        ('AT', 'Austria'),
        ('AZ', 'Azerbaijan'),
        ('BS', 'Bahamas'),
        ('BH', 'Bahrain'),
        ('BD', 'Bangladesh'),
        ('BB', 'Barbados'),
        ('BY', 'Belarus'),
        ('BE', 'Belgium'),
        ('BZ', 'Belize'),
        ('BJ', 'Benin'),
        ('BM', 'Bermuda'),
        ('BT', 'Bhutan'),
        ('BO', 'Bolivia'),
        ('BA', 'Bosnia and Herzegovina'),
        ('BW', 'Botswana'),
        ('BV', 'Bouvet Island'),
        ('BR', 'Brazil'),
        ('IO', 'British Indian Ocean Territory'),
        ('BN', 'Brunei Darussalam'),
        ('BG', 'Bulgaria'),
        ('BF', 'Burkina Faso'),
        ('BI', 'Burundi'),
        ('KH', 'Cambodia'),
        ('CM', 'Cameroon'),
        ('CA', 'Canada'),
        ('CV', 'Cape Verde'),
        ('KY', 'Cayman Islands'),
        ('CF', 'Central African Republic'),
        ('TD', 'Chad'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CX', 'Christmas Island'),
        ('CC', 'Cocos (Keeling) Islands'),
        ('CO', 'Colombia'),
        ('KM', 'Comoros'),
        ('CG', 'Congo'),
        ('CD', 'Congo, the Democratic Republic of the'),
        ('CK', 'Cook Islands'),
        ('CR', 'Costa Rica'),
        ('CI', "Cote D'Ivoire"),
        ('HR', 'Croatia'),
        ('CU', 'Cuba'),
        ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'),
        ('DK', 'Denmark'),
        ('DJ', 'Djibouti'),
        ('DM', 'Dominica'),
        ('DO', 'Dominican Republic'),
        ('EC', 'Ecuador'),
        ('EG', 'Egypt'),
        ('SV', 'El Salvador'),
        ('GQ', 'Equatorial Guinea'),
        ('ER', 'Eritrea'),
        ('EE', 'Estonia'),
        ('ET', 'Ethiopia'),
        ('FK', 'Falkland Islands (Malvinas)'),
        ('FO', 'Faroe Islands')]
    Firstname = forms.CharField(label='Your Name', max_length=100)
    LastName = forms.CharField(label='Last Name', max_length=100)
    passportCountry = forms.ChoiceField(choices=AllCountries)
    passport_image = forms.ImageField(label='Passport Image')
    # This below code will display a list of all flight, Above code is used to display select using django
    ListOfAllFlights = forms.MultipleChoiceField(
        choices=flight_choices, widget=forms.CheckboxSelectMultiple, label="List of All FLights")


class AddaTicketForm(forms.Form):
    AllFLights = FlightModel.objects.all()
    all_FLights_Choices = [(flight.id, " {} --- to ---> {} ID({}) ".format(
        flight.origin, flight.distination, flight.id)) for flight in AllFLights]

    ticket_types = TicketsModel.TicketClassesChoice
    passenger_choices = [(passenger.id, f"{passenger.first}  {passenger.last}  ({passenger.id})")
                         for passenger in PassengersModel.objects.filter(ticket__isnull=True)]
    airline_choices = [(airline.id, airline.airlineName)
                       for airline in AirlinesModel.objects.all()]
    ticket_type = forms.ChoiceField(choices=ticket_types)
    passenger = forms.ChoiceField(choices=passenger_choices)
    airlines = forms.ChoiceField(choices=airline_choices)
    Flight_for_this_Ticket = forms.ChoiceField(choices=all_FLights_Choices)


class AddAnotherTicketForm(forms.Form):
    AllFLights = FlightModel.objects.all()
    all_FLights_Choices = [(flight.id, " {} --- to ---> {} ID({}) ".format(
        flight.origin, flight.distination, flight.id)) for flight in AllFLights]

    ticket_types = TicketsModel.TicketClassesChoice
    passenger_choices = [(passenger.id, f"{passenger.first}  {passenger.last}  ({passenger.id})")
                         for passenger in PassengersModel.objects.all()]
    airline_choices = [(airline.id, airline.airlineName)
                       for airline in AirlinesModel.objects.all()]
    ticket_type = forms.ChoiceField(choices=ticket_types)
    passenger = forms.ChoiceField(choices=passenger_choices)
    airline = forms.ChoiceField(choices=airline_choices)
    Flight_for_this_Ticket = forms.ChoiceField(choices=all_FLights_Choices)
