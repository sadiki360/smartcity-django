from django import forms
from .models import Parking, BorneRecharge

class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ['nom','adresse','capacite_totale','places_disponibles','tarif_horaire','zone','ouvert']
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'adresse': forms.TextInput(attrs={'class':'form-control'}),
            'capacite_totale': forms.NumberInput(attrs={'class':'form-control'}),
            'places_disponibles': forms.NumberInput(attrs={'class':'form-control'}),
            'tarif_horaire': forms.NumberInput(attrs={'class':'form-control'}),
            'zone': forms.Select(attrs={'class':'form-select'}),
            'ouvert': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class BorneForm(forms.ModelForm):
    class Meta:
        model = BorneRecharge
        fields = ['parking','numero','type_charge','puissance_kw','etat','vehicule_en_charge','duree_estimee']
        widgets = {
            'parking': forms.Select(attrs={'class':'form-select'}),
            'numero': forms.TextInput(attrs={'class':'form-control'}),
            'type_charge': forms.Select(attrs={'class':'form-select'}),
            'puissance_kw': forms.NumberInput(attrs={'class':'form-control'}),
            'etat': forms.Select(attrs={'class':'form-select'}),
            'vehicule_en_charge': forms.Select(attrs={'class':'form-select'}),
            'duree_estimee': forms.NumberInput(attrs={'class':'form-control'}),
        }
