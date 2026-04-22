from django.contrib import admin
from .models import Parking, BorneRecharge

@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ['nom', 'capacite_totale', 'places_disponibles', 'taux_occupation', 'ouvert']
    list_filter = ['ouvert', 'zone']

@admin.register(BorneRecharge)
class BorneAdmin(admin.ModelAdmin):
    list_display = ['numero', 'parking', 'type_charge', 'etat', 'puissance_kw']
    list_filter = ['etat', 'type_charge']
