from django import forms
from .models import Vehicule, Mission

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['immatriculation','type','vitesse_moyenne','etat','route_actuelle',
                  'point_depart','destination','niveau_batterie','mission_statut','priorite']
        widgets = {
            'immatriculation': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-select'}),
            'vitesse_moyenne': forms.NumberInput(attrs={'class':'form-control'}),
            'etat': forms.Select(attrs={'class':'form-select'}),
            'route_actuelle': forms.Select(attrs={'class':'form-select'}),
            'point_depart': forms.TextInput(attrs={'class':'form-control'}),
            'destination': forms.TextInput(attrs={'class':'form-control'}),
            'niveau_batterie': forms.NumberInput(attrs={'class':'form-control','min':0,'max':100}),
            'mission_statut': forms.TextInput(attrs={'class':'form-control'}),
            'priorite': forms.NumberInput(attrs={'class':'form-control','min':0,'max':3}),
        }

class VehiculeFilterForm(forms.Form):
    type = forms.ChoiceField(choices=[('','Tous')]+Vehicule.TYPE_CHOICES, required=False,
                              widget=forms.Select(attrs={'class':'form-select'}))
    etat = forms.ChoiceField(choices=[('','Tous')]+Vehicule.ETAT_CHOICES, required=False,
                              widget=forms.Select(attrs={'class':'form-select'}))
    search = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Immatriculation...'}))

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['vehicule','type_service','description','depart','destination','statut']
        widgets = {
            'vehicule': forms.Select(attrs={'class':'form-select'}),
            'type_service': forms.Select(attrs={'class':'form-select'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'depart': forms.TextInput(attrs={'class':'form-control'}),
            'destination': forms.TextInput(attrs={'class':'form-control'}),
            'statut': forms.Select(attrs={'class':'form-select'}),
        }
