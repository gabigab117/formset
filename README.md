# Django InlineFormSet avec HTMX (1 Vue) - Exemple Pratique

## 📋 Description

Ce projet est un exemple d'utilisation des **InlineFormSet** de Django avec **HTMX** pour une expérience utilisateur interactive. Il démontre comment gérer plusieurs formulaires liés à un objet parent **dans une seule vue** qui gère à la fois les requêtes classiques et HTMX, permettant la modification en masse de tâches associées à un projet **sans rechargement complet de la page**.

## 🎯 Fonctionnalités

- Création et gestion de projets
- Ajout de tâches associées à chaque projet
- **Édition en masse** de plusieurs tâches directement depuis le projet parent
- Ajout de nouvelles tâches via le formulaire inline
- Suppression de tâches existantes
- Marquage des tâches comme complètes/incomplètes
- **Mise à jour asynchrone** avec HTMX (sans rechargement de page)
- **Interface réactive** : les modifications sont appliquées instantanément
- **Expérience utilisateur fluide** grâce à HTMX

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

### HTMX avec une seule vue

Cette branche utilise une approche **simplifiée** avec **une seule vue** qui détecte automatiquement le type de requête :
- **Soumission de formulaire asynchrone** : Le formset est envoyé via AJAX
- **Mise à jour partielle** : Seul le contenu du formset est rechargé (`hx-swap="innerHTML"`)
- **Templates partiels** : Utilisation de `partials/formset.html` pour le rendu partiel
- **Une seule vue intelligente** : 
  - Détecte si la requête vient de HTMX via `request.headers.get('HX-Request')`
  - Retourne le partial si requête HTMX
  - Retourne la page complète si requête classique

```python
def projet_detail(request, pk):
    projet = Projet.objects.get(id=pk)
    
    if request.method == 'POST':
        formset = TaskFormSet(request.POST, instance=projet)
        if formset.is_valid():
            formset.save()
    
    # On recharge toujours le formset depuis la DB
    formset = TaskFormSet(instance=projet)
    
    # Si requête HTMX, on retourne juste le partial
    if request.headers.get('HX-Request'):
        return render(request, 'project_manager/partials/formset.html', 
                      {'projet': projet, 'formset': formset})
    
    # Sinon on retourne la page complète
    return render(request, 'project_manager/project.html', 
                  {'projet': projet, 'formset': formset})
```

### Avantages de cette approche

✅ **Une seule URL** : `/projet/<pk>/` gère tout (GET et POST, HTMX et classique)  
✅ **Moins de code** : Pas besoin d'une vue séparée pour les mises à jour  
✅ **Plus simple à maintenir** : Logique centralisée dans une seule vue  
✅ **Graceful degradation** : Fonctionne même si HTMX échoue (rechargement classique)  
✅ **DRY** : Pas de duplication de logique entre deux vues

### Attributs HTMX utilisés

```html
<form 
    hx-post="{% url 'projet_detail' projet.id %}"
    hx-target="#formset"
    hx-swap="innerHTML"
>
```

- `hx-post` : Poste vers la **même URL** que la page (approche simplifiée)
- `hx-target` : Élément à mettre à jour (div avec id="formset")
- `hx-swap="innerHTML"` : Remplace le contenu du conteneur (garde la div, remplace le formulaire)

### Détection de requête HTMX

HTMX ajoute automatiquement un header `HX-Request` à toutes ses requêtes :
```python
if request.headers.get('HX-Request'):
    # C'est une requête HTMX, on retourne le partial
else:
    # C'est une requête classique, on retourne la page complète
```

## 🚀 Installation

1. Cloner le repository et basculer sur cette branche
```bash
git clone <url-du-repo>
cd formset
git checkout 5-htmx-in-1-view
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
5. Cliquer sur "Enregistrer les tâches" 
6. **✨ Les modifications sont appliquées instantanément sans rechargement de page grâce à HTMX !**

## 📚 Apprentissage

Ce projet est idéal pour comprendre :
- Les **InlineFormSet** de Django
- La différence entre ModelFormSet et InlineFormSet
- La gestion de relations parent-enfant dans les formulaires
- Les relations ForeignKey
- L'édition en masse de données liées
- **L'intégration de HTMX** dans un projet Django
- Les **requêtes AJAX** sans JavaScript explicite
- Le **rendu partiel de templates** (partials)
- La création d'**applications web réactives** avec Django + HTMX
- Les attributs HTMX (`hx-post`, `hx-target`, `hx-swap`)
- **La détection de requêtes HTMX** via les headers
- **Une architecture simplifiée** avec une seule vue pour GET et POST
- Le principe de **graceful degradation** (fonctionne avec et sans HTMX)

## 🔧 Technologies

- Django 5.x
- Python 3.13
- SQLite
- **HTMX 2.0.7** (via CDN)
- **Bootstrap 5.3.2** (via CDN)
- **Bootstrap Icons 1.11.3** (via CDN)

## 🔀 Autres Branches

- **`main`** : Utilise `modelformset_factory` - Rechargement de page classique
- **`1-add-inline`** : Utilise `inlineformset_factory` - Rechargement de page classique
- **`3-add-boostrap-5`** : InlineFormSet + Bootstrap 5 - Rechargement de page classique
- **`4-add-htmx-to-formset`** : InlineFormSet + Bootstrap 5 + HTMX (2 vues séparées)
- **`5-htmx-in-1-view`** : InlineFormSet + Bootstrap 5 + HTMX avec **1 seule vue** (cette branche) ⭐

## 🎯 Pourquoi HTMX ?

HTMX permet de créer des applications web modernes et réactives **sans écrire de JavaScript** :
- ✅ Soumissions de formulaires asynchrones
- ✅ Mises à jour partielles de la page
- ✅ Expérience utilisateur fluide
- ✅ Code simple et maintenable
- ✅ Pas besoin de frameworks JavaScript complexes (React, Vue, etc.)

## 🆚 Différence avec la branche 4-add-htmx-to-formset

| Caractéristique | Branche 4 (2 vues) | Branche 5 (1 vue) ⭐ |
|----------------|-------------------|---------------------|
| **Nombre de vues** | 2 (`projet_detail` + `update_tasks`) | 1 (`projet_detail`) |
| **Nombre d'URLs** | 2 URLs différentes | 1 URL unique |
| **Détection HTMX** | Via URL différente | Via header `HX-Request` |
| **Complexité** | Plus de code | Code simplifié |
| **Maintenance** | Logique dupliquée | Logique centralisée |
| **Graceful degradation** | Limitée | Automatique |

**Recommandation** : La branche 5 (cette branche) est l'approche **recommandée** pour sa simplicité et sa maintenabilité.
