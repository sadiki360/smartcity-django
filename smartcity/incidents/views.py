from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Incident
from .forms import IncidentForm

@login_required
def incident_list(request):
    statut = request.GET.get('statut', '')
    type_inc = request.GET.get('type', '')
    incidents = Incident.objects.prefetch_related('routes_impactees').all()
    if statut: incidents = incidents.filter(statut=statut)
    if type_inc: incidents = incidents.filter(type=type_inc)
    return render(request, 'incidents/incident_list.html', {
        'incidents': incidents, 'statut': statut, 'type_inc': type_inc,
        'statut_choices': Incident.STATUT_CHOICES,
        'type_choices': Incident.TYPE_CHOICES,
    })

@login_required
def incident_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'incidents/incident_detail.html', {'incident': incident})

@login_required
def incident_create(request):
    form = IncidentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Incident signalé !")
        return redirect('incident_list')
    return render(request, 'incidents/incident_form.html', {'form': form, 'title': 'Signaler un incident'})

@login_required
def incident_update(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    form = IncidentForm(request.POST or None, instance=incident)
    if form.is_valid():
        form.save()
        messages.success(request, "Incident mis à jour !")
        return redirect('incident_list')
    return render(request, 'incidents/incident_form.html', {'form': form, 'title': 'Modifier incident'})

@login_required
def incident_delete(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        incident.delete()
        messages.success(request, "Incident supprimé.")
        return redirect('incident_list')
    return render(request, 'traffic/confirm_delete.html', {'obj': incident, 'type': 'Incident'})

@login_required
def incident_resoudre(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    from django.utils import timezone
    incident.statut = 'resolu'
    incident.date_resolution = timezone.now()
    incident.save()
    messages.success(request, "Incident marqué comme résolu.")
    return redirect('incident_list')
