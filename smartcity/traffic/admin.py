from django.contrib import admin
from .models import ZoneUrbaine, Intersection, Route

@admin.register(ZoneUrbaine)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description']
    search_fields = ['nom']

@admin.register(Intersection)
class IntersectionAdmin(admin.ModelAdmin):
    list_display = ['nom', 'zone', 'latitude', 'longitude']
    list_filter = ['zone']
    search_fields = ['nom']

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'etat', 'vitesse_limite', 'nb_voies', 'zone']
    list_filter = ['etat', 'zone']
    search_fields = ['nom']
    filter_horizontal = ['intersections']
