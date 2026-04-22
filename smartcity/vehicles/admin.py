from django.contrib import admin
from .models import Vehicule, Mission

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ['immatriculation', 'type', 'etat', 'route_actuelle', 'vitesse_moyenne']
    list_filter = ['type', 'etat']
    search_fields = ['immatriculation']

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['vehicule', 'type_service', 'statut', 'depart', 'destination', 'date_debut']
    list_filter = ['type_service', 'statut']
