from django.contrib import admin

# Registering models here.
from .models import Client, Wedding, WeddingService, Service

admin.site.register(Client)
admin.site.register(Wedding)
admin.site.register(Service)
admin.site.register(WeddingService)