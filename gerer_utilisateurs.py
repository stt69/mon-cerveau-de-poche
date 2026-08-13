#!/usr/bin/env python3
"""
Gestion de la liste d'emails autorisés.

Les étudiants créent leur mot de passe eux-mêmes à la première connexion.
Tu n'as qu'à autoriser (ou retirer) des emails.

Usage :
  python gerer_utilisateurs.py init
  python gerer_utilisateurs.py autoriser email@ecole.ch
  python gerer_utilisateurs.py autoriser-fichier emails.txt
  python gerer_utilisateurs.py liste
  python gerer_utilisateurs.py retirer email@ecole.ch
  python gerer_utilisateurs.py reinitialiser email@ecole.ch
"""

from __future__ import annotations

import argparse
import secrets
import sys
from pathlib import Path

import yaml

CONFIG = Path(__file__).resolve().parent / "auth_config.yaml"
EXAMPLE = Path(__file__).resolve().parent / "auth_config.yaml.example"


def _normaliser_preauthorized(data: dict) -> None:
    """Uniformise pre-authorized en {"emails": [...]} (compat streamlit-authenticator)."""
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
        print(f"Fichier manquant : {CONFIG}")
        print("Lancez d'abord : python gerer_utilisateurs.py init")
        sys.exit(1)
    with CONFIG.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("credentials", {}).setdefault("usernames", {})
    _normaliser_preauthorized(data)
    return data


def sauver(config: dict) -> None:
    _normaliser_preauthorized(config)
    with CONFIG.open("w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def emails_autorises(config: dict) -> list:
    _normaliser_preauthorized(config)
    return list(config["pre-authorized"]["emails"])


def cmd_init(_: argparse.Namespace) -> None:
    if CONFIG.exists():
        print(f"Déjà présent : {CONFIG}")
        return
    if not EXAMPLE.exists():
        print(f"Exemple introuvable : {EXAMPLE}")
        sys.exit(1)
    texte = EXAMPLE.read_text(encoding="utf-8")
    texte = texte.replace("CHANGEZ_CETTE_CLE_SECRETE", secrets.token_hex(32))
    CONFIG.write_text(texte, encoding="utf-8")
    print(f"Créé : {CONFIG}")
    print("Autorisez des emails avec : python gerer_utilisateurs.py autoriser ...")


def cmd_autoriser(args: argparse.Namespace) -> None:
    email = args.email.strip().lower()
    config = charger()
    users = config["credentials"]["usernames"]
    pre = emails_autorises(config)

    if email in users:
        print(f"Déjà inscrit (mot de passe créé) : {email}")
        return
    if email in pre:
        print(f"Déjà en attente de première connexion : {email}")
        return

    config["pre-authorized"]["emails"] = pre + [email]
    sauver(config)
    print(f"Autorisé (première connexion) : {email}")


def cmd_autoriser_fichier(args: argparse.Namespace) -> None:
    chemin = Path(args.fichier)
    if not chemin.exists():
        print(f"Fichier introuvable : {chemin}")
        sys.exit(1)
    lignes = [
        l.strip().lower()
        for l in chemin.read_text(encoding="utf-8").splitlines()
        if l.strip() and not l.strip().startswith("#") and "@" in l
    ]
    for email in lignes:
        ns = argparse.Namespace(email=email)
        cmd_autoriser(ns)


def cmd_liste(_: argparse.Namespace) -> None:
    config = charger()
    pre = emails_autorises(config)
    users = config["credentials"]["usernames"] or {}

    print("=== En attente (première connexion) ===")
    if pre:
        for email in sorted(pre):
            print(f"- {email}")
    else:
        print("(aucun)")

    print()
    print("=== Comptes activés ===")
    if users:
        for email, data in sorted(users.items()):
            prenom = data.get("first_name", "")
            nom = data.get("last_name", "")
            print(f"- {email}  ({prenom} {nom})".rstrip())
    else:
        print("(aucun)")


def cmd_retirer(args: argparse.Namespace) -> None:
    """Retire l'email de la liste d'attente et/ou des comptes actifs."""
    email = args.email.strip().lower()
    config = charger()
    pre = emails_autorises(config)
    users = config["credentials"]["usernames"]
    change = False

    if email in pre:
        config["pre-authorized"]["emails"] = [e for e in pre if e != email]
        change = True
        print(f"Retiré de la liste d'attente : {email}")

    if email in users:
        del users[email]
        change = True
        print(f"Compte désactivé : {email}")

    if not change:
        print(f"Introuvable : {email}")
        sys.exit(1)

    sauver(config)


def cmd_reinitialiser(args: argparse.Namespace) -> None:
    """Supprime le mot de passe : l'étudiant devra refaire la première connexion."""
    email = args.email.strip().lower()
    config = charger()
    users = config["credentials"]["usernames"]
    pre = emails_autorises(config)

    if email not in users and email not in pre:
        print(f"Introuvable : {email}")
        sys.exit(1)

    if email in users:
        del users[email]
        print(f"Mot de passe effacé : {email}")

    if email not in pre:
        config["pre-authorized"]["emails"] = pre + [email]

    sauver(config)
    print(f"Remis en première connexion : {email}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gérer les emails autorisés — Mon Cerveau de Poche"
    )
    sub = parser.add_subparsers(dest="commande", required=True)

    p_init = sub.add_parser("init", help="Créer auth_config.yaml")
    p_init.set_defaults(func=cmd_init)

    p_add = sub.add_parser("autoriser", help="Autoriser un email (sans mot de passe)")
    p_add.add_argument("email")
    p_add.set_defaults(func=cmd_autoriser)

    p_file = sub.add_parser("autoriser-fichier", help="Autoriser une liste d'emails (1 par ligne)")
    p_file.add_argument("fichier")
    p_file.set_defaults(func=cmd_autoriser_fichier)

    p_list = sub.add_parser("liste", help="Lister emails en attente et comptes activés")
    p_list.set_defaults(func=cmd_liste)

    p_del = sub.add_parser("retirer", help="Retirer un email / désactiver un compte")
    p_del.add_argument("email")
    p_del.set_defaults(func=cmd_retirer)

    p_reset = sub.add_parser(
        "reinitialiser",
        help="Effacer le mot de passe et forcer une nouvelle première connexion",
    )
    p_reset.add_argument("email")
    p_reset.set_defaults(func=cmd_reinitialiser)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
