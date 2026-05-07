# vault-camp-bruchesi

Base de connaissances officielle du Camp Bruchési — construite avec MkDocs Material, déployée automatiquement sur GitHub Pages.

🌐 **Site live** : https://ndelorimier.github.io/vault-camp-bruchesi/

---

## Contenu

| Section | Description |
|---------|-------------|
| **Séjours** | Tous les programmes (vacances + jour), calendrier 2026, tarifs, conditions d'annulation |
| **Services** | Hébergement, activités, restauration |
| **FAQ** | Questions fréquentes tirées des accordéons du site campbruchesi.ca |
| **Contact** | Coordonnées, heures, accès |

## Stack

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) — thème, navigation, recherche FR
- GitHub Actions — deploy automatique sur push vers `main`
- GitHub Pages — hébergement

## Déploiement local

```bash
pip install mkdocs-material
mkdocs serve        # http://localhost:8000
mkdocs build        # génère le dossier site/
```

## Suivi des tâches

Voir [TACHES.md](TACHES.md) pour l'état d'avancement et les prochaines étapes.
