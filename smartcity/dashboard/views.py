from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

@login_required
def dashboard(request):
    from vehicles.models import Vehicule, Mission
    from incidents.models import Incident
    from signals.models import FeuCirculation
    from parking.models import Parking, BorneRecharge
    from traffic.models import Route

    # Stats globales
    total_vehicules = Vehicule.objects.count()
    vehicules_par_type = Vehicule.objects.values('type').annotate(nb=Count('id'))
    incidents_actifs = Incident.objects.filter(statut='actif').count()
    missions_en_cours = Mission.objects.filter(statut='en_cours').count()

    # Feux
    feux_rouge = FeuCirculation.objects.filter(etat='rouge').count()
    feux_vert = FeuCirculation.objects.filter(etat='vert').count()
    feux_orange = FeuCirculation.objects.filter(etat='orange').count()

    # Parkings
    all_parkings = Parking.objects.all()
    parkings_satures = sum(1 for p in all_parkings if p.est_sature)

    # EV en recharge
    ev_recharge = BorneRecharge.objects.filter(etat='occupe').count()

    # Derniers incidents
    derniers_incidents = Incident.objects.filter(statut='actif').order_by('-date_debut')[:5]
    dernieres_missions = Mission.objects.filter(statut='en_cours').order_by('-date_debut')[:5]

    # Routes par état
    routes_ouvertes = Route.objects.filter(etat='ouvert').count()
    routes_fermees = Route.objects.filter(etat='ferme').count()

    context = {
        'total_vehicules': total_vehicules,
        'vehicules_par_type': list(vehicules_par_type),
        'incidents_actifs': incidents_actifs,
        'missions_en_cours': missions_en_cours,
        'feux_rouge': feux_rouge, 'feux_vert': feux_vert, 'feux_orange': feux_orange,
        'parkings_satures': parkings_satures,
        'total_parkings': all_parkings.count(),
        'ev_recharge': ev_recharge,
        'derniers_incidents': derniers_incidents,
        'dernieres_missions': dernieres_missions,
        'routes_ouvertes': routes_ouvertes,
        'routes_fermees': routes_fermees,
    }
    return render(request, 'dashboard/dashboard.html', context)

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')
