# Tâches — Vault Camp Bruchési (Base de connaissances MkDocs)
> Fichier de suivi. Mettre à jour à chaque session.
> Format : - [ ] à faire · - [x] complété · - [~] en cours

---

## ✅ Session 2026-05-07 — Mise en place initiale

- [x] Créer le repo `vault-camp-bruchesi` sur GitHub (public)
- [x] Structure MkDocs Material (thème vert, FR, mode sombre/clair, recherche)
- [x] Structure de navigation : Séjours, Services, FAQ, Contact
- [x] GitHub Actions — workflow auto-deploy (`gh-pages` branch) sur push `main`
- [x] GitHub Pages activé et fonctionnel
- [x] Intégrer les vraies informations du camp (campbruchesi.ca + monportail)
  - [x] Coordonnées réelles (adresse, tél, courriel, heures)
  - [x] Tous les programmes avec tarifs réels
  - [x] Calendrier 2026 complet
  - [x] Ratios animateur/enfants (vacances et jour)
  - [x] Hébergement détaillé (dortoirs, Manoir, tipis, Maison du lac)
  - [x] Restauration (végétarien, allergies non supportées, dîner traiteur)
  - [x] Politiques d'annulation camp de jour ET camp de vacances
  - [x] FAQ complète depuis les accordéons du site (cellulaires, moniteurs, test de nage, etc.)
  - [x] Tarifs groupes scolaires (classes vertes/neige)
  - [x] Tarifs hébergement (Manoir, Maison du lac, Campement)
  - [x] Programme Sauveteur (prérequis, subventions, reprise examen)
  - [x] Programme PAM — Aspirant-moniteur (200h, DAFA, débouchés)
  - [x] Programmes saisonniers (Noël, Relâche, Répit Weekend)
  - [x] Rabais familles (2e -20%, 3e -50%, 4e gratuit/50%)

---

## ✅ Session 2026-05-08 — Vault public Phase 1 + Formation staff Phase 2

- [x] docs/sejours/transport.md (arrêts Décampe : Lac Connoly, IGA Saint-Hippolyte, Foccacia, IGA Prévost, Place de la station)
- [x] docs/sejours/quoi-apporter.md (listes par programme)
- [x] docs/sejours/groupes-scolaires.md (classes vertes/neige, tarifs)
- [x] docs/formation/index.md
- [x] docs/formation/nouveau-animateur.md
- [x] docs/formation/code-ethique.md
- [x] docs/formation/protocoles/urgences.md
- [x] docs/formation/protocoles/signalement.md
- [x] docs/formation/protocoles/sante.md
- [x] docs/formation/protocoles/garde-nuit.md
- [x] docs/formation/ressources-aide.md

---

## ✅ Session 2026-05-11 — Contenu complémentaire + Plan ZVA

- [x] docs/sejours/transport.md — ajout arrêts réels Décampe
- [x] docs/sejours/mission-valeurs.md
- [x] docs/sejours/emploi.md
- [x] docs/sejours/corporatif.md
- [x] Navigation mkdocs.yml mise à jour (toutes nouvelles pages)
- [x] Plan d'intégration Zoom Virtual Agent documenté → voir `docs/integration/zoom-virtual-agent.md`

---

## 🌐 Priorité — Zoom Virtual Agent

Voir le plan complet : [docs/integration/zoom-virtual-agent.md](docs/integration/zoom-virtual-agent.md)

**Ce que tu dois faire (accès requis) :**
1. [ ] Accéder au portail Zoom Admin : admin.zoom.us
2. [ ] Activer Zoom Virtual Agent dans les produits
3. [ ] Créer un bot et configurer Web Sync → URL : `https://ndelorimier.github.io/vault-camp-bruchesi/`
4. [ ] Tester avec les questions de référence (voir plan)
5. [ ] Déployer sur le canal de ton choix (site web, Zoom chat)

**Optionnel mais recommandé avant :**
- [ ] Domaine personnalisé (`docs.campbruchesi.ca`) pour une URL plus propre dans ZVA

---

## 📄 Contenu manquant (nécessite info de ta part)

- [ ] **Page Los Bruchos** — informations du programme non disponibles
- [ ] **Page Répits Plus** — informations du programme non disponibles
- [ ] **Points de ramassage complets** — arrêts pour autres programmes (camp de jour Découverte, camp de vacances)
- [ ] **Sous-pages par programme vacances** — si tu veux des pages dédiées détaillées

---

## 🎨 Améliorations visuelles (optionnel)

- [ ] Logo du camp + favicon
- [ ] Photos d'activités dans les pages
- [ ] Domaine personnalisé (`docs.campbruchesi.ca` ou `kb.campbruchesi.ca`)
- [ ] Analytics (Google Analytics ou Plausible)

---

## 🔄 Maintenance continue

- [ ] Mettre à jour tarifs et calendrier pour la saison 2027 (novembre 2026)
- [ ] Valider les informations avec l'équipe avant chaque saison
- [ ] Synchroniser conditions d'annulation si elles changent
