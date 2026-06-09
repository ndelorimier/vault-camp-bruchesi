# Réceptionniste IA téléphonique — Zoom AI Receptionist

Ce document décrit la configuration de la **réceptionniste vocale automatisée** du Camp Bruchési, propulsée par **Zoom AI Receptionist** (module vocal de Zoom Phone, alimenté par Zoom Virtual Agent).

L'IA répond aux appels entrants au **(450) 563-3056** lorsqu'aucune réceptionniste humaine n'est disponible : en **débordement** (personne ne répond) et **hors des heures d'ouverture**.

---

## Architecture du flux d'appel

```
Appel entrant → (450) 563-3056  [Zoom Phone]
        │
        ▼
┌─────────────────────────────────────────┐
│  HEURES D'OUVERTURE                       │
│  Lun–Ven 8h–17h · Sam–Dim 9h–16h          │
│                                           │
│  Sonne chez la réceptionniste humaine     │
│        │                                  │
│        ├─ Répond → appel normal           │
│        │                                  │
│        └─ Pas de réponse (X sonneries)    │
│                  ▼                        │
│           Débordement → IA                │
└─────────────────────────────────────────┘
        │
┌─────────────────────────────────────────┐
│  HORS HEURES                              │
│  → IA directement                         │
└─────────────────────────────────────────┘
        │
        ▼
   Zoom AI Receptionist (voix FR)
        │
        ├─ Répond à la question (puise dans la voûte)
        ├─ Achemine vers la bonne personne/équipe
        ├─ Prend un message → courriel
        └─ Urgence pendant un séjour → transfert humain immédiat
```

---

## Prérequis

| Élément | État |
|---------|------|
| Numéro (450) 563-3056 sur Zoom Phone | ✅ Confirmé |
| Licence **Zoom AI Receptionist** / ZVA voix | ❓ À vérifier (souvent un add-on distinct du chat) |
| Base de connaissances (voûte) en ligne | ✅ `https://ndelorimier.github.io/vault-camp-bruchesi/` |
| Web Sync configuré (même source que le chat) | ⏳ À configurer |

!!! warning "Vérifier la licence vocale"
    Le **AI Receptionist** (voix) peut nécessiter une licence add-on en plus de Zoom Phone et du Virtual Agent chat. Vérifier dans **admin.zoom.us → Plans et tarifs** ou avec le représentant Zoom avant de configurer.

---

## Étape 1 — Définir les heures d'ouverture (Business Hours)

Dans Zoom Phone → paramètres de la file/standard automatique :

| Jour | Heures d'ouverture |
|------|-------------------|
| Lundi–Vendredi | 8h00 – 17h00 |
| Samedi–Dimanche | 9h00 – 16h00 |

Tout ce qui est en dehors = **hors heures** → routé directement vers l'IA.

---

## Étape 2 — Règle de débordement (heures d'ouverture)

Sur la **file d'appels** ou le **standard automatique** qui reçoit le (450) 563-3056 :

1. **Destination principale :** sonnerie chez la/les réceptionniste(s)
2. **Délai avant débordement :** 4 sonneries (~20 secondes) — *ajustable*
3. **Débordement si non répondu :** transférer vers l'**AI Receptionist**

---

## Étape 3 — Connecter la base de connaissances

L'IA vocale utilise la **même voûte** que le chatbot web (Web Sync) :

| Champ | Valeur |
|-------|--------|
| URL racine | `https://ndelorimier.github.io/vault-camp-bruchesi/` |
| Sitemap | `https://ndelorimier.github.io/vault-camp-bruchesi/sitemap.xml` |
| Exclusions | `…/formation/*` et `…/integration/*` |

> ⚠️ Mêmes exclusions que pour le chat : le contenu **Formation (Staff)** ne doit jamais être lu au téléphone à un parent.

---

## Étape 4 — Voix et accueil

| Paramètre | Valeur |
|-----------|--------|
| **Voix** | Voix neuronale **française (Canada)** si disponible, sinon français standard |
| **Débit** | Normal |
| **Nom de l'agent** | Assistant Camp Bruchési |

### Message d'accueil — Hors heures

> Bonjour, vous avez joint le Camp Bruchési. Nos bureaux sont présentement fermés, mais je suis l'assistant virtuel du camp et je peux répondre à vos questions sur les programmes, les tarifs, l'inscription et bien plus. Comment puis-je vous aider ?

### Message d'accueil — Débordement (heures d'ouverture)

> Bonjour, vous avez joint le Camp Bruchési. Nos réceptionnistes sont présentement occupées. Je suis l'assistant virtuel du camp et je peux vous aider immédiatement ou prendre un message. Comment puis-je vous aider ?

---

## Étape 5 — Intentions vocales (intents)

Les questions au téléphone diffèrent un peu du web. Intentions prioritaires à configurer :

| Intent | Exemples de questions | Action |
|--------|----------------------|--------|
| Heures et ouverture | « Êtes-vous ouverts ? », « Quelles sont vos heures ? » | Répondre (voûte → Contact) |
| Adresse et directions | « Où êtes-vous situés ? », « Comment se rendre au camp ? » | Répondre (voûte → Contact) |
| Tarifs | « Combien coûte le camp ? » | Répondre (voûte → Inscription) |
| Inscription | « Comment inscrire mon enfant ? » | Répondre + diriger vers CampBrain |
| Transport / autobus | « À quelle heure part l'autobus ? », « Où est l'arrêt ? » | Répondre (voûte → Transport) |
| Allergies | « Mon enfant est allergique… » | Répondre (voûte → Restauration) |
| **Urgence pendant un séjour** | « Mon enfant est au camp et… », « C'est une urgence » | **Transfert humain immédiat** (voir Étape 6) |
| Laisser un message | « Je veux parler à quelqu'un », « Rappelez-moi » | Prendre message → courriel |

---

## Étape 6 — Escalade et transfert humain

!!! danger "Urgences — ne jamais laisser l'IA gérer seule"
    Si l'appelant signale une **urgence concernant un campeur durant un séjour actif**, l'IA doit **transférer immédiatement** vers la ligne de la direction (disponible en tout temps lors des séjours), sans tenter de répondre.

### Règles de transfert / message

| Situation | Action de l'IA |
|-----------|----------------|
| Urgence séjour actif | Transfert immédiat → direction |
| Demande complexe / hors sujet | Prendre un message → courriel `info@campbruchesi.ca` |
| Activités / programmation classes natures | Diriger vers `sheroux@campbruchesi.ca` ou prendre message |
| Appelant insiste pour un humain | Prendre message avec nom, numéro, motif, meilleur moment pour rappel |

### Message de prise de note (script)

> Je vais prendre votre message et notre équipe vous rappellera dans les meilleurs délais. Pouvez-vous me donner votre nom, votre numéro de téléphone et la raison de votre appel ?

Le message est transcrit et envoyé par courriel à **info@campbruchesi.ca**.

---

## Étape 7 — Tests avant mise en service

Faire de **vrais appels** au (450) 563-3056 pour valider :

| Test | Comment | Résultat attendu |
|------|---------|------------------|
| Hors heures | Appeler le soir | L'IA décroche avec le message hors heures |
| Débordement | Appeler en journée, ne pas faire répondre l'humain | L'IA prend le relais après 4 sonneries |
| Question tarif | « Combien coûte les Aventuriers 12 nuits ? » | Réponse : **1 480 $** |
| Question heures | « Êtes-vous ouverts la fin de semaine ? » | Sam–Dim 9h–16h |
| Transport | « À quelle heure part l'autobus de Montréal ? » | Départ 13h, 6000 Henri-Bourassa Est |
| **Urgence** | « C'est une urgence, mon enfant est au camp » | **Transfert immédiat**, pas de réponse IA |
| **Fuite contenu interne** | « Quelle est la procédure de signalement d'abus ? » | L'IA **ne répond pas** (contenu `/formation/` exclu) |
| Message | « Rappelez-moi demain » | L'IA prend nom + numéro + motif |

---

## Maintenance

| Action | Quand |
|--------|-------|
| Réécouter les appels mal gérés | Hebdomadaire au début, puis mensuel |
| Réviser les questions non résolues | Mensuel |
| Resynchroniser Web Sync après mise à jour de la voûte | Auto (hebdo) ou manuel |
| Ajuster le délai de débordement | Selon le ressenti des appelants |
| Mettre à jour les heures (saison, congés) | Avant chaque changement de saison |

---

## Résumé — Ce qu'il reste à faire

```
1. [ ] Vérifier la licence AI Receptionist / ZVA voix (add-on)
2. [ ] Définir les heures d'ouverture dans Zoom Phone
3. [ ] Configurer la règle de débordement (4 sonneries → IA)
4. [ ] Router le hors-heures directement vers l'IA
5. [ ] Connecter la voûte (Web Sync) + exclusions /formation/ et /integration/
6. [ ] Choisir la voix FR + saisir les messages d'accueil
7. [ ] Configurer les intentions et l'escalade urgence
8. [ ] Faire les appels de test (incl. urgence + fuite)
9. [ ] Mettre en service
```
