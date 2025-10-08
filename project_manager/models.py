from django.db import models


class Projet(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Projet"
        
    
class Task(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='tasks')
    titre = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titre
    
    class Meta:
        verbose_name = "Tâche"
