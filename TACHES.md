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

## 🌐 Domaine et intégrations

- [ ] **Configurer un domaine custom** (ex : `docs.campbruchesi.ca` ou `kb.campbruchesi.ca`)
  - Dans GitHub : Settings → Pages → Custom domain
  - Chez le registraire DNS : ajouter un CNAME `ndelorimier.github.io`
- [ ] **Connecter Zoom Virtual Agent (ZVA)** via Web Sync
  - Configurer la source de données ZVA → pointer vers `https://ndelorimier.github.io/vault-camp-bruchesi/`
  - Valider l'indexation des pages (FAQ, séjours, services)
  - Tester les réponses du bot sur les questions fréquentes

---

## 📄 Contenu à ajouter

- [ ] **Page Los Bruchos** — décrire le programme (informations manquantes)
- [ ] **Page Répits Plus** — décrire le programme
- [ ] **Page Transport** — points de ramassage autobus par programme et ville
  - Arrêts Décampe mentionnés : Lac Connoly, IGA Saint-Hippolyte, Restaurant Foccacia, IGA Prévost, Place de la station
- [ ] **Page Groupes scolaires** dédiée — classes vertes, classes rouges, classes neige avec détails pédagogiques
- [ ] **Page Corporatif / Accueil de groupes** — offre d'entreprise, team building
- [ ] **Page Emploi** — postes disponibles, conditions, comment postuler
- [ ] **Page Campement scouts/cadets** — conditions, capacité, tarifs
- [ ] **Sous-pages par programme vacances** (Bourlingueurs, Aventuriers, etc.)
  - Ce qui est inclus, une nuit camping, dortoirs, etc.
- [ ] **Page Mission et valeurs** — histoire depuis 1928, OBNL Plein air Bruchési, conseil d'administration

---

## 🎨 Améliorations du site

- [ ] Ajouter des photos/images dans les pages (logo du camp, photos d'activités)
- [ ] Vérifier rendu mobile (MkDocs Material est responsive par défaut)
- [ ] Ajouter un `favicon` aux couleurs du camp
- [ ] Configurer `extra.analytics` (Google Analytics ou Plausible) si souhaité
- [ ] Revoir la navigation : envisager des onglets pour Camp de jour / Camp de vacances

---

## 🔄 Maintenance continue

- [ ] Mettre à jour les tarifs et calendriers pour la saison 2027
- [ ] Valider les informations avec l'équipe avant chaque saison
- [ ] Ajouter les nouveaux programmes si le camp en crée
- [ ] Synchroniser les conditions d'annulation si elles changent
