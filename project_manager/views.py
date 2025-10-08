from django.shortcuts import redirect, render
from .models import Projet
from .forms import TaskFormSet


def index(request):
    projets = Projet.objects.all()
    return render(request, 'project_manager/index.html', {'projets': projets})


def projet_detail(request, pk):
    projet = Projet.objects.get(id=pk)
    
    if request.method == 'POST':
        formset = TaskFormSet(request.POST, instance=projet)
        if formset.is_valid():
            formset.save()
    
    # On recharge toujours le formset depuis la DB (après POST ou pour GET)
    formset = TaskFormSet(instance=projet)
    
    # Si requête HTMX, on retourne juste le partial
    if request.headers.get('HX-Request'):
        return render(request, 'project_manager/partials/formset.html', {'projet': projet, 'formset': formset})
    
    # Sinon on retourne la page complète
    return render(request, 'project_manager/project.html', {'projet': projet, 'formset': formset})
