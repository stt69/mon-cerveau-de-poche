#!/usr/bin/env python3
"""
Gestion de la liste d'emails autorisés (ligne de commande).

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

import auth_gestion as ag


def cmd_init(_: argparse.Namespace) -> None:
    if ag.CONFIG.exists():
        print(f"Déjà présent : {ag.CONFIG}")
        return
    if not ag.EXAMPLE.exists():
        print(f"Exemple introuvable : {ag.EXAMPLE}")
        sys.exit(1)
    texte = ag.EXAMPLE.read_text(encoding="utf-8")
    texte = texte.replace("CHANGEZ_CETTE_CLE_SECRETE", secrets.token_hex(32))
    ag.CONFIG.write_text(texte, encoding="utf-8")
    print(f"Créé : {ag.CONFIG}")
    print("Autorisez des emails avec : python gerer_utilisateurs.py autoriser ...")


def cmd_autoriser(args: argparse.Namespace) -> None:
    print(ag.autoriser(args.email))


def cmd_autoriser_fichier(args: argparse.Namespace) -> None:
    chemin = Path(args.fichier)
    if not chemin.exists():
        print(f"Fichier introuvable : {chemin}")
        sys.exit(1)
    messages = ag.autoriser_plusieurs(chemin.read_text(encoding="utf-8"))
    if not messages:
        print("Aucun email trouvé dans le fichier.")
        return
    for m in messages:
        print(m)


def cmd_liste(_: argparse.Namespace) -> None:
    try:
        pre = ag.emails_attente()
        actifs = ag.comptes_actifs()
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    print("=== En attente (première connexion) ===")
    if pre:
        for email in pre:
            print(f"- {email}")
    else:
        print("(aucun)")

    print()
    print("=== Comptes activés ===")
    if actifs:
        for email, label in actifs:
            suffix = f"  ({label})" if label else ""
            print(f"- {email}{suffix}")
    else:
        print("(aucun)")


def cmd_retirer(args: argparse.Namespace) -> None:
    msg = ag.retirer(args.email)
    print(msg)
    if msg.startswith("Introuvable"):
        sys.exit(1)


def cmd_reinitialiser(args: argparse.Namespace) -> None:
    msg = ag.reinitialiser(args.email)
    print(msg)
    if msg.startswith("Introuvable"):
        sys.exit(1)


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
