from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import FeuCirculation, HistoriqueFeu
from .forms import FeuForm

@login_required
def feu_list(request):
    feux = FeuCirculation.objects.select_related('intersection').all()
    return render(request, 'signals/feu_list.html', {'feux': feux})

@login_required
def feu_detail(request, pk):
    feu = get_object_or_404(FeuCirculation, pk=pk)
    historique = feu.historique.all()[:10]
    return render(request, 'signals/feu_detail.html', {'feu': feu, 'historique': historique})

@login_required
def feu_create(request):
    form = FeuForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Feu de circulation ajouté !")
        return redirect('feu_list')
    return render(request, 'signals/feu_form.html', {'form': form, 'title': 'Ajouter un feu'})

@login_required
def feu_update(request, pk):
    feu = get_object_or_404(FeuCirculation, pk=pk)
    ancien_etat = feu.etat
    form = FeuForm(request.POST or None, instance=feu)
    if form.is_valid():
        nouvel_feu = form.save()
        if nouvel_feu.etat != ancien_etat:
            HistoriqueFeu.objects.create(
                feu=nouvel_feu, ancien_etat=ancien_etat,
                nouvel_etat=nouvel_feu.etat, commentaire="Modification manuelle"
            )
        messages.success(request, "Feu modifié !")
        return redirect('feu_list')
    return render(request, 'signals/feu_form.html', {'form': form, 'title': 'Modifier le feu'})

@login_required
def feu_changer_etat(request, pk):
    """Changer rapidement l'état d'un feu (rouge→vert→orange→rouge)"""
    feu = get_object_or_404(FeuCirculation, pk=pk)
    ancien = feu.etat
    cycle = {'rouge': 'vert', 'vert': 'orange', 'orange': 'rouge'}
    feu.etat = cycle.get(feu.etat, 'rouge')
    feu.save()
    HistoriqueFeu.objects.create(
        feu=feu, ancien_etat=ancien, nouvel_etat=feu.etat, commentaire="Changement rapide"
    )
    messages.success(request, f"Feu passé à {feu.get_etat_display()}")
    return redirect('feu_list')

@login_required
def feu_delete(request, pk):
    feu = get_object_or_404(FeuCirculation, pk=pk)
    if request.method == 'POST':
        feu.delete()
        messages.success(request, "Feu supprimé.")
        return redirect('feu_list')
    return render(request, 'traffic/confirm_delete.html', {'obj': feu, 'type': 'Feu'})
