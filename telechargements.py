"""
Téléchargement des versions desktop (Windows / macOS).
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent
DOWNLOADS_DIR = APP_DIR / "downloads"

VERSION = "1.0.0"

FICHIER_MAC = DOWNLOADS_DIR / f"MonCerveauDePoche-{VERSION}.dmg"
FICHIER_WIN_ZIP = DOWNLOADS_DIR / f"MonCerveauDePoche-{VERSION}-windows.zip"
FICHIER_WIN_EXE = DOWNLOADS_DIR / "MonCerveauDePoche.exe"


def _lire_fichier(chemin: Path) -> bytes | None:
    if not chemin.is_file():
        return None
    return chemin.read_bytes()


def _taille_lisible(octets: int) -> str:
    if octets >= 1024 * 1024:
        return f"{octets / (1024 * 1024):.1f} Mo"
    if octets >= 1024:
        return f"{octets / 1024:.0f} Ko"
    return f"{octets} o"


def onglet_application_mac() -> None:
    """Contenu de l'onglet « Application Mac »."""
    st.markdown(
        "Téléchargez **Mon Cerveau de Poche** pour macOS. "
        "L'application tourne **en local** sur votre Mac — aucune connexion Internet "
        "n'est requise après l'installation."
    )
    st.markdown(
        "1. Ouvrez le fichier `.dmg`  \n"
        "2. Glissez l'application dans **Applications**  \n"
        "3. Première fois : clic droit → **Ouvrir** (macOS bloque les apps non signées)"
    )

    data = _lire_fichier(FICHIER_MAC)
    if data:
        st.download_button(
            label=f"Télécharger pour Mac ({_taille_lisible(len(data))})",
            data=data,
            file_name=FICHIER_MAC.name,
            mime="application/x-apple-diskimage",
            type="primary",
            use_container_width=True,
            key="dl_mac",
        )
    else:
        st.info(
            f"Le fichier `{FICHIER_MAC.name}` n'est pas encore disponible sur ce serveur. "
            "Contactez votre enseignant ou consultez le site du livre."
        )


def onglet_application_windows() -> None:
    """Contenu de l'onglet « Application Windows »."""
    st.markdown(
        "Téléchargez **Mon Cerveau de Poche** pour Windows. "
        "L'application tourne **en local** — vos données restent sur votre machine."
    )
    st.markdown(
        "1. Décompressez le fichier `.zip`  \n"
        "2. Lancez `MonCerveauDePoche.exe`  \n"
        "3. Si Windows affiche un avertissement : **Informations complémentaires** → **Exécuter quand même**"
    )

    data_zip = _lire_fichier(FICHIER_WIN_ZIP)
    data_exe = _lire_fichier(FICHIER_WIN_EXE)

    if data_zip:
        st.download_button(
            label=f"Télécharger pour Windows — ZIP ({_taille_lisible(len(data_zip))})",
            data=data_zip,
            file_name=FICHIER_WIN_ZIP.name,
            mime="application/zip",
            type="primary",
            use_container_width=True,
            key="dl_win_zip",
        )
    elif data_exe:
        st.download_button(
            label=f"Télécharger pour Windows — EXE ({_taille_lisible(len(data_exe))})",
            data=data_exe,
            file_name=FICHIER_WIN_EXE.name,
            mime="application/vnd.microsoft.portable-executable",
            type="primary",
            use_container_width=True,
            key="dl_win_exe",
        )
    else:
        st.info(
            f"Le fichier `{FICHIER_WIN_ZIP.name}` n'est pas encore disponible sur ce serveur. "
            "Contactez votre enseignant ou consultez le site du livre."
        )
