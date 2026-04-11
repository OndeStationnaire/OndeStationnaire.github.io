#!/usr/bin/env python3
"""
parse_blog.py
Lit blog_contenu.md et génère les fichiers Jekyll dans _posts/

Format source attendu :
    ### 2026.03.11.Mer.
    Texte direct (post sans titre)

    ### 2026.03.15.Dim.
    #### Titre du post
    Texte du post
"""

import re
import os
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────────

SOURCE_FILE = "blog_contenu.md"
OUTPUT_DIR  = "_posts"

# Correspondance jour abrégé → numéro (pour validation optionnelle)
JOURS = {"Lun": "Mon", "Mar": "Tue", "Mer": "Wed",
         "Jeu": "Thu", "Ven": "Fri", "Sam": "Sat", "Dim": "Sun"}

# ── Fonctions utilitaires ──────────────────────────────────────────────────────

def slugify(texte: str) -> str:
    """Convertit un titre en slug compatible Jekyll."""
    import unicodedata
    texte = unicodedata.normalize("NFD", texte)
    texte = texte.encode("ascii", "ignore").decode("ascii")
    texte = texte.lower()
    texte = re.sub(r"[^\w\s-]", "", texte)
    texte = re.sub(r"[\s_]+", "-", texte).strip("-")
    return texte

def parse_date(date_str: str):
    """
    Extrait la date depuis une chaîne de format variable.
    Accepte : 2026.04.11.Sam. / 2026.04.06.Lun / 2026.04.04. / 2026.03.06
    Retourne '2026-04-11' ou None si invalide.
    """
    m = re.match(r"(\d{4})\.(\d{2})\.(\d{2})", date_str.strip())
    if not m:
        return None
    annee, mois, jour = m.groups()
    return f"{annee}-{mois}-{jour}"

def front_matter(date_iso: str, title: str = None) -> str:
    """Génère le front matter Jekyll."""
    lines = ["---", "layout: post", f"date: {date_iso}"]
    if title:
        lines.append(f'title: "{title}"')
    lines.append("---")
    return "\n".join(lines)

def write_post(date_iso: str, title: str, body: str, index: int):
    """Écrit un fichier post dans _posts/."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if title:
        slug = slugify(title)
    else:
        slug = f"entree-{index:02d}"

    # Éviter les collisions si plusieurs posts le même jour
    filename = f"{date_iso}-{slug}.md"
    filepath = Path(OUTPUT_DIR) / filename

    # Ne pas écraser si le contenu est identique
    fm = front_matter(date_iso, title)
    content = f"{fm}\n\n{body.strip()}\n"

    if filepath.exists() and filepath.read_text(encoding="utf-8") == content:
        return False  # Pas de changement

    filepath.write_text(content, encoding="utf-8")
    print(f"  ✓ {filename}")
    return True

# ── Parser principal ───────────────────────────────────────────────────────────

def parse_blog(source_path: str):
    text = Path(source_path).read_text(encoding="utf-8")

    # Découpe par entrées de date (### AAAA.MM.JJ.Xxx.)
    sections = re.split(r"^###\s+", text, flags=re.MULTILINE)

    total = 0

    for section in sections:
        if not section.strip():
            continue

        lines = section.splitlines()
        header = lines[0].strip()

        date_iso = parse_date(header)
        if not date_iso:
            continue
        
        print(f"  → Section trouvée : {date_iso}")  # DEBUG
        
        body_raw = "\n".join(lines[1:]).strip()

        if not body_raw:
            continue

        # Cherche des sous-titres #### dans le corps
        sous_sections = re.split(r"^####\s+", body_raw, flags=re.MULTILINE)

        if len(sous_sections) == 1:
            # Pas de sous-titre → post sans titre
            ecrit = write_post(date_iso, None, sous_sections[0], total + 1)
            if ecrit:
                total += 1
        else:
            # Première partie avant le premier #### (souvent vide)
            intro = sous_sections[0].strip()
            if intro:
                ecrit = write_post(date_iso, None, intro, total + 1)
                if ecrit:
                    total += 1

            # Chaque sous-section #### devient un post
            for sous in sous_sections[1:]:
                sous_lines = sous.splitlines()
                titre = sous_lines[0].strip()
                corps = "\n".join(sous_lines[1:]).strip()
                ecrit = write_post(date_iso, titre, corps, total + 1)
                if ecrit:
                    total += 1

    print(f"\n{total} fichier(s) généré(s) dans {OUTPUT_DIR}/")

# ── Point d'entrée ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    source = sys.argv[1] if len(sys.argv) > 1 else SOURCE_FILE

    if not Path(source).exists():
        print(f"Erreur : fichier source '{source}' introuvable.")
        sys.exit(1)

    print(f"Parsing de {source}...")
    parse_blog(source)
