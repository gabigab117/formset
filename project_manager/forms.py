from .models import Task
from django.forms import modelformset_factory


TaskFormSet = modelformset_factory(Task, 
                                   fields=('titre', 'complete'),
                                   extra=0,
                                   can_delete=True)
