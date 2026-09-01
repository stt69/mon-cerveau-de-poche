"""Charge les explications (chapitres du livre) pour les exemples Excel."""

from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
INDEX_PATH = BASE / "explications_index.json"

_index: dict | None = None


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
    return meta.get("titre") or "Explication du cas"


def charger_contenu(nom_xlsx: str) -> str | None:
    meta = _charger_index().get(nom_xlsx)
    if not meta:
        return None
    chemin = BASE / meta["fichier"]
    if not chemin.is_file():
        return None
    return chemin.read_text(encoding="utf-8")
