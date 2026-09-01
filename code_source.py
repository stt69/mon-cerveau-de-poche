"""
Affichage du code source complet de l'application (popup + copie presse-papiers).
"""

from __future__ import annotations

import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

APP_DIR = Path(__file__).resolve().parent

FICHIERS: list[tuple[str, str, list[str]]] = [
    ("cerveau_poche.py", "Moteur de neurones (NumPy pur)", ["cerveau_poche.py"]),
    ("app.py", "Interface graphique Streamlit", ["app.py"]),
    ("aide_graphiques.py", "Aides contextuelles (graphiques et réglages)", ["aide_graphiques.py"]),
    ("explications.py", "Chargement des explications de cas métier", ["explications.py"]),
    ("auth_gestion.py", "Gestion des emails et comptes autorisés", ["auth_gestion.py"]),
    ("gerer_utilisateurs.py", "Outil CLI pour l'administrateur", ["gerer_utilisateurs.py"]),
    (
        "launcher.py",
        "Lanceur de l'application desktop",
        ["launcher.py", "packaging/launcher.py"],
    ),
]


def _trouver_fichier(candidats: list[str]) -> Path | None:
    for rel in candidats:
        chemin = APP_DIR / rel
        if chemin.is_file():
            return chemin
    return None


def charger_sources() -> list[tuple[str, str, str]]:
    """Retourne [(nom, description, contenu), …] pour les fichiers présents."""
    resultat: list[tuple[str, str, str]] = []
    for nom, description, candidats in FICHIERS:
        chemin = _trouver_fichier(candidats)
        if chemin is None:
            continue
        resultat.append((nom, description, chemin.read_text(encoding="utf-8")))
    return resultat


def _bouton_copier(contenu: str, cle: str) -> None:
    """Lien « Copier » qui place le contenu dans le presse-papiers."""
    js = json.dumps(contenu)
    uid = cle.replace(".", "-").replace("/", "-")
    components.html(
        f"""
        <a href="#" id="copy-{uid}" style="
            font-size:0.85rem;
            text-decoration:none;
            color:#2F5496;
            white-space:nowrap;
        ">Copier</a>
        <script>
        (function() {{
            var el = document.getElementById("copy-{uid}");
            el.addEventListener("click", function(e) {{
                e.preventDefault();
                navigator.clipboard.writeText({js}).then(function() {{
                    el.textContent = "Copié !";
                    el.style.color = "#548235";
                    setTimeout(function() {{
                        el.textContent = "Copier";
                        el.style.color = "#2F5496";
                    }}, 2000);
                }});
            }});
        }})();
        </script>
        """,
        height=28,
    )


def _corps_popup() -> None:
    sources = charger_sources()
    if not sources:
        st.warning("Aucun fichier source trouvé.")
        return

    st.caption(
        "Code Python complet de **Mon Cerveau de Poche**. "
        "Cliquez **Copier** à côté d'un fichier pour le coller ailleurs."
    )

    for nom, description, contenu in sources:
        col_titre, col_copie = st.columns([8, 1])
        with col_titre:
            st.markdown(f"**`{nom}`** — {description}")
        with col_copie:
            _bouton_copier(contenu, nom)
        st.code(contenu, language="python", line_numbers=True)
        st.divider()


def afficher_popup_code_source() -> None:
    """Ouvre une popup avec le code source complet."""
    if not hasattr(st, "dialog"):
        st.warning("Votre version de Streamlit ne supporte pas les fenêtres modales.")
        _corps_popup()
        return

    @st.dialog("Code source — Mon Cerveau de Poche", width="large")
    def _popup() -> None:
        _corps_popup()

    _popup()


def onglet_code_source(ouvrir_popup: bool = False) -> None:
    """Contenu de l'onglet « Code source » du menu de connexion."""
    st.markdown(
        "Le **code source complet** de l'application est disponible en open source. "
        "Parcourez tous les fichiers Python ou copiez-les un par un."
    )
    if ouvrir_popup:
        afficher_popup_code_source()
    if st.button(
        "Afficher le code source",
        type="primary",
        use_container_width=True,
        key="btn_popup_code_source",
    ):
        afficher_popup_code_source()
