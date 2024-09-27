from django.db import models

# Client Model

from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Wedding(models.Model):
    bride = models.ForeignKey(Client, related_name="bride_wedding", on_delete=models.CASCADE)
    groom = models.ForeignKey(Client, related_name='groom_wedding', on_delete=models.CASCADE)
    wedding_day = models.DateField(blank=True, null=True)
    weekend_only = models.BooleanField(default=False)
    min_guests = models.IntegerField()
    max_guests = models.IntegerField()
    foreign_guests = models.IntegerField(blank=True, null=True) 
    foreign_languages = models.CharField(max_length=200, blank=True, null=True)
    program_languages = models.CharField(max_length=200, blank=True, null=True)
    accommodation_guests = models.IntegerField(blank=True, null=True)  # Made optional
    transport_airport = models.BooleanField(default=False)
    transport_after = models.BooleanField(default=False)
    wedding_location = models.CharField(max_length=200, blank=True) 
    region = models.CharField(max_length=100, blank=True) 
    indoor_outdoor = models.CharField(
        max_length=100,
        choices=[
            ('indoor', 'Indoor'),
            ('outdoor', 'Outdoor'),
            ('any', 'No Preference'),
        ],
        blank=True  # Made optional
    )
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    homemade_alcohol = models.BooleanField(default=False)
    homemade_food = models.BooleanField(default=False)
    total_service_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.bride.first_namename} & {self.groom.first_name}'s Wedding"
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class WeddingService(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    chosen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service.name} for {self.wedding}"

