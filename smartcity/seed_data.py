"""
seed_data.py — Script pour peupler la base de données avec des données de test.
Lancer avec : python manage.py shell < seed_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartcity.settings')
django.setup()

from django.contrib.auth.models import User
from traffic.models import ZoneUrbaine, Intersection, Route
from vehicles.models import Vehicule, Mission
from signals.models import FeuCirculation, HistoriqueFeu
from incidents.models import Incident
from parking.models import Parking, BorneRecharge

print("🌱 Création des données initiales...")

# ── Super utilisateur ──────────────────────────────────────────────────────
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@smartcity.ma', 'admin123')
    print("✅ Admin créé : admin / admin123")

# ── Zones ──────────────────────────────────────────────────────────────────
z1, _ = ZoneUrbaine.objects.get_or_create(nom="Centre-Ville",    defaults={'description': 'Zone centrale de la ville'})
z2, _ = ZoneUrbaine.objects.get_or_create(nom="Zone Industrielle", defaults={'description': 'Zone nord industrielle'})
z3, _ = ZoneUrbaine.objects.get_or_create(nom="Zone Résidentielle", defaults={'description': 'Quartiers résidentiels sud'})
print("✅ Zones créées")

# ── Intersections ──────────────────────────────────────────────────────────
i1, _ = Intersection.objects.get_or_create(nom="Carrefour Mohammed V",    defaults={'latitude': 35.77, 'longitude': -5.80, 'zone': z1})
i2, _ = Intersection.objects.get_or_create(nom="Rond-Point Hassan II",    defaults={'latitude': 35.78, 'longitude': -5.81, 'zone': z1})
i3, _ = Intersection.objects.get_or_create(nom="Croisement Zerktouni",    defaults={'latitude': 35.76, 'longitude': -5.79, 'zone': z1})
i4, _ = Intersection.objects.get_or_create(nom="Carrefour Zone Nord",     defaults={'latitude': 35.80, 'longitude': -5.82, 'zone': z2})
i5, _ = Intersection.objects.get_or_create(nom="Échangeur Autoroute",     defaults={'latitude': 35.75, 'longitude': -5.83, 'zone': z3})
print("✅ Intersections créées")

# ── Routes ─────────────────────────────────────────────────────────────────
r1, _ = Route.objects.get_or_create(nom="Boulevard Mohammed V",
    defaults={'longueur_km': 3.5, 'nb_voies': 4, 'vitesse_limite': 60, 'etat': 'ouvert', 'zone': z1})
r1.intersections.set([i1, i2])

r2, _ = Route.objects.get_or_create(nom="Avenue Hassan II",
    defaults={'longueur_km': 2.1, 'nb_voies': 2, 'vitesse_limite': 50, 'etat': 'ouvert', 'zone': z1})
r2.intersections.set([i2, i3])

r3, _ = Route.objects.get_or_create(nom="Route Industrielle Nord",
    defaults={'longueur_km': 5.8, 'nb_voies': 2, 'vitesse_limite': 80, 'etat': 'travaux', 'zone': z2})
r3.intersections.set([i4])

r4, _ = Route.objects.get_or_create(nom="Avenue Résidentielle Sud",
    defaults={'longueur_km': 1.5, 'nb_voies': 2, 'vitesse_limite': 30, 'etat': 'ouvert', 'zone': z3})
r4.intersections.set([i5])

r5, _ = Route.objects.get_or_create(nom="Boulevard Périphérique",
    defaults={'longueur_km': 12.0, 'nb_voies': 6, 'vitesse_limite': 100, 'etat': 'ouvert', 'zone': z1})
r5.intersections.set([i1, i3, i4])
print("✅ Routes créées")

# ── Véhicules ──────────────────────────────────────────────────────────────
veh_data = [
    ('AB-1234-TNG', 'voiture',     15.0, 'actif',   r1, 'Centre', 'Aéroport',   None,  0),
    ('CD-5678-TNG', 'bus',         8.0,  'actif',   r1, 'Gare',   'Université', None,  0),
    ('EF-9012-TNG', 'camion',      5.0,  'arrete',  r3, 'Zone I', 'Port',       None,  0),
    ('GH-3456-TNG', 'moto',        25.0, 'actif',   r2, 'Centre', 'Marché',     None,  0),
    ('IJ-7890-TNG', 'electrique',  18.0, 'recharge',None,'Parking A','Centre',  45.0,  0),
    ('KL-1111-TNG', 'electrique',  20.0, 'actif',   r4, 'Résid.', 'Centre',     78.0,  0),
    ('AM-2222-TNG', 'prioritaire', 30.0, 'mission', r1, 'Hôpital','Accident',   None,  3),
    ('PM-3333-TNG', 'prioritaire', 25.0, 'actif',   r2, 'Comm.',  'Patrouille', None,  2),
    ('XY-4444-TNG', 'bus',         9.0,  'actif',   r5, 'Gare',   'Zone I',     None,  0),
    ('ZZ-5555-TNG', 'voiture',     12.0, 'arrete',  None,'Quartier','Centre',   None,  0),
]
vehicules = []
for immat, typ, vit, etat, route, dep, dest, bat, prio in veh_data:
    v, _ = Vehicule.objects.get_or_create(immatriculation=immat, defaults={
        'type': typ, 'vitesse_moyenne': vit, 'etat': etat,
        'route_actuelle': route, 'point_depart': dep, 'destination': dest,
        'niveau_batterie': bat, 'priorite': prio,
    })
    vehicules.append(v)
print("✅ Véhicules créés")

# ── Missions prioritaires ──────────────────────────────────────────────────
vp1 = Vehicule.objects.get(immatriculation='AM-2222-TNG')
vp2 = Vehicule.objects.get(immatriculation='PM-3333-TNG')
if not vp1.missions.exists():
    Mission.objects.create(vehicule=vp1, type_service='ambulance',
        description='Intervention urgente — victime accident route N1',
        depart='Hôpital Mohammed VI', destination='Route N1 km 12',
        statut='en_cours')
if not vp2.missions.exists():
    Mission.objects.create(vehicule=vp2, type_service='police',
        description='Patrouille de nuit centre-ville',
        depart='Commissariat Central', destination='Boulevard Mohammed V',
        statut='en_cours')
print("✅ Missions créées")

# ── Feux de circulation ────────────────────────────────────────────────────
feux_data = [
    (i1, 'rouge',  'fixe',       30, 25, 5),
    (i2, 'vert',   'adaptatif',  45, 40, 5),
    (i3, 'orange', 'fixe',       30, 25, 5),
    (i4, 'rouge',  'fixe',       60, 55, 5),
    (i5, 'vert',   'adaptatif',  35, 30, 5),
]
for inter, etat, mode, dr, dv, do in feux_data:
    feu, created = FeuCirculation.objects.get_or_create(intersection=inter, defaults={
        'etat': etat, 'mode': mode,
        'duree_rouge': dr, 'duree_vert': dv, 'duree_orange': do,
    })
    if created:
        HistoriqueFeu.objects.create(feu=feu, ancien_etat='rouge', nouvel_etat=etat,
                                      commentaire="Configuration initiale")
print("✅ Feux créés")

# ── Incidents ──────────────────────────────────────────────────────────────
if not Incident.objects.exists():
    inc1 = Incident.objects.create(
        type='accident', description='Collision entre deux voitures',
        localisation='Bd Mohammed V km 2', gravite='grave',
        statut='actif', duree_estimee=60)
    inc1.routes_impactees.set([r1])
    inc1.vehicules_impactes.set([vehicules[0]])
    inc1.route_alternative = r2
    inc1.save()

    inc2 = Incident.objects.create(
        type='travaux', description='Réfection de la chaussée',
        localisation='Route Industrielle Nord', gravite='faible',
        statut='en_cours', duree_estimee=480)
    inc2.routes_impactees.set([r3])

    inc3 = Incident.objects.create(
        type='congestion', description='Embouteillage heure de pointe',
        localisation='Avenue Hassan II', gravite='moyen',
        statut='actif', duree_estimee=30)
    inc3.routes_impactees.set([r2])
print("✅ Incidents créés")

# ── Parkings ───────────────────────────────────────────────────────────────
p1, _ = Parking.objects.get_or_create(nom="Parking Centre-Ville A",
    defaults={'adresse': 'Rue Ibn Battouta, Centre', 'capacite_totale': 200,
              'places_disponibles': 45, 'tarif_horaire': 5.0, 'zone': z1})
p2, _ = Parking.objects.get_or_create(nom="Parking Gare Tanger-Ville",
    defaults={'adresse': 'Place de la Gare', 'capacite_totale': 150,
              'places_disponibles': 12, 'tarif_horaire': 3.0, 'zone': z1})
p3, _ = Parking.objects.get_or_create(nom="Parking Zone Industrielle",
    defaults={'adresse': 'Route de Tétouan km 5', 'capacite_totale': 500,
              'places_disponibles': 320, 'tarif_horaire': 2.0, 'zone': z2})
p4, _ = Parking.objects.get_or_create(nom="Parking Résidentiel Sud",
    defaults={'adresse': 'Cité Al Amal', 'capacite_totale': 80,
              'places_disponibles': 60, 'tarif_horaire': 1.0, 'zone': z3})
print("✅ Parkings créés")

# ── Bornes de recharge ─────────────────────────────────────────────────────
ev_vehicule = Vehicule.objects.get(immatriculation='IJ-7890-TNG')
BorneRecharge.objects.get_or_create(parking=p1, numero='B01',
    defaults={'type_charge': 'rapide', 'puissance_kw': 50.0, 'etat': 'occupe',
              'vehicule_en_charge': ev_vehicule, 'duree_estimee': 45})
BorneRecharge.objects.get_or_create(parking=p1, numero='B02',
    defaults={'type_charge': 'lente', 'puissance_kw': 22.0, 'etat': 'libre'})
BorneRecharge.objects.get_or_create(parking=p1, numero='B03',
    defaults={'type_charge': 'ultra', 'puissance_kw': 150.0, 'etat': 'libre'})
BorneRecharge.objects.get_or_create(parking=p3, numero='B04',
    defaults={'type_charge': 'rapide', 'puissance_kw': 50.0, 'etat': 'panne'})
BorneRecharge.objects.get_or_create(parking=p3, numero='B05',
    defaults={'type_charge': 'rapide', 'puissance_kw': 50.0, 'etat': 'libre'})
print("✅ Bornes de recharge créées")

print()
print("🎉 Base de données peuplée avec succès !")
print("   → Admin : http://127.0.0.1:8000/admin/  (admin / admin123)")
print("   → App   : http://127.0.0.1:8000/dashboard/")
