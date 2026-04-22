from django import forms
from .models import FeuCirculation

class FeuForm(forms.ModelForm):
    class Meta:
        model = FeuCirculation
        fields = ['intersection','etat','duree_rouge','duree_vert','duree_orange','mode','actif']
        widgets = {
            'intersection': forms.Select(attrs={'class':'form-select'}),
            'etat': forms.Select(attrs={'class':'form-select'}),
            'duree_rouge': forms.NumberInput(attrs={'class':'form-control'}),
            'duree_vert': forms.NumberInput(attrs={'class':'form-control'}),
            'duree_orange': forms.NumberInput(attrs={'class':'form-control'}),
            'mode': forms.Select(attrs={'class':'form-select'}),
            'actif': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
