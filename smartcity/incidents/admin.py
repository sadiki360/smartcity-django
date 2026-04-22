from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['type', 'gravite', 'statut', 'localisation', 'date_debut']
    list_filter = ['type', 'gravite', 'statut']
    search_fields = ['localisation', 'description']
    filter_horizontal = ['routes_impactees', 'vehicules_impactes']
