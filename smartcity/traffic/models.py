from django.db import models

class ZoneUrbaine(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self): return self.nom
    class Meta: verbose_name = "Zone Urbaine"

class Intersection(models.Model):
    nom = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    zone = models.ForeignKey(ZoneUrbaine, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self): return self.nom

class Route(models.Model):
    SENS_CHOICES = [('1', 'Sens unique'), ('2', 'Double sens')]
    ETAT_CHOICES = [('ouvert', 'Ouverte'), ('ferme', 'Fermée'), ('travaux', 'En travaux')]

    nom = models.CharField(max_length=200)
    longueur_km = models.FloatField(default=1.0)
    nb_voies = models.IntegerField(default=2)
    vitesse_limite = models.IntegerField(default=50)
    sens = models.CharField(max_length=1, choices=SENS_CHOICES, default='2')
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='ouvert')
    zone = models.ForeignKey(ZoneUrbaine, on_delete=models.SET_NULL, null=True, blank=True)
    intersections = models.ManyToManyField(Intersection, blank=True, related_name='routes')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.nom
    class Meta: ordering = ['nom']
