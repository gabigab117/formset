from django.shortcuts import redirect, render
from .models import Projet, Task
from .forms import TaskFormSet


def index(request):
    projets = Projet.objects.all()
    return render(request, 'project_manager/index.html', {'projets': projets})


def projet_detail(request, pk):
    projet = Projet.objects.get(id=pk)
    tasks = projet.tasks.all()
    if request.method == 'POST':
        formset = TaskFormSet(request.POST, queryset=tasks)
        if formset.is_valid():
            formset.save()
            return redirect('projet_detail', pk=projet.id)
    else:
        formset = TaskFormSet(queryset=tasks)
    return render(request, 'project_manager/project.html', {'projet': projet, 'tasks': tasks, 'formset': formset})
