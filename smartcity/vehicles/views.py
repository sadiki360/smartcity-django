from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Vehicule, Mission
from .forms import VehiculeForm, VehiculeFilterForm, MissionForm

@login_required
def vehicule_list(request):
    form = VehiculeFilterForm(request.GET or None)
    vehicules = Vehicule.objects.select_related('route_actuelle').all()
    if form.is_valid():
        if form.cleaned_data.get('type'):
            vehicules = vehicules.filter(type=form.cleaned_data['type'])
        if form.cleaned_data.get('etat'):
            vehicules = vehicules.filter(etat=form.cleaned_data['etat'])
        if form.cleaned_data.get('search'):
            vehicules = vehicules.filter(immatriculation__icontains=form.cleaned_data['search'])
    return render(request, 'vehicles/vehicule_list.html', {'vehicules': vehicules, 'form': form})

@login_required
def vehicule_detail(request, pk):
    v = get_object_or_404(Vehicule, pk=pk)
    return render(request, 'vehicles/vehicule_detail.html', {'vehicule': v})

@login_required
def vehicule_create(request):
    form = VehiculeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Véhicule ajouté !")
        return redirect('vehicule_list')
    return render(request, 'vehicles/vehicule_form.html', {'form': form, 'title': 'Ajouter un véhicule'})

@login_required
def vehicule_update(request, pk):
    v = get_object_or_404(Vehicule, pk=pk)
    form = VehiculeForm(request.POST or None, instance=v)
    if form.is_valid():
        form.save()
        messages.success(request, "Véhicule modifié !")
        return redirect('vehicule_list')
    return render(request, 'vehicles/vehicule_form.html', {'form': form, 'title': 'Modifier le véhicule'})

@login_required
def vehicule_delete(request, pk):
    v = get_object_or_404(Vehicule, pk=pk)
    if request.method == 'POST':
        v.delete()
        messages.success(request, "Véhicule supprimé.")
        return redirect('vehicule_list')
    return render(request, 'traffic/confirm_delete.html', {'obj': v, 'type': 'Véhicule'})

@login_required
def mission_list(request):
    missions = Mission.objects.select_related('vehicule').all()
    return render(request, 'vehicles/mission_list.html', {'missions': missions})

@login_required
def mission_create(request):
    form = MissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Mission créée !")
        return redirect('mission_list')
    return render(request, 'vehicles/vehicule_form.html', {'form': form, 'title': 'Nouvelle mission'})

@login_required
def mission_update(request, pk):
    m = get_object_or_404(Mission, pk=pk)
    form = MissionForm(request.POST or None, instance=m)
    if form.is_valid():
        form.save()
        messages.success(request, "Mission mise à jour !")
        return redirect('mission_list')
    return render(request, 'vehicles/vehicule_form.html', {'form': form, 'title': 'Modifier mission'})
