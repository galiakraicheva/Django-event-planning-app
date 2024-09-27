from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('first-meeting/', views.first_meeting, name='first_meeting'),
    path('select-services/<int:wedding_id>/', views.select_services, name='select_services'),
    path('select-services/confirmation/<int:wedding_id>/', views.select_services_confirmation, name='select_services_confirmation'),
]