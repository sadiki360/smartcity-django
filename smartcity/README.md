# SmartCity Django — Application Web
**Université Abdelmalek Essaâdi — FST Tanger | 2025/2026**
*Module : Développement Web Avancé — Back end Python*
*Professeur : Sara AHSAIN*

---

## Équipe
- EL BOURMAKI Salim
- EL HAJIOUI Houssam
- SADIKI Maroua
- DANY Homam

---

## Lancement rapide (Windows)

```
Double-cliquer sur setup.bat
```

Puis ouvrir : **http://127.0.0.1:8000**
Connexion : `admin` / `admin123`

---

## Lancement manuel

```bash
# 1. Migrations
py -3.12 manage.py makemigrations
py -3.12 manage.py migrate

# 2. Données de test
py -3.12 manage.py shell < seed_data.py

# 3. Lancer le serveur
py -3.12 manage.py runserver
```

---

## Structure du projet

```
smartcity/
├── smartcity/          ← Configuration principale
│   ├── settings.py
│   └── urls.py
├── traffic/            ← Routes, Intersections, Zones
├── vehicles/           ← Véhicules, Missions prioritaires
├── signals/            ← Feux de circulation
├── incidents/          ← Incidents, Reroutage
├── parking/            ← Parkings, Bornes EV
├── dashboard/          ← Tableau de bord global
├── templates/          ← Templates HTML
├── seed_data.py        ← Données de test
└── setup.bat           ← Script de démarrage Windows
```

---

## Fonctionnalités

| Module | Fonctionnalités |
|--------|----------------|
| **Réseau Routier** | CRUD routes, intersections, zones urbaines, filtrage |
| **Véhicules** | CRUD véhicules (6 types), filtrage multi-critères, détail batterie EV |
| **Feux** | CRUD feux, changement d'état en 1 clic, historique, mode adaptatif |
| **Incidents** | Signalement, reroutage, résolution, filtrage par type/statut |
| **Parking** | CRUD parkings, taux d'occupation en temps réel, bornes EV |
| **Missions** | Gestion véhicules prioritaires (ambulance, pompiers, police) |
| **Dashboard** | Statistiques globales, graphiques, alertes temps réel |

---

## Modèles Django

- **ZoneUrbaine** — zones de la ville
- **Intersection** — points de croisement (FK → ZoneUrbaine)
- **Route** — routes (FK → ZoneUrbaine, M2M → Intersection)
- **Vehicule** — tous types de véhicules (FK → Route)
- **Mission** — missions prioritaires (FK → Vehicule, M2M → Intersection)
- **FeuCirculation** — feux (FK → Intersection)
- **HistoriqueFeu** — historique changements (FK → FeuCirculation)
- **Incident** — incidents (M2M → Route, M2M → Vehicule)
- **Parking** — parkings (FK → ZoneUrbaine)
- **BorneRecharge** — bornes EV (FK → Parking, O2O → Vehicule)
