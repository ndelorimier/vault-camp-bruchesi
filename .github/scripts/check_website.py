"""
Surveillance automatique du site campbruchesi.ca
Compare le contenu des pages avec des snapshots stockés en repo.
Signale les changements via GitHub Actions outputs.
"""

import requests
import hashlib
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime

# Pages à surveiller
PAGES = {
    "Accueil": "https://www.campbruchesi.ca/",
    "Camp de vacances": "https://www.campbruchesi.ca/camp-de-vacances/",
    "Camp de jour": "https://www.campbruchesi.ca/camp-de-jour/",
    "Tarifs": "https://www.campbruchesi.ca/tarifs/",
    "PAM — Aspirant-moniteur": "https://www.campbruchesi.ca/camp-de-vacances-pam/",
    "Transport camp de jour": "https://www.campbruchesi.ca/camp-de-jour-transport/",
    "À propos": "https://www.campbruchesi.ca/a-propos/",
    "Accessibilité financière": "https://www.campbruchesi.ca/accessibilite-financiere/",
    "Manoir": "https://www.campbruchesi.ca/manoir/",
    "Maison du lac": "https://www.campbruchesi.ca/maison-du-lac/",
    "Emploi": "https://www.campbruchesi.ca/emploi/",
    "Groupes scolaires": "https://www.campbruchesi.ca/classes-vertes/",
    "Répit Weekend": "https://www.campbruchesi.ca/repit-weekend/",
    "Camp de Noël": "https://www.campbruchesi.ca/camp-de-noel/",
    "Corporatif": "https://www.campbruchesi.ca/corporatif/",
}

SNAPSHOTS_FILE = ".github/website-snapshots.json"
ISSUE_BODY_FILE = "/tmp/issue_body.txt"


def get_page_hash(url: str) -> str | None:
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (compatible; VaultBot/1.0; "
                "+https://github.com/ndelorimier/vault-camp-bruchesi)"
            )
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Retirer les éléments non-contenus (nav, footer, scripts, styles)
        for tag in soup(["script", "style", "nav", "footer", "header", "meta", "link"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        return hashlib.sha256(text.encode("utf-8")).hexdigest()
    except Exception as e:
        print(f"  ⚠️  Erreur pour {url}: {e}")
        return None


def main():
    # Charger les snapshots existants
    if os.path.exists(SNAPSHOTS_FILE):
        with open(SNAPSHOTS_FILE, "r", encoding="utf-8") as f:
            snapshots = json.load(f)
        is_first_run = False
    else:
        snapshots = {}
        is_first_run = True

    changed_pages = []
    unreachable_pages = []
    new_snapshots = dict(snapshots)

    print(f"{'=' * 60}")
    print(f"Surveillance campbruchesi.ca — {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC")
    print(f"{'=' * 60}\n")

    for name, url in PAGES.items():
        print(f"→ {name}")
        print(f"  {url}")
        new_hash = get_page_hash(url)

        if new_hash is None:
            print(f"  ❌ Page inaccessible\n")
            unreachable_pages.append({"name": name, "url": url})
            continue

        old_hash = snapshots.get(name)

        if old_hash is None:
            print(f"  ✅ Premier snapshot enregistré\n")
            new_snapshots[name] = new_hash
        elif old_hash != new_hash:
            print(f"  🔔 CHANGEMENT DÉTECTÉ\n")
            changed_pages.append({"name": name, "url": url})
            new_snapshots[name] = new_hash
        else:
            print(f"  ✅ Aucun changement\n")

    # Sauvegarder les snapshots mis à jour
    os.makedirs(os.path.dirname(SNAPSHOTS_FILE), exist_ok=True)
    with open(SNAPSHOTS_FILE, "w", encoding="utf-8") as f:
        json.dump(new_snapshots, f, indent=2, ensure_ascii=False)
    print(f"Snapshots mis à jour: {SNAPSHOTS_FILE}")

    # Résumé
    print(f"\n{'=' * 60}")
    print(f"Résultat: {len(changed_pages)} changement(s) détecté(s)")
    if unreachable_pages:
        print(f"Pages inaccessibles: {len(unreachable_pages)}")
    print(f"{'=' * 60}")

    # Préparer le corps de l'issue si des changements sont détectés
    github_output = os.environ.get("GITHUB_OUTPUT", "/dev/null")

    if changed_pages and not is_first_run:
        date_str = datetime.now().strftime("%Y-%m-%d à %H:%M")
        lines = [
            f"## 🔔 Changements détectés sur campbruchesi.ca",
            f"",
            f"**Détecté le :** {date_str} UTC",
            f"",
            f"Les pages suivantes ont été modifiées depuis la dernière vérification. "
            f"Vérifier si la voûte doit être mise à jour.",
            f"",
            f"### Pages modifiées",
            f"",
        ]
        for page in changed_pages:
            lines.append(f"- [ ] **{page['name']}** — [{page['url']}]({page['url']})")

        if unreachable_pages:
            lines.append(f"")
            lines.append(f"### Pages inaccessibles lors de cette vérification")
            lines.append(f"")
            for page in unreachable_pages:
                lines.append(f"- ⚠️ {page['name']} — {page['url']}")

        lines += [
            f"",
            f"---",
            f"",
            f"**Prochaines étapes :**",
            f"1. Consulter chaque page modifiée",
            f"2. Identifier les changements de contenu (tarifs, dates, programmes...)",
            f"3. Mettre à jour le fichier correspondant dans la voûte",
            f"4. Fermer cette issue une fois les mises à jour effectuées",
            f"",
            f"_Généré automatiquement par le [workflow de surveillance]"
            f"(https://github.com/ndelorimier/vault-camp-bruchesi/actions)_",
        ]

        issue_body = "\n".join(lines)
        with open(ISSUE_BODY_FILE, "w", encoding="utf-8") as f:
            f.write(issue_body)

        with open(github_output, "a") as f:
            f.write("changes=true\n")
    else:
        with open(github_output, "a") as f:
            f.write("changes=false\n")

        if is_first_run:
            print("\nPremière exécution — snapshots initialisés. Aucune issue créée.")


if __name__ == "__main__":
    main()
