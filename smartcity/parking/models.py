from django.db import models
from traffic.models import ZoneUrbaine
from vehicles.models import Vehicule

class Parking(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=300)
    capacite_totale = models.IntegerField(default=100)
    places_disponibles = models.IntegerField(default=100)
    tarif_horaire = models.FloatField(default=5.0, help_text="Tarif en MAD/heure")
    zone = models.ForeignKey(ZoneUrbaine, on_delete=models.SET_NULL, null=True, blank=True)
    ouvert = models.BooleanField(default=True)

    @property
    def taux_occupation(self):
        if self.capacite_totale == 0: return 0
        return round((self.capacite_totale - self.places_disponibles) / self.capacite_totale * 100, 1)

    @property
    def est_sature(self):
        return self.taux_occupation >= 90

    def __str__(self): return self.nom
    class Meta: ordering = ['nom']

class BorneRecharge(models.Model):
    ETAT_CHOICES = [('libre','Libre'), ('occupe','Occupée'), ('panne','En panne')]
    TYPE_CHOICES = [('lente','Lente (AC)'), ('rapide','Rapide (DC)'), ('ultra','Ultra-rapide')]

    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name='bornes')
    numero = models.CharField(max_length=20)
    type_charge = models.CharField(max_length=10, choices=TYPE_CHOICES, default='rapide')
    puissance_kw = models.FloatField(default=22.0)
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES, default='libre')
    vehicule_en_charge = models.OneToOneField(Vehicule, on_delete=models.SET_NULL,
                                               null=True, blank=True, related_name='borne_recharge')
    debut_recharge = models.DateTimeField(null=True, blank=True)
    duree_estimee = models.IntegerField(null=True, blank=True, help_text="Minutes")

    def __str__(self): return f"Borne {self.numero} @ {self.parking}"
    class Meta: verbose_name = "Borne de Recharge"
