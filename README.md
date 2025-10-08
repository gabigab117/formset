# Django InlineFormSet - Exemple Pratique

## 📋 Description

Ce projet est un exemple d'utilisation des **InlineFormSet** de Django. Il démontre comment gérer plusieurs formulaires liés à un objet parent dans une seule vue, permettant la modification en masse de tâches associées à un projet.

## 🎯 Fonctionnalités

- Création et gestion de projets
- Ajout de tâches associées à chaque projet
- **Édition en masse** de plusieurs tâches directement depuis le projet parent
- Ajout de nouvelles tâches via le formulaire inline
- Suppression de tâches existantes
- Marquage des tâches comme complètes/incomplètes

## 🏗️ Structure du Projet

Le projet contient deux modèles principaux :
- **Projet** : représente un projet avec un nom
- **Task** : représente une tâche liée à un projet via une ForeignKey (titre, statut de complétion)

### Le InlineFormSet

Le cœur de ce projet est l'utilisation de `inlineformset_factory` qui permet de :
- Éditer plusieurs objets Task liés à un Projet simultanément
- Ajouter de nouvelles tâches directement dans le formulaire
- Gérer les modifications en une seule requête POST
- Supprimer des tâches existantes via l'interface

```python
TaskFormSet = inlineformset_factory(
    Projet,        # Modèle parent
    Task,          # Modèle enfant (lié par ForeignKey)
    fields=('titre', 'complete'),
    extra=1,       # Nombre de formulaires vides pour ajouter de nouvelles tâches
    can_delete=True
)
```

### Différence avec ModelFormSet

**InlineFormSet** est spécifiquement conçu pour gérer des relations parent-enfant :
- Utilise automatiquement la relation ForeignKey
- Simplifie le code de la vue avec `instance=projet`
- Gère automatiquement l'association avec le projet parent

## 🚀 Installation

1. Cloner le repository et basculer sur cette branche
```bash
git clone <url-du-repo>
cd formset
git checkout 1-add-inline
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

1. Accéder à l'admin Django (`/admin`) pour créer des projets
2. Visiter la page d'accueil pour voir la liste des projets
3. Cliquer sur un projet pour voir et éditer ses tâches
4. Modifier les tâches existantes, ajouter de nouvelles tâches, ou supprimer des tâches
5. Cliquer sur "Enregistrer les tâches" pour valider toutes les modifications en une fois

## 📚 Apprentissage

Ce projet est idéal pour comprendre :
- Les **InlineFormSet** de Django
- La différence entre ModelFormSet et InlineFormSet
- La gestion de relations parent-enfant dans les formulaires
- Les relations ForeignKey
- L'édition en masse de données liées

## 🔧 Technologies

- Django 5.x
- Python 3.13
- SQLite

## 🔀 Autres Branches

- **`main`** : Utilise `modelformset_factory` (approche plus générique)
- **`1-add-inline`** : Utilise `inlineformset_factory` (cette branche - pour relations parent-enfant)
