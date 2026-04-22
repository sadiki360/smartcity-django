# 🏙️ SmartCity Django

> Plateforme de gestion urbaine intelligente — Python / Django / Bootstrap 5

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)](https://djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)](https://getbootstrap.com)
[![License](https://img.shields.io/badge/License-Academic-orange)]()

---

## 📌 Description

**SmartCity Django** est une application web complète de supervision et d'administration d'une ville intelligente. Elle permet de gérer en temps réel les entités clés d'une Smart City : réseau routier, véhicules, feux de circulation, incidents, parkings intelligents et véhicules prioritaires.

Développée avec **Django (MVT)**, **Bootstrap 5** et **Chart.js**, cette plateforme offre une interface centralisée, responsive et sécurisée.

---

## 🎓 Contexte Académique

| | |
|---|---|
| **Module** | Développement Web Avancé — Back end Python |
| **Institution** | Faculté des Sciences et Techniques de Tanger |
| **Université** | Université Abdelmalek Essaâdi |
| **Encadrante** | Prof. Sara AHSAIN |
| **Étudiante** | Maroua SADIKI |
| **Année** | 2025 / 2026 |

---

## ✨ Fonctionnalités

| Module | Fonctionnalités |
|---|---|
| 🛣️ **Réseau Routier** | Gestion des routes, intersections, zones urbaines |
| 🚗 **Véhicules** | Voiture, Bus, Camion, Moto, Électrique, Prioritaire |
| 🚦 **Feux de Circulation** | États, historique, modes fixe/adaptatif |
| ⚠️ **Incidents** | Signalement, reroutage, résolution |
| 🅿️ **Parkings Intelligents** | Taux d'occupation, bornes de recharge EV |
| 🚨 **Véhicules Prioritaires** | Ambulance, Pompiers, Police — gestion missions |
| 📊 **Tableau de Bord** | Statistiques globales + graphiques Chart.js |
| 🔐 **Authentification** | Login/Logout sécurisé, @login_required |

---

## 🛠️ Stack Technique

- **Backend** : Python 3.12 / Django 5.x
- **Base de données** : SQLite
- **Frontend** : Bootstrap 5.3 / Chart.js / Font Awesome 6
- **Auth** : django.contrib.auth (LoginView, LogoutView, @login_required)
- **Formulaires** : Django Forms avec validation côté serveur

---

## 🗂️ Structure du Projet

```
smartcity/               ← Projet Django principal (settings, urls)
├── traffic/             ← Routes, Intersections, Zones Urbaines
├── vehicles/            ← Véhicules, Missions Prioritaires
├── signals/             ← Feux de Circulation, Historique
├── incidents/           ← Incidents, Reroutage
├── parking/             ← Parkings Intelligents, Bornes EV
├── dashboard/           ← Tableau de Bord Global
├── templates/           ← Templates HTML (base + modules)
└── seed_data.py         ← Script de population initiale
```

---

## 🚀 Installation & Lancement

### 1. Cloner le projet
```bash
git clone https://github.com/sadiki360/smartcity-django.git
cd smartcity-django
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# ou
source venv/bin/activate     # Linux / Mac
```

### 3. Installer les dépendances
```bash
pip install django
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Peupler la base de données (données de test)
```bash
python seed_data.py
```

### 6. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur
```bash
python manage.py runserver
```

Ouvrir : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔑 Compte par défaut

| Paramètre | Valeur |
|---|---|
| Nom d'utilisateur | `admin` |
| Mot de passe | `admin123` |

---

## 🗺️ URLs principales

| URL | Description |
|---|---|
| `/dashboard/` | Tableau de bord global |
| `/traffic/routes/` | Gestion des routes |
| `/vehicles/` | Gestion des véhicules |
| `/signals/` | Feux de circulation |
| `/incidents/` | Gestion des incidents |
| `/parking/` | Parkings et bornes EV |
| `/admin/` | Panel d'administration Django |

---

## 📊 Modèles Django (10 modèles)

`ZoneUrbaine` · `Intersection` · `Route` · `Vehicule` · `Mission` · `FeuCirculation` · `HistoriqueFeu` · `Incident` · `Parking` · `BorneRecharge`

Relations : **ForeignKey**, **ManyToManyField**, **OneToOneField**

---

## 🔒 Sécurité

- ✅ `@login_required` sur toutes les vues
- ✅ Protection CSRF (`{% csrf_token %}`)
- ✅ Protection XSS (auto-échappement Django)
- ✅ Sessions sécurisées

---

## 📈 Améliorations futures

- API REST avec Django REST Framework
- Temps réel avec WebSockets (Django Channels)
- Carte interactive Leaflet.js
- Intégration IoT pour données de trafic réelles
- Application mobile React Native / Flutter

---

*SmartCity Django — Une plateforme pour les villes de demain. 🌆*
