# Plan d'intégration — Zoom Virtual Agent

Ce document décrit les étapes complètes pour connecter le vault Camp Bruchési à **Zoom Virtual Agent (ZVA)** afin de créer un chatbot qui répond automatiquement aux questions des parents et des familles.

---

## Vue d'ensemble

```
Parent pose une question
        ↓
Zoom Virtual Agent (ZVA)
        ↓
Web Sync crawle le vault
        ↓
https://ndelorimier.github.io/vault-camp-bruchesi/
        ↓
Réponse générée + lien vers la page source
```

ZVA fonctionne via **Web Sync** : il indexe le site public du vault, puis utilise cet index pour répondre aux questions. Pas de code à écrire, pas d'API à brancher — c'est une configuration dans le portail Zoom Admin.

---

## Prérequis

| Élément | État |
|---------|------|
| Vault public en ligne | ✅ `https://ndelorimier.github.io/vault-camp-bruchesi/` |
| Sitemap.xml automatique | ✅ Généré par MkDocs à `…/sitemap.xml` |
| Contenu structuré en FR | ✅ |
| Licence Zoom avec Virtual Agent | ❓ À vérifier dans ton compte Zoom |

!!! info "Licence ZVA"
    Zoom Virtual Agent est disponible avec Zoom Contact Center ou en module complémentaire. Vérifie dans ton portail Zoom si le module est actif : **admin.zoom.us → Produits → Virtual Agent**.

---

## Étape 1 — Activer Zoom Virtual Agent

1. Aller sur [admin.zoom.us](https://admin.zoom.us)
2. Menu gauche → **Virtual Agent**
3. Si absent : **Produits** → activer **Zoom Virtual Agent** (ou contacter ton représentant Zoom)

---

## Étape 2 — Créer un bot

1. Dans Virtual Agent → **Créer un bot**
2. Nom : `Assistant Camp Bruchési`
3. Langue : **Français**
4. Icône / avatar : logo du camp (optionnel)
5. Message de bienvenue suggéré :
   > *Bonjour ! Je suis l'assistant du Camp Bruchési. Je peux vous aider avec les programmes, les tarifs, l'inscription et les questions fréquentes. Comment puis-je vous aider ?*

---

## Étape 3 — Configurer Web Sync (source de données)

C'est l'étape centrale : ZVA va crawler le vault et construire sa base de connaissances automatiquement.

1. Dans le bot → **Sources de connaissances** → **Ajouter une source web**
2. URL racine : `https://ndelorimier.github.io/vault-camp-bruchesi/`
3. Sitemap : `https://ndelorimier.github.io/vault-camp-bruchesi/sitemap.xml`
4. Fréquence de resynchronisation : **Hebdomadaire** (ou manuelle après chaque mise à jour importante)
5. Lancer la première synchronisation → attendre l'indexation (5–15 minutes selon la taille)

### Pages qui seront indexées automatiquement

| Section | URL | Contenu clé |
|---------|-----|-------------|
| Accueil | `/` | Vue d'ensemble |
| Séjours | `/sejours/` | Programmes, âges |
| Calendrier | `/sejours/calendrier/` | Dates 2026 |
| Tarifs | `/sejours/inscription/` | Prix, annulations |
| Transport | `/sejours/transport/` | Arrêts, horaires |
| Quoi apporter | `/sejours/quoi-apporter/` | Listes bagages |
| Groupes scolaires | `/sejours/groupes-scolaires/` | Classes vertes/neige |
| Emploi | `/sejours/emploi/` | Postes, PAM |
| Hébergement | `/services/hebergement/` | Manoir, Maison du lac |
| Activités | `/services/activites/` | Sports, nature |
| Restauration | `/services/restauration/` | Menus, allergies |
| FAQ | `/faq/` | Questions fréquentes |
| Contact | `/contact/` | Coordonnées, heures |

### Pages à exclure du Web Sync

La section **Formation (Staff)** ne devrait pas être indexée par ZVA public — elle contient du contenu interne. Ajouter ces URL en **exclusions** dans la config Web Sync :

```
https://ndelorimier.github.io/vault-camp-bruchesi/formation/
```

---

## Étape 4 — Configurer les intentions (intents)

Après l'indexation, tester et créer des intentions pour les questions les plus fréquentes. ZVA peut suggérer des intentions automatiquement à partir du contenu crawlé.

### Intentions recommandées à créer manuellement

| Intent | Exemples de questions | Page source |
|--------|----------------------|-------------|
| Tarifs programmes | "Combien coûte le camp ?", "Quel est le prix pour les Aventuriers ?" | `/sejours/inscription/` |
| Inscription | "Comment inscrire mon enfant ?", "Où s'inscrire ?" | `/sejours/inscription/` |
| Allergies | "Mon enfant est allergique, peut-il venir ?", "Accommodez-vous le sans-gluten ?" | `/services/restauration/` |
| Cellulaires | "Mon enfant peut-il avoir son téléphone ?" | `/faq/` |
| Annulation | "Quelle est la politique d'annulation ?" | `/sejours/inscription/` |
| Transport | "Y a-t-il un autobus ?" | `/sejours/transport/` |
| Quoi apporter | "Qu'est-ce qu'on apporte au camp ?" | `/sejours/quoi-apporter/` |
| Emploi | "Comment travailler au camp ?", "Engagez-vous des animateurs ?" | `/sejours/emploi/` |
| Calendrier | "Quand commence le camp ?", "C'est quoi les dates ?" | `/sejours/calendrier/` |
| Contact | "Quel est le numéro de téléphone ?", "Vos heures d'ouverture ?" | `/contact/` |

---

## Étape 5 — Configurer l'escalade humaine

Pour les questions que ZVA ne peut pas répondre, configurer l'escalade vers un humain :

1. Bot settings → **Fallback / Escalade**
2. Message de fallback :
   > *Je n'ai pas trouvé de réponse à votre question. Vous pouvez nous joindre directement : **(450) 563-3056** ou **info@campbruchesi.ca** (lundi–vendredi 8h–17h).*
3. Si tu as Zoom Contact Center actif : activer le transfert vers un agent humain

---

## Étape 6 — Déployer le bot

### Option A — Widget sur le site web du camp (recommandé)
1. Dans ZVA → **Canaux** → **Widget web**
2. Personnaliser les couleurs (vert `#00c853` pour matcher l'identité du camp)
3. Copier le snippet JavaScript généré
4. L'intégrer dans le code du site campbruchesi.ca (une ligne dans le `<body>`)

### Option B — Zoom Chat (interne)
Si tu veux d'abord tester sans toucher au site web :
1. Déployer sur **Zoom Team Chat** → les membres de ton équipe Zoom peuvent interroger le bot
2. Permet de valider les réponses avant de l'exposer aux parents

### Option C — Lien direct
ZVA génère un lien direct vers le bot (format `https://zoom.us/...`). Tu peux le partager dans les courriels aux parents pour tester.

---

## Étape 7 — Tester avec les questions de référence

Avant de déployer, tester ces questions manuellement dans le bot :

**Tarifs et programmes**
- "Quel est le tarif pour les Aventuriers 12 nuits ?"
- "Y a-t-il un rabais pour le 2e enfant ?"
- "Quel programme pour un enfant de 5 ans ?"

**Inscription et logistique**
- "Comment s'inscrire ?"
- "Qu'est-ce qu'on apporte au camp de vacances ?"
- "Est-ce qu'il y a un autobus depuis Prévost ?"

**Sécurité et santé**
- "Mon enfant est allergique au soya, peut-il venir en camp de vacances ?"
- "Comment fonctionne la baignade ?"
- "Est-ce que les cellulaires sont permis ?"

**Emploi**
- "Comment travailler comme animateur ?"
- "Quel est l'âge minimum pour être animateur ?"

**Pour chaque réponse, vérifier :**
- ✅ La réponse est correcte et complète
- ✅ La source citée est la bonne page du vault
- ✅ Le ton est approprié (français, professionnel mais accessible)
- ✅ Les informations de contact sont mentionnées si la réponse est incomplète

---

## Maintenance du bot

| Action | Quand | Qui |
|--------|-------|-----|
| Resynchronisation Web Sync | Après chaque mise à jour du vault | Automatique (hebdo) ou manuelle |
| Révision des intents | Début de saison | Responsable vault |
| Mise à jour des tarifs | Novembre–décembre | Responsable vault |
| Revue des questions non répondues | Mensuelle | Responsable vault |

### Voir les questions non répondues
ZVA garde un log des questions auxquelles le bot n'a pas su répondre. Ces logs sont précieux : ils indiquent exactement quel contenu ajouter au vault.

Dans le portail ZVA → **Analytiques** → **Questions non résolues**

---

## Résumé — Ce que tu dois faire

```
1. [ ] Vérifier que tu as une licence ZVA dans ton compte Zoom
2. [ ] Créer le bot (10 min)
3. [ ] Configurer Web Sync → URL du vault (5 min)
4. [ ] Exclure /formation/ du crawl (2 min)
5. [ ] Attendre l'indexation (15 min)
6. [ ] Tester les 10 questions de référence (20 min)
7. [ ] Déployer sur le canal de ton choix
```

**Durée totale estimée : ~1 heure** une fois la licence confirmée.
