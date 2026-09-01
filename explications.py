"""Charge les explications (chapitres du livre) pour les exemples Excel."""

from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
INDEX_PATH = BASE / "explications_index.json"

_index: dict | None = None


def _sans_numero_chapitre(texte: str) -> str:
    lignes = texte.splitlines()
    if lignes and lignes[0].startswith("## Chapitre "):
        m = re.match(r"## Chapitre \d+ — (.+)", lignes[0])
        if m:
            lignes[0] = f"## {m.group(1)}"
    texte = "\n".join(lignes)
    texte = re.sub(r"\(chapitre \d+\)", "", texte, flags=re.IGNORECASE)
    texte = re.sub(r"\bchapitre \d+\b", "", texte, flags=re.IGNORECASE)
    texte = re.sub(r"Ce chapitre ", "Ce cas ", texte)
    texte = re.sub(r"\n{3,}", "\n\n", texte)
    return texte.strip()


def _charger_index() -> dict:
    global _index
    if _index is None:
        if INDEX_PATH.exists():
            _index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        else:
            _index = {}
    return _index


def a_explication(nom_xlsx: str) -> bool:
    """True si une explication existe pour ce fichier .xlsx."""
    return nom_xlsx in _charger_index()


def titre_pour(nom_xlsx: str) -> str:
    meta = _charger_index().get(nom_xlsx) or {}
    titre = meta.get("titre") or "Explication du cas"
    return re.sub(r"^Chapitre \d+ — ", "", titre)


def charger_contenu(nom_xlsx: str) -> str | None:
    meta = _charger_index().get(nom_xlsx)
    if not meta:
        return None
    chemin = BASE / meta["fichier"]
    if not chemin.is_file():
        return None
    return _sans_numero_chapitre(chemin.read_text(encoding="utf-8"))


def contenu_pour_popup(nom_xlsx: str) -> str | None:
    """Contenu sans le titre H2 initial (déjà affiché dans l'en-tête du dialogue)."""
    contenu = charger_contenu(nom_xlsx)
    if not contenu:
        return None
    lignes = contenu.splitlines()
    if lignes and lignes[0].startswith("## "):
        lignes = lignes[1:]
        while lignes and lignes[0].strip() in ("", "---"):
            lignes = lignes[1:]
    return "\n".join(lignes).strip()
