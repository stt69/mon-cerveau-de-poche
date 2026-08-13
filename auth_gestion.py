"""Gestion partagée des emails autorisés (CLI + interface admin Streamlit)."""

from __future__ import annotations

from pathlib import Path

import yaml

CONFIG = Path(__file__).resolve().parent / "auth_config.yaml"
EXAMPLE = Path(__file__).resolve().parent / "auth_config.yaml.example"

ADMIN_EMAILS = {"thomas@immotour.swiss"}


def _normaliser_preauthorized(data: dict) -> None:
    pre = data.get("pre-authorized")
    if pre is None:
        data["pre-authorized"] = {"emails": []}
    elif isinstance(pre, list):
        data["pre-authorized"] = {
            "emails": [e.strip().lower() for e in pre if e]
        }
    elif isinstance(pre, dict):
        emails = pre.get("emails") or []
        data["pre-authorized"] = {
            "emails": [e.strip().lower() for e in emails if e]
        }
    else:
        data["pre-authorized"] = {"emails": []}


def charger() -> dict:
    if not CONFIG.exists():
        raise FileNotFoundError(f"Fichier manquant : {CONFIG}")
    with CONFIG.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("credentials", {}).setdefault("usernames", {})
    _normaliser_preauthorized(data)
    return data


def sauver(config: dict) -> None:
    _normaliser_preauthorized(config)
    with CONFIG.open("w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def emails_attente(config: dict | None = None) -> list[str]:
    cfg = config or charger()
    _normaliser_preauthorized(cfg)
    return sorted(cfg["pre-authorized"]["emails"])


def comptes_actifs(config: dict | None = None) -> list[tuple[str, str]]:
    """Retourne [(email, nom_affiche), ...]."""
    cfg = config or charger()
    users = cfg.get("credentials", {}).get("usernames") or {}
    out = []
    for email, data in sorted(users.items()):
        prenom = (data or {}).get("first_name", "") or ""
        nom = (data or {}).get("last_name", "") or ""
        label = f"{prenom} {nom}".strip()
        out.append((email, label))
    return out


def autoriser(email: str) -> str:
    email = email.strip().lower()
    if "@" not in email:
        return f"Email invalide : {email}"
    config = charger()
    users = config["credentials"]["usernames"]
    pre = emails_attente(config)

    if email in users:
        return f"Déjà inscrit (mot de passe créé) : {email}"
    if email in pre:
        return f"Déjà en attente de première connexion : {email}"

    config["pre-authorized"]["emails"] = pre + [email]
    sauver(config)
    return f"Autorisé (première connexion) : {email}"


def autoriser_plusieurs(texte: str) -> list[str]:
    messages = []
    for ligne in texte.splitlines():
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#") or "@" not in ligne:
            continue
        messages.append(autoriser(ligne))
    return messages


def retirer(email: str) -> str:
    email = email.strip().lower()
    config = charger()
    pre = emails_attente(config)
    users = config["credentials"]["usernames"]
    parts = []

    if email in pre:
        config["pre-authorized"]["emails"] = [e for e in pre if e != email]
        parts.append("retiré de la liste d'attente")
    if email in users:
        del users[email]
        parts.append("compte désactivé")

    if not parts:
        return f"Introuvable : {email}"

    sauver(config)
    return f"{email} : " + ", ".join(parts)


def reinitialiser(email: str) -> str:
    email = email.strip().lower()
    config = charger()
    users = config["credentials"]["usernames"]
    pre = emails_attente(config)

    if email not in users and email not in pre:
        return f"Introuvable : {email}"

    if email in users:
        del users[email]
    if email not in pre:
        config["pre-authorized"]["emails"] = pre + [email]
    sauver(config)
    return f"Remis en première connexion : {email}"


def est_admin(username: str | None = None, email: str | None = None) -> bool:
    candidats = {
        (username or "").strip().lower(),
        (email or "").strip().lower(),
    }
    return bool(candidats & ADMIN_EMAILS)
