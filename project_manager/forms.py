from .models import Task, Projet
from django.forms import inlineformset_factory


TaskFormSet = inlineformset_factory(Projet, Task, fields=('titre', 'complete'), extra=1, can_delete=True)
