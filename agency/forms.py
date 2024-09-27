from django import forms
from .models import Client, Wedding, WeddingService, Service

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone', 'email']
        labels = {
            'first_name': 'Име / First Name',
            'last_name': 'Фамилно име / Last Name',
            'phone': 'Телефон / Phone',
            'email': 'Имейл / Email',
        }


class WeddingForm(forms.ModelForm):
    class Meta:
        model = Wedding
        fields = [
            'wedding_day',
            'weekend_only', 'min_guests', 'max_guests', 'foreign_guests', 'foreign_languages', 
            'program_languages', 'accommodation_guests', 'transport_airport', 'transport_after',
            'wedding_location', 'region', 'indoor_outdoor', 'budget', 'homemade_alcohol', 'homemade_food'
        ]
        labels = {
            'wedding_day': 'Дата на сватбата във формат YYYY-MM-DD / Wedding day in the format YYYY-MM-DD',
            'weekend_only': 'Само през уикенда ли може да е сватбата или може и през седмицата? / Do you only want a weekend wedding or during the week is OK too?',
            'min_guests': 'Приблизителен минимален брой гости / Approxiamte min number of guests', 
            'max_guests': 'Приблизителен максимален брой гости / Approxiamte max number of guests', 
            'foreign_guests': 'Ще има ли чуждестранни гости? / Will there be foreign guests?', 
            'foreign_languages': 'Какви чуждестранни езици ще се говорят на сватбата? / What foreign languages will be spoken at the wedding?', 
            'program_languages': 'На какви езици трябва да бъде програмата вечерта? / What languages should the program for the wedding party be at?', 
            'accommodation_guests': 'Ще има ли настаняване на гости? / Will guests need accomodation? ', 
            'transport_airport': 'Ще има ли нужда от транспорт от летището до сватбата? / Will transportation of guests to the wedding be needed?', 
            'transport_after': 'Ще има ли нужда от транспорт след сватбата? / Will transportation be needed after the wedding? ',
            'wedding_location': 'Имате ли избрана локация на сватбата? Ако да, коя? / Do you have a chosen wedding location? If yes, which is it?', 
            'region': 'Ако нямате избрана локация на сватбата, в кои региони на България бихте искали да препоръчаме ресторанти и зали? / If you do not have a chosen wedding venue, which regions of Bulgaria would you like us to recommend resaurants in?', 
            'indoor_outdoor': 'Сватбеното парти на открито ли искате да бъде или на закрито? / Do you want an outdoor or indoor wedding party?', 
            'budget': 'Имате ли определен сватбен бюджет, с които трябва да се съобразим? Ако да, посочете стойността му в лева, ако не, оставете празно. / Do you have a sample wedding budget for the whole wedding that we should have in mind? If yes, write the budget in Bulgarian levas, if not, leave the field empty.', 
            'homemade_alcohol': 'Държите ли да се вкара домашен алкохол на сватбата за консумация на гостите, например, ракия на роднина? / Do you insist on using a homemade alcohol for the wedding, for example, the homemade rakia of a relative? ', 
            'homemade_food': 'Държите ли да има внесена домашна храна на сватбата, например, питка от някои роднина, торта или друго? / Do you insist on having a homemade food at the wedding like a pitka bread made by a relative, a cake or something else? '
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = WeddingService
        fields = ['service', 'chosen']

class ServiceSelectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        services = kwargs.pop('services')
        super(ServiceSelectionForm, self).__init__(*args, **kwargs)
        
        for service in services:
            self.fields[f'service_{service.id}'] = forms.BooleanField(
                label=service.name, required=False
            )