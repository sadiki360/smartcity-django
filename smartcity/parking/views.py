from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Parking, BorneRecharge
from .forms import ParkingForm, BorneForm

@login_required
def parking_list(request):
    filtre = request.GET.get('filtre', '')
    parkings = Parking.objects.select_related('zone').all()
    if filtre == 'disponible': parkings = [p for p in parkings if not p.est_sature]
    elif filtre == 'sature': parkings = [p for p in parkings if p.est_sature]
    return render(request, 'parking/parking_list.html', {
        'parkings': parkings, 'filtre': filtre
    })

@login_required
def parking_detail(request, pk):
    parking = get_object_or_404(Parking, pk=pk)
    bornes = parking.bornes.select_related('vehicule_en_charge').all()
    return render(request, 'parking/parking_detail.html', {'parking': parking, 'bornes': bornes})

@login_required
def parking_create(request):
    form = ParkingForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Parking ajouté !")
        return redirect('parking_list')
    return render(request, 'parking/parking_form.html', {'form': form, 'title': 'Ajouter un parking'})

@login_required
def parking_update(request, pk):
    parking = get_object_or_404(Parking, pk=pk)
    form = ParkingForm(request.POST or None, instance=parking)
    if form.is_valid():
        form.save()
        messages.success(request, "Parking modifié !")
        return redirect('parking_list')
    return render(request, 'parking/parking_form.html', {'form': form, 'title': 'Modifier parking'})

@login_required
def parking_delete(request, pk):
    parking = get_object_or_404(Parking, pk=pk)
    if request.method == 'POST':
        parking.delete()
        messages.success(request, "Parking supprimé.")
        return redirect('parking_list')
    return render(request, 'traffic/confirm_delete.html', {'obj': parking, 'type': 'Parking'})

@login_required
def borne_create(request):
    form = BorneForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Borne ajoutée !")
        return redirect('parking_list')
    return render(request, 'parking/parking_form.html', {'form': form, 'title': 'Ajouter une borne'})
