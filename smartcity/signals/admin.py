from django.contrib import admin
from .models import FeuCirculation, HistoriqueFeu

@admin.register(FeuCirculation)
class FeuAdmin(admin.ModelAdmin):
    list_display = ['intersection', 'etat', 'mode', 'actif', 'derniere_modif']
    list_filter = ['etat', 'mode', 'actif']

@admin.register(HistoriqueFeu)
class HistoriqueAdmin(admin.ModelAdmin):
    list_display = ['feu', 'ancien_etat', 'nouvel_etat', 'date_changement']
    list_filter = ['nouvel_etat']
