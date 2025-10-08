# Django ModelFormSet - Exemple Pratique

## 📋 Description

Ce projet est un exemple d'utilisation des **ModelFormSet** de Django. Il démontre comment gérer plusieurs formulaires simultanément dans une seule vue, permettant la modification en masse de tâches liées à un projet.

## 🎯 Fonctionnalités

- Création et gestion de projets
- Ajout de tâches associées à chaque projet
- **Édition en masse** de plusieurs tâches en une seule soumission de formulaire
- Suppression de tâches via le formset
- Marquage des tâches comme complètes/incomplètes

## 🏗️ Structure du Projet

Le projet contient deux modèles principaux :
- **Projet** : représente un projet avec un nom
- **Task** : représente une tâche liée à un projet (titre, statut de complétion)

### Le ModelFormSet

Le cœur de ce projet est l'utilisation de `modelformset_factory` qui permet de :
- Éditer plusieurs objets Task simultanément
- Gérer les modifications en une seule requête POST
- Supprimer des tâches via l'interface

```python
TaskFormSet = modelformset_factory(
    Task, 
    fields=('titre', 'complete'),
    extra=0,
    can_delete=True
)
```

## 🚀 Installation

1. Cloner le repository
```bash
git clone <url-du-repo>
cd formset
```

2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
```

3. Installer les dépendances
```bash
pip install django
```

4. Appliquer les migrations
```bash
python manage.py migrate
```

5. Créer un superutilisateur (optionnel)
```bash
python manage.py createsuperuser
```

6. Lancer le serveur
```bash
python manage.py runserver
```

## 💡 Utilisation

1. Accéder à l'admin Django (`/admin`) pour créer des projets et des tâches
2. Visiter la page d'accueil pour voir la liste des projets
3. Cliquer sur un projet pour voir et éditer ses tâches en masse
4. Modifier plusieurs tâches à la fois et cliquer sur "Enregistrer les tâches"

## 📚 Apprentissage

Ce projet est idéal pour comprendre :
- Les ModelFormSet de Django
- La gestion de formulaires multiples
- Les relations ForeignKey
- L'édition en masse de données

## 🔧 Technologies

- Django 5.x
- Python 3.13
- SQLite
