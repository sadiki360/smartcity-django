from django.db import models
from traffic.models import Intersection

class FeuCirculation(models.Model):
    ETAT_CHOICES = [('rouge','🔴 Rouge'), ('orange','🟠 Orange'), ('vert','🟢 Vert')]
    MODE_CHOICES = [('fixe','Fixe'), ('adaptatif','Adaptatif')]

    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE, related_name='feux')
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES, default='rouge')
    duree_rouge = models.IntegerField(default=30, help_text="Durée rouge (secondes)")
    duree_vert = models.IntegerField(default=25, help_text="Durée vert (secondes)")
    duree_orange = models.IntegerField(default=5, help_text="Durée orange (secondes)")
    mode = models.CharField(max_length=15, choices=MODE_CHOICES, default='fixe')
    actif = models.BooleanField(default=True)
    derniere_modif = models.DateTimeField(auto_now=True)

    def __str__(self): return f"Feu @ {self.intersection} — {self.get_etat_display()}"
    class Meta: verbose_name = "Feu de Circulation"

class HistoriqueFeu(models.Model):
    feu = models.ForeignKey(FeuCirculation, on_delete=models.CASCADE, related_name='historique')
    ancien_etat = models.CharField(max_length=10)
    nouvel_etat = models.CharField(max_length=10)
    date_changement = models.DateTimeField(auto_now_add=True)
    commentaire = models.CharField(max_length=200, blank=True)

    def __str__(self): return f"{self.feu} : {self.ancien_etat}→{self.nouvel_etat}"
    class Meta: ordering = ['-date_changement']
