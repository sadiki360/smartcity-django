from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Route, Intersection, ZoneUrbaine
from .forms import RouteForm, IntersectionForm

@login_required
def route_list(request):
    q = request.GET.get('q', '')
    etat = request.GET.get('etat', '')
    routes = Route.objects.select_related('zone').prefetch_related('intersections')
    if q: routes = routes.filter(nom__icontains=q)
    if etat: routes = routes.filter(etat=etat)
    return render(request, 'traffic/route_list.html', {
        'routes': routes, 'q': q, 'etat': etat,
        'etat_choices': Route.ETAT_CHOICES
    })

@login_required
def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk)
    return render(request, 'traffic/route_detail.html', {'route': route})

@login_required
def route_create(request):
    form = RouteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Route ajoutée avec succès !")
        return redirect('route_list')
    return render(request, 'traffic/route_form.html', {'form': form, 'title': 'Ajouter une route'})

@login_required
def route_update(request, pk):
    route = get_object_or_404(Route, pk=pk)
    form = RouteForm(request.POST or None, instance=route)
    if form.is_valid():
        form.save()
        messages.success(request, "Route modifiée avec succès !")
        return redirect('route_list')
    return render(request, 'traffic/route_form.html', {'form': form, 'title': 'Modifier la route'})

@login_required
def route_delete(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == 'POST':
        route.delete()
        messages.success(request, "Route supprimée.")
        return redirect('route_list')
    return render(request, 'traffic/confirm_delete.html', {'obj': route, 'type': 'Route'})

@login_required
def intersection_list(request):
    intersections = Intersection.objects.select_related('zone').all()
    return render(request, 'traffic/intersection_list.html', {'intersections': intersections})

@login_required
def intersection_create(request):
    form = IntersectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Intersection ajoutée !")
        return redirect('intersection_list')
    return render(request, 'traffic/route_form.html', {'form': form, 'title': 'Ajouter une intersection'})
