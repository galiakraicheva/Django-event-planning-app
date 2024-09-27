from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Client
from .forms import ServiceSelectionForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'agency/client_list.html', {'clients': clients})

from django.shortcuts import render, redirect
from .forms import ClientForm, WeddingForm, ServiceForm
from .models import Wedding, Service, WeddingService

#First meeting

def first_meeting(request):
    if request.method == 'POST':
        bride_form = ClientForm(request.POST, prefix='bride')
        groom_form = ClientForm(request.POST, prefix='groom')
        wedding_form = WeddingForm(request.POST)

        if bride_form.is_valid() and groom_form.is_valid() and wedding_form.is_valid():
            bride = bride_form.save()
            groom = groom_form.save()
            wedding = wedding_form.save(commit=False)
            wedding.bride = bride
            wedding.groom = groom
            wedding.save()

            return redirect('select_services', wedding_id=wedding.id)
    else:
        bride_form = ClientForm(prefix='bride')
        groom_form = ClientForm(prefix='groom')
        wedding_form = WeddingForm()

    return render(request, 'agency/first_meeting.html', {
        'bride_form': bride_form,
        'groom_form': groom_form,
        'wedding_form': wedding_form,
    })

def select_services(request, wedding_id):
    wedding = Wedding.objects.get(id=wedding_id)
    services = Service.objects.all()

    if request.method == 'POST':
        # Process form submission
        selected_services = []
        total_price = 0
        for service in services:
            if f'service_{service.id}' in request.POST:
                selected_services.append(service)
                total_price += service.price
                # Save or update the WeddingService instance
                WeddingService.objects.update_or_create(
                    wedding=wedding,
                    service=service,
                    defaults={'chosen': True}
                )
            else:
                # If the service was not selected, ensure it's marked as not chosen
                WeddingService.objects.update_or_create(
                    wedding=wedding,
                    service=service,
                    defaults={'chosen': False}
                )

        # Saving the total_price to the wedding model
        wedding.total_service_price = total_price
        wedding.save()

        # Redirect to the confirmation page
        return redirect('select_services_confirmation', wedding_id=wedding.id)
    else:
        # GET request, render the form
        return render(request, 'agency/select_services.html', {
            'services': services,
            'wedding': wedding,
        })
    
def select_services_confirmation(request, wedding_id):
    wedding = get_object_or_404(Wedding, id=wedding_id)
    selected_services = WeddingService.objects.filter(wedding=wedding, chosen=True)
    total_price = sum(ws.service.price for ws in selected_services)
    return render(request, 'agency/select_services_confirmation.html', {
        'wedding': wedding,
        'selected_services': selected_services,
        'total_price': total_price,
    })