from django.db import models
from traffic.models import Route, Intersection

class Vehicule(models.Model):
    TYPE_CHOICES = [
        ('voiture','Voiture'), ('bus','Bus'), ('camion','Camion'),
        ('moto','Moto'), ('electrique','Électrique'), ('prioritaire','Prioritaire'),
    ]
    ETAT_CHOICES = [
        ('actif','En circulation'), ('arrete','Arrêté'),
        ('recharge','En recharge'), ('mission','En mission'),
    ]
    immatriculation = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    vitesse_moyenne = models.FloatField(default=0)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='arrete')
    route_actuelle = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True, related_name='vehicules')
    point_depart = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    # Spécifique électrique
    niveau_batterie = models.FloatField(null=True, blank=True, help_text="% pour véhicules électriques")
    # Spécifique prioritaire
    mission_statut = models.CharField(max_length=100, blank=True)
    priorite = models.IntegerField(default=0, help_text="Niveau de priorité (0=normal, 1-3=prioritaire)")
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"{self.immatriculation} ({self.get_type_display()})"
    class Meta: ordering = ['-date_ajout']

class Mission(models.Model):
    """Pour les véhicules prioritaires (ambulance, pompiers, police)"""
    TYPE_CHOICES = [('ambulance','Ambulance'), ('pompiers','Pompiers'), ('police','Police')]
    STATUT_CHOICES = [('en_cours','En cours'), ('terminee','Terminée'), ('annulee','Annulée')]

    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='missions')
    type_service = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    depart = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(null=True, blank=True)
    intersection_prioritaire = models.ManyToManyField(Intersection, blank=True)

    def __str__(self): return f"Mission {self.type_service} - {self.vehicule}"
    class Meta: ordering = ['-date_debut']
