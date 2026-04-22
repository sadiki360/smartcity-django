from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['type','description','localisation','gravite','statut',
                  'duree_estimee','routes_impactees','vehicules_impactes','route_alternative']
        widgets = {
            'type': forms.Select(attrs={'class':'form-select'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'localisation': forms.TextInput(attrs={'class':'form-control'}),
            'gravite': forms.Select(attrs={'class':'form-select'}),
            'statut': forms.Select(attrs={'class':'form-select'}),
            'duree_estimee': forms.NumberInput(attrs={'class':'form-control'}),
            'routes_impactees': forms.SelectMultiple(attrs={'class':'form-select','size':'4'}),
            'vehicules_impactes': forms.SelectMultiple(attrs={'class':'form-select','size':'4'}),
            'route_alternative': forms.Select(attrs={'class':'form-select'}),
        }
