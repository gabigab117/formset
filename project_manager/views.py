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
            return redirect('projet_detail', pk=projet.id)
    else:
        formset = TaskFormSet(instance=projet)
    return render(request, 'project_manager/project.html', {'projet': projet, 'formset': formset})
