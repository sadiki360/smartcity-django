from django import forms
from .models import Route, Intersection, ZoneUrbaine

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['nom', 'longueur_km', 'nb_voies', 'vitesse_limite', 'sens', 'etat', 'zone', 'intersections']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la route'}),
            'longueur_km': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_voies': forms.NumberInput(attrs={'class': 'form-control'}),
            'vitesse_limite': forms.NumberInput(attrs={'class': 'form-control'}),
            'sens': forms.Select(attrs={'class': 'form-select'}),
            'etat': forms.Select(attrs={'class': 'form-select'}),
            'zone': forms.Select(attrs={'class': 'form-select'}),
            'intersections': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }

class IntersectionForm(forms.ModelForm):
    class Meta:
        model = Intersection
        fields = ['nom', 'latitude', 'longitude', 'zone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'zone': forms.Select(attrs={'class': 'form-select'}),
        }
