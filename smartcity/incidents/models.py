from django.db import models
from traffic.models import Route
from vehicles.models import Vehicule

class Incident(models.Model):
    TYPE_CHOICES = [
        ('accident','Accident'), ('blocage','Route bloquée'),
        ('congestion','Congestion'), ('travaux','Travaux'), ('urgence','Urgence'),
    ]
    GRAVITE_CHOICES = [('faible','Faible'), ('moyen','Moyen'), ('grave','Grave'), ('critique','Critique')]
    STATUT_CHOICES = [('actif','Actif'), ('en_cours','En cours de résolution'), ('resolu','Résolu')]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    localisation = models.CharField(max_length=300)
    gravite = models.CharField(max_length=10, choices=GRAVITE_CHOICES, default='moyen')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='actif')
    duree_estimee = models.IntegerField(default=30, help_text="Durée estimée en minutes")
    date_debut = models.DateTimeField(auto_now_add=True)
    date_resolution = models.DateTimeField(null=True, blank=True)
    routes_impactees = models.ManyToManyField(Route, blank=True, related_name='incidents')
    vehicules_impactes = models.ManyToManyField(Vehicule, blank=True, related_name='incidents')
    route_alternative = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='alternative_pour')

    def __str__(self): return f"{self.get_type_display()} — {self.localisation[:50]}"
    class Meta: ordering = ['-date_debut']
