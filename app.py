"""
Mon Cerveau de Poche — Application Streamlit

Interface graphique pour entraîner, visualiser et utiliser
un réseau de neurones sur n'importe quel fichier Excel.

Lancer avec :  streamlit run app.py
"""

from __future__ import annotations

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import io
from pathlib import Path

from cerveau_poche import (
    CerveauPoche, Normaliseur, RegressionLineaire,
    decouper_donnees, indices_decoupe, calculer_r2, calculer_mae,
    recommander_reseau, formater_formules_regression,
    recommandation_favorise_regression,
)
import auth_gestion as ag
import explications as exp
import aide_graphiques as ag_aide
import code_source as cs
import telechargements as tel

# ── Configuration ───────────────────────────────────────────
st.set_page_config(
    page_title="Mon Cerveau de Poche",
    page_icon="🧠",
    layout="wide",
)

PREREGLAGES = {
    'Petit (< 200 lignes)':  dict(couches=1, neurones=8,  lr=0.01,  epoques=200, lot=16),
    'Moyen (200 – 2 000)':   dict(couches=2, neurones=16, lr=0.001, epoques=300, lot=32),
    'Grand (2 000+)':        dict(couches=2, neurones=32, lr=0.001, epoques=500, lot=64),
}

COULEURS = ['#2F5496', '#C00000', '#548235', '#BF8F00', '#7030A0',
            '#00B0F0', '#FF6600', '#005B5B']

DISCLAIMER_TEXTE = """
### Avertissement important — limitation de responsabilité

L'application **Mon Cerveau de Poche** est un outil d'aide à la décision
pédagogique et opérationnel. Les prédictions produites (régression /
classification) sont indicatives et peuvent contenir des erreurs.

En utilisant ce logiciel, vous reconnaissez notamment que :

1. vous restez seul responsable de l'installation, de la configuration et de
   l'utilisation du programme ;
2. vous restez seul responsable de toute décision métier, financière,
   contractuelle, juridique, technique ou opérationnelle prise sur la base des
   résultats fournis ;
3. vous devez vérifier la cohérence des données, valider les résultats et
   exercer votre jugement professionnel avant toute décision ;
4. dans les limites autorisées par la loi applicable, **immotour** et les
   auteurs n'assument aucune responsabilité pour d'éventuels dommages directs,
   indirects ou consécutifs liés à l'installation, à l'utilisation du
   programme, ou à des décisions prises sur la base des prédictions.
"""


# ── Fonctions utilitaires ──────────────────────────────────

def preparer_donnees(df, colonnes_cible):
    """Nettoie le DataFrame, sépare entrées et cibles."""
    df = df.dropna().copy()
    non_num = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if non_num:
        st.warning(f"Colonnes non numériques ignorées : {', '.join(non_num)}")
        df = df.drop(columns=non_num)

    y = df[colonnes_cible].values.astype(np.float64)
    X = df.drop(columns=colonnes_cible).values.astype(np.float64)
    colonnes_entree = [c for c in df.columns if c not in colonnes_cible]
    return X, y, colonnes_entree


def tracer_mae(historique, colonnes_cible, norm_y, y_val_reel, ax):
    """Trace la courbe MAE sur l'axe donné."""
    epoques = range(1, len(historique['mae_val']) + 1)
    ax.plot(epoques, historique['mae_val'], color=COULEURS[0], linewidth=1.5, label='MAE test')
    ax.plot(epoques, historique['mae_train'], color=COULEURS[1], linewidth=1,
            alpha=0.5, linestyle='--', label='MAE entraînement')
    ax.set_title("Courbe d'erreur (MAE)", fontsize=11, fontweight='bold')
    ax.set_xlabel("Époque")
    ax.set_ylabel("MAE (normalisé)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)


def tracer_pred_vs_reel(y_vrai, y_pred, colonnes_cible, ax):
    """Graphique Prédit vs Réel."""
    n_cibles = y_vrai.shape[1] if y_vrai.ndim > 1 else 1
    for i in range(n_cibles):
        yv = y_vrai[:, i] if n_cibles > 1 else y_vrai
        yp = y_pred[:, i] if n_cibles > 1 else y_pred
        label = colonnes_cible[i] if n_cibles > 1 else colonnes_cible[0]
        ax.scatter(yv, yp, s=14, alpha=0.6, label=label, color=COULEURS[i % len(COULEURS)])
        lo, hi = yv.min(), yv.max()
        ax.plot([lo, hi], [lo, hi], linewidth=0.8, alpha=0.5, color='gray')
    ax.set_title("Prédit vs Réel", fontsize=11, fontweight='bold')
    ax.set_xlabel("Valeur réelle")
    ax.set_ylabel("Valeur prédite")
    if n_cibles > 1:
        ax.legend(fontsize=7, ncols=2)
    ax.grid(True, alpha=0.3)


def tracer_residus(y_vrai, y_pred, colonnes_cible, ax):
    """Graphique des résidus."""
    n_cibles = y_vrai.shape[1] if y_vrai.ndim > 1 else 1
    for i in range(n_cibles):
        yv = y_vrai[:, i] if n_cibles > 1 else y_vrai
        yp = y_pred[:, i] if n_cibles > 1 else y_pred
        res = yv - yp
        label = colonnes_cible[i] if n_cibles > 1 else colonnes_cible[0]
        ax.scatter(yv, res, s=14, alpha=0.6, label=label, color=COULEURS[i % len(COULEURS)])
    ax.axhline(0, linestyle='--', linewidth=0.9, color='gray')
    ax.set_title("Résidus", fontsize=11, fontweight='bold')
    ax.set_xlabel("Valeur réelle")
    ax.set_ylabel("Résidu (réel − prédit)")
    if n_cibles > 1:
        ax.legend(fontsize=7, ncols=2)
    ax.grid(True, alpha=0.3)


def tracer_confusion(y_vrai, y_pred, classes, ax):
    """Matrice de confusion pour la classification."""
    n = len(classes)
    matrice = np.zeros((n, n), dtype=int)
    for v, p in zip(y_vrai, y_pred):
        vi = np.searchsorted(classes, v)
        pi = np.searchsorted(classes, p)
        if 0 <= vi < n and 0 <= pi < n:
            matrice[vi, pi] += 1

    ax.imshow(matrice, cmap='Blues', aspect='auto')
    for i in range(n):
        for j in range(n):
            ax.text(j, i, str(matrice[i, j]), ha='center', va='center',
                    fontsize=11, color='white' if matrice[i, j] > matrice.max() / 2 else 'black')
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels([str(c) for c in classes])
    ax.set_yticklabels([str(c) for c in classes])
    ax.set_xlabel("Prédit")
    ax.set_ylabel("Réel")
    ax.set_title("Matrice de confusion", fontsize=11, fontweight='bold')


def suggerer_prereglage(n_lignes):
    if n_lignes < 200:
        return 'Petit (< 200 lignes)'
    elif n_lignes < 2000:
        return 'Moyen (200 – 2 000)'
    return 'Grand (2 000+)'


def afficher_metriques_regression(mae_par_cible, r2_par_cible, colonnes_cible, prefixe=""):
    """Affiche MAE et R² par cible (régression ou réseau)."""
    cols_met = st.columns(min(4, len(colonnes_cible)))
    for i, cible in enumerate(colonnes_cible):
        with cols_met[i % len(cols_met)]:
            st.metric(f"{prefixe}MAE — {cible}", f"{mae_par_cible[i]:,.2f}")
            st.caption(f"R² = {float(r2_par_cible[i]):.3f}")
    if len(colonnes_cible) > 1:
        st.metric(f"{prefixe}MAE globale", f"{np.mean(mae_par_cible):,.2f}")
        st.caption(f"R² global = {np.mean(r2_par_cible):.3f}")


def tableau_comparaison(colonnes_cible, mae_reg, mae_nn, r2_reg, r2_nn):
    """Tableau comparatif régression vs réseau."""
    lignes = []
    for i, c in enumerate(colonnes_cible):
        d_mae = (mae_reg[i] - mae_nn[i]) / (mae_reg[i] + 1e-10) * 100
        lignes.append({
            "Cible": c,
            "MAE régression": round(float(mae_reg[i]), 2),
            "MAE réseau": round(float(mae_nn[i]), 2),
            "Δ MAE (%)": round(float(d_mae), 1),
            "R² régression": round(float(r2_reg[i]), 3),
            "R² réseau": round(float(r2_nn[i]), 3),
            "Δ R²": round(float(r2_nn[i] - r2_reg[i]), 3),
        })
    if len(colonnes_cible) > 1:
        d_mae_g = (np.mean(mae_reg) - np.mean(mae_nn)) / (np.mean(mae_reg) + 1e-10) * 100
        lignes.append({
            "Cible": "— Global —",
            "MAE régression": round(float(np.mean(mae_reg)), 2),
            "MAE réseau": round(float(np.mean(mae_nn)), 2),
            "Δ MAE (%)": round(float(d_mae_g), 1),
            "R² régression": round(float(np.mean(r2_reg)), 3),
            "R² réseau": round(float(np.mean(r2_nn)), 3),
            "Δ R²": round(float(np.mean(r2_nn) - np.mean(r2_reg)), 3),
        })
    return pd.DataFrame(lignes)


def afficher_formules_regression(reg, colonnes_entree, colonnes_cible):
    """Affiche équation, Excel et Python (formules complètes)."""
    formules = formater_formules_regression(reg, colonnes_entree, colonnes_cible)
    st.subheader("📋 Formules de prédiction (régression linéaire)")
    st.caption(
        "Modèle ajusté sur les valeurs brutes du fichier (mêmes unités que votre Excel). "
        "Recopiez dans un tableur ou un programme."
    )
    for f in formules:
        if len(formules) > 1:
            st.markdown(f"**Cible : {f['cible']}**")
        st.markdown("**Équation**")
        st.code(f["equation"], language=None)
        st.markdown("**Formule Excel**")
        st.caption(f"Références ligne 2 : {f['legende_excel']}")
        st.code(f["excel"], language=None)
        st.markdown("**Python**")
        st.code(f["python"], language="python")
        if len(formules) > 1:
            st.divider()


def _rerun():
    """Compatibilité rerun Streamlit."""
    if hasattr(st, "rerun"):
        st.rerun()
    elif hasattr(st, "experimental_rerun"):
        st.experimental_rerun()


AUTH_CONFIG_PATH = Path(__file__).resolve().parent / "auth_config.yaml"

CATEGORIES_EXEMPLES = {
    "pratique": "Cas pratiques (commerce)",
    "tourisme": "Tourisme",
    "construction": "Construction",
    "immobilier": "Immobilier",
    "sante": "Santé",
    "production": "Production",
    "enseignement": "Enseignement",
    "droit": "Droit",
    "photo": "Photographie",
    "biologie": "Biologie",
    "forestier": "Forestier",
    "agriculture": "Agriculture",
    "info": "Informatique",
    "transport": "Transport",
    "fromagerie": "Fromagerie",
}


def dossier_exemples() -> Path | None:
    """Dossier des Excel d'exemple (VPS: exemples/, local PocketBrain: ../excel/)."""
    base = Path(__file__).resolve().parent
    for candidat in (base / "exemples", base.parent / "excel"):
        if candidat.is_dir() and any(candidat.glob("*.xlsx")):
            return candidat
    return None


def categoriser_exemple(nom: str) -> str:
    stem = Path(nom).stem
    if stem.startswith("cas_"):
        parties = stem.split("_")
        if len(parties) >= 2:
            return CATEGORIES_EXEMPLES.get(parties[1], parties[1].capitalize())
    if stem.startswith("chapitre"):
        return "Chapitres (Partie I)"
    return "Autres exemples"


def lister_exemples() -> dict[str, list[Path]]:
    """Retourne {catégorie: [chemins .xlsx]} trié (hors chapitres Partie I)."""
    dossier = dossier_exemples()
    if dossier is None:
        return {}
    groupes: dict[str, list[Path]] = {}
    for chemin in sorted(dossier.glob("*.xlsx")):
        stem = chemin.stem.lower()
        # Exclure les exercices Excel de la Partie I (chapitres 03–05)
        if stem.startswith("chapitre"):
            continue
        cat = categoriser_exemple(chemin.name)
        if cat == "Chapitres (Partie I)":
            continue
        groupes.setdefault(cat, []).append(chemin)
    return dict(sorted(groupes.items(), key=lambda x: x[0].lower()))


def verifier_authentification():
    """
    Si auth_config.yaml est présent, impose une connexion.
    - Liste d'emails autorisés gérée côté serveur
    - Mot de passe choisi par l'étudiant à la première connexion
    Sans ce fichier (ex. app locale packagée), l'accès reste ouvert.
    """
    if not AUTH_CONFIG_PATH.exists():
        return None

    import streamlit_authenticator as stauth
    import yaml

    with AUTH_CONFIG_PATH.open(encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}
    # streamlit-authenticator peut stocker pre-authorized comme
    # {"emails": [...]} ou directement comme une liste.
    pre = config.get("pre-authorized") or []
    if isinstance(pre, dict):
        pre = pre.get("emails") or []
    emails_preautorises = [e.strip().lower() for e in pre if e]

    authenticator = stauth.Authenticate(str(AUTH_CONFIG_PATH))

    menu_options = [
        "Se connecter",
        "Première connexion",
        "Code source",
        "Application Windows",
        "Application Mac",
    ]
    section = st.radio(
        "Menu",
        menu_options,
        horizontal=True,
        label_visibility="collapsed",
        key="menu_public",
    )

    menu_precedent = st.session_state.get("_menu_public_precedent")
    ouvrir_code = section == "Code source" and menu_precedent != "Code source"
    st.session_state["_menu_public_precedent"] = section

    if section == "Code source":
        cs.onglet_code_source(ouvrir_popup=ouvrir_code)

    elif section == "Application Windows":
        tel.onglet_application_windows()

    elif section == "Application Mac":
        tel.onglet_application_mac()

    elif section == "Se connecter":
        try:
            authenticator.login(
                location="main",
                fields={
                    "Form name": "Connexion",
                    "Username": "Email",
                    "Password": "Mot de passe",
                    "Login": "Se connecter",
                },
                captcha=False,
                max_login_attempts=5,
                key="Login",
            )
        except Exception as e:
            st.error(f"Erreur de connexion : {e}")

    elif section == "Première connexion":
        st.caption(
            "Réservé aux emails autorisés par l'enseignant. "
            "Choisissez votre mot de passe une seule fois."
        )
        try:
            email_reg, username_reg, name_reg = authenticator.register_user(
                location="main",
                pre_authorized=emails_preautorises,
                merge_username_email=True,
                captcha=False,
                password_hint=False,
                fields={
                    "Form name": "Créer mon accès",
                    "Email": "Email",
                    "Username": "Email",
                    "Password": "Mot de passe",
                    "Repeat password": "Confirmer le mot de passe",
                    "Register": "Créer mon accès",
                },
                key="Register user",
            )
            if email_reg:
                st.success(
                    f"Compte créé pour {email_reg}. "
                    "Passez à l'onglet « Se connecter »."
                )
        except Exception as e:
            st.error(str(e))

    status = st.session_state.get("authentication_status")
    if status is True:
        return authenticator
    if status is False:
        st.error("Email ou mot de passe incorrect.")
        st.stop()

    st.stop()


def afficher_administration():
    """Panneau réservé à l'administrateur pour gérer les emails autorisés."""
    st.subheader("Administration des accès")
    st.caption(
        "Autorisez des emails : les étudiants créeront leur mot de passe "
        "à la première connexion."
    )

    try:
        attente = ag.emails_attente()
        actifs = ag.comptes_actifs()
    except FileNotFoundError as e:
        st.error(str(e))
        return

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**En attente** (première connexion)")
        if attente:
            for email in attente:
                st.write(f"- {email}")
        else:
            st.write("_Aucun_")
    with c2:
        st.markdown("**Comptes activés**")
        if actifs:
            for email, label in actifs:
                suffix = f" ({label})" if label else ""
                st.write(f"- {email}{suffix}")
        else:
            st.write("_Aucun_")

    st.divider()

    st.markdown("**Autoriser un email**")
    col_a, col_b = st.columns([3, 1])
    with col_a:
        nouvel_email = st.text_input(
            "Email",
            placeholder="etudiant@ecole.ch",
            label_visibility="collapsed",
            key="admin_nouvel_email",
        )
    with col_b:
        if st.button("Autoriser", use_container_width=True, key="admin_btn_autoriser"):
            if nouvel_email.strip():
                st.success(ag.autoriser(nouvel_email))
                _rerun()
            else:
                st.warning("Indiquez un email.")

    st.markdown("**Autoriser plusieurs emails** (un par ligne)")
    lot = st.text_area(
        "Liste",
        height=120,
        placeholder="alice@ecole.ch\nbob@ecole.ch",
        label_visibility="collapsed",
        key="admin_lot_emails",
    )
    if st.button("Autoriser la liste", key="admin_btn_lot"):
        messages = ag.autoriser_plusieurs(lot)
        if not messages:
            st.warning("Aucun email valide trouvé.")
        else:
            for m in messages:
                st.write(m)
            _rerun()

    st.divider()

    st.markdown("**Retirer un accès / réinitialiser un mot de passe**")
    tous = sorted(set(attente) | {e for e, _ in actifs})
    if not tous:
        st.info("Aucun email à gérer pour le moment.")
        return

    cible = st.selectbox("Email concerné", tous, key="admin_email_cible")
    b1, b2 = st.columns(2)
    with b1:
        if st.button("Réinitialiser mot de passe", use_container_width=True, key="admin_btn_reset"):
            st.warning(ag.reinitialiser(cible))
            _rerun()
    with b2:
        if st.button("Retirer complètement", use_container_width=True, key="admin_btn_retirer"):
            st.warning(ag.retirer(cible))
            _rerun()


def verifier_disclaimer():
    """Affiche un disclaimer obligatoire avant usage."""
    if "disclaimer_accepte" not in st.session_state:
        st.session_state.disclaimer_accepte = False

    if st.session_state.disclaimer_accepte:
        return

    # Popup native si disponible (Streamlit récent)
    if hasattr(st, "dialog"):
        @st.dialog("⚠️ Conditions d'utilisation")
        def popup_disclaimer():
            st.markdown(DISCLAIMER_TEXTE)
            lu = st.checkbox(
                "J'ai lu, compris et j'accepte ces conditions.",
                key="disclaimer_check_popup",
            )
            col_ok, col_no = st.columns(2)
            with col_ok:
                if st.button("J'accepte", use_container_width=True, key="btn_accept_popup"):
                    if lu:
                        st.session_state.disclaimer_accepte = True
                        st.session_state.disclaimer_accepte_le = datetime.datetime.now().isoformat()
                        _rerun()
                    else:
                        st.warning("Veuillez cocher la case avant de continuer.")
            with col_no:
                st.button("Je refuse", use_container_width=True, key="btn_refuse_popup")

        popup_disclaimer()

    # Garde-fou bloquant (utile aussi en fallback)
    st.warning("L'utilisation de l'application est bloquée tant que les conditions ne sont pas acceptées.")
    st.markdown(DISCLAIMER_TEXTE)
    lu = st.checkbox(
        "J'ai lu, compris et j'accepte ces conditions.",
        key="disclaimer_check_fallback",
    )
    if st.button("Continuer vers l'application", type="primary", key="btn_accept_fallback"):
        if lu:
            st.session_state.disclaimer_accepte = True
            st.session_state.disclaimer_accepte_le = datetime.datetime.now().isoformat()
            _rerun()
        else:
            st.error("Veuillez cocher la case d'acceptation.")
    st.stop()


# ════════════════════════════════════════════════════════════════════
#  INTERFACE
# ════════════════════════════════════════════════════════════════════

authenticator = verifier_authentification()

verifier_disclaimer()

st.title("🧠 Mon Cerveau de Poche")
st.caption("Entraînez un réseau de neurones sur vos données Excel — sans code, sans cloud.")

# ── Barre latérale ─────────────────────────────────────────

with st.sidebar:
    if authenticator is not None:
        nom = st.session_state.get("name") or st.session_state.get("username", "")
        st.caption(f"Connecté : {nom}")
        authenticator.logout("Se déconnecter", location="sidebar", key="logout_btn")
        st.divider()

    admin = authenticator is not None and ag.est_admin(
        st.session_state.get("username"),
        st.session_state.get("email"),
    )
    if admin:
        vue = st.radio(
            "Vue",
            ["Application", "Administration"],
            key="vue_admin",
        )
        st.divider()
    else:
        vue = "Application"

if vue == "Administration":
    afficher_administration()
    st.stop()

with st.sidebar:
    st.header("💾 Modèle sauvegardé")
    fichier_modele = st.file_uploader(
        "Charger un modèle (.zip)", type=["zip"], key="charger_modele")
    if fichier_modele is not None:
        if st.button("Charger ce modèle", key="btn_charger"):
            try:
                data = fichier_modele.read()
                reseau, nX, nY, col_e, col_c, meta = CerveauPoche.depuis_bytes(data)
                st.session_state.reseau = reseau
                st.session_state.norm_X = nX
                st.session_state.norm_y = nY
                st.session_state.colonnes_entree = col_e
                st.session_state.colonnes_cible = col_c
                st.session_state.mode = meta.get('mode', 'regression')
                st.session_state.classes = meta.get('classes', None)
                st.session_state.pop('regression', None)
                st.success(f"Modèle chargé ! Cibles : {', '.join(col_c)}")
            except Exception as e:
                st.error(f"Erreur : {e}")

    st.divider()

    # ── Réglages ──
    st.header("⚙️ Réglages du réseau")
    ag_aide.injecter_style_puces_sidebar()

    def _reglage(label, cle, titre, contenu, widget_fn):
        col_titre, col_i = st.columns([6, 1])
        with col_titre:
            st.markdown(f"**{label}**")
        with col_i:
            ag_aide.afficher_puce_aide_reglage(cle, titre, contenu)
        return widget_fn()

    prereglage = _reglage(
        "Préréglage", "prereglage", "Préréglage", ag_aide.AIDE_PREREGLAGE,
        lambda: st.selectbox(
            "Préréglage", list(PREREGLAGES.keys()), index=1,
            key="prereglage", label_visibility="collapsed",
        ),
    )
    p = PREREGLAGES[prereglage]

    couches = _reglage(
        "Couches cachées", "couches", "Couches cachées", ag_aide.AIDE_COUCHES,
        lambda: st.number_input(
            "Couches cachées", 1, 10, p['couches'],
            key="couches", label_visibility="collapsed",
        ),
    )
    neurones = _reglage(
        "Neurones par couche", "neurones", "Neurones par couche", ag_aide.AIDE_NEURONES,
        lambda: st.number_input(
            "Neurones par couche", 2, 128, p['neurones'],
            key="neurones", label_visibility="collapsed",
        ),
    )
    activation = _reglage(
        "Activation", "activation", "Activation", ag_aide.AIDE_ACTIVATION,
        lambda: st.selectbox(
            "Activation", ['relu', 'sigmoid', 'tanh'],
            key="activation", label_visibility="collapsed",
        ),
    )
    optimiseur = _reglage(
        "Optimiseur", "optimiseur", "Optimiseur", ag_aide.AIDE_OPTIMISEUR,
        lambda: st.selectbox(
            "Optimiseur", ['adam', 'sgd'],
            key="optimiseur", label_visibility="collapsed",
        ),
    )
    lr = _reglage(
        "Taux d'apprentissage", "lr", "Taux d'apprentissage", ag_aide.AIDE_TAUX_APPRENTISSAGE,
        lambda: st.select_slider(
            "Taux d'apprentissage",
            options=[0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001],
            value=p['lr'], key="lr", label_visibility="collapsed",
        ),
    )
    epoques = _reglage(
        "Époques", "epoques", "Époques", ag_aide.AIDE_EPOQUES,
        lambda: st.number_input(
            "Époques", 10, 2000, p['epoques'], step=50,
            key="epoques", label_visibility="collapsed",
        ),
    )
    taille_lot = _reglage(
        "Taille de lot", "lot", "Taille de lot", ag_aide.AIDE_TAILLE_LOT,
        lambda: st.number_input(
            "Taille de lot", 8, 256, p['lot'], step=8,
            key="lot", label_visibility="collapsed",
        ),
    )
    test_pct = _reglage(
        "% données de test", "test_pct", "% données de test", ag_aide.AIDE_DONNEES_TEST,
        lambda: st.slider(
            "% données de test", 0.05, 0.50, 0.20, 0.05,
            key="test_pct", label_visibility="collapsed",
        ),
    )
    graine = _reglage(
        "Graine aléatoire", "graine", "Graine aléatoire", ag_aide.AIDE_GRAINE,
        lambda: st.number_input(
            "Graine aléatoire", value=42,
            key="graine", label_visibility="collapsed",
        ),
    )

    st.divider()

    # ── Prédiction rapide ──
    st.header("🔮 Prédiction rapide")
    if "reseau" in st.session_state and "colonnes_entree" in st.session_state:
        valeurs_pred = []
        for col in st.session_state.colonnes_entree:
            v = st.number_input(f"{col}", value=0.0, key=f"pred_{col}", format="%.4f")
            valeurs_pred.append(v)

        if st.button("Calculer", key="btn_pred_rapide"):
            try:
                reseau = st.session_state.reseau
                nX = st.session_state.norm_X
                nY = st.session_state.norm_y
                mode = st.session_state.get('mode', 'regression')

                row = np.array([valeurs_pred], dtype=np.float64)
                row_n = nX.transformer(row)
                pred_n = reseau.predire(row_n)

                if mode == 'classification':
                    classes = st.session_state.get('classes', [0, 1, 2])
                    classe = classes[np.argmax(pred_n[0])]
                    st.session_state.resultat_rapide = f"Classe prédite : **{classe}**"
                else:
                    pred_nn = nY.inverser(pred_n)[0]
                    cols = st.session_state.colonnes_cible
                    parties = [f"Réseau **{c}** = {v:,.2f}" for c, v in zip(cols, pred_nn)]
                    if "regression" in st.session_state:
                        pred_reg = st.session_state.regression.predire(row)[0]
                        parties += [f"Régression **{c}** = {v:,.2f}"
                                    for c, v in zip(cols, pred_reg)]
                    st.session_state.resultat_rapide = " · ".join(parties)
            except Exception as e:
                st.error(f"Erreur : {e}")

        if "resultat_rapide" in st.session_state:
            st.success(st.session_state.resultat_rapide)
    else:
        st.caption("Entraînez ou chargez un modèle pour prédire.")


# ── Zone principale ────────────────────────────────────────

st.subheader("📂 Données")
source_donnees = st.radio(
    "Comment charger les données ?",
    ["Mon fichier Excel", "Exemples"],
    horizontal=True,
    key="source_donnees",
)

df = None
id_source = None

if source_donnees == "Exemples":
    groupes = lister_exemples()
    if not groupes:
        st.warning(
            "Aucun fichier d'exemple trouvé sur le serveur. "
            "Placez les `.xlsx` dans le dossier `exemples/` à côté de `app.py`, "
            "ou utilisez « Mon fichier Excel »."
        )
    else:
        categories = list(groupes.keys())
        categorie = st.selectbox("Thème", categories, key="exemple_categorie")
        fichiers = groupes[categorie]
        labels = {p: p.stem.replace("_", " ") for p in fichiers}
        choix = st.selectbox(
            "Fichier exemple",
            fichiers,
            format_func=lambda p: labels[p],
            key="exemple_fichier",
        )
        if choix is not None:
            id_source = str(choix.resolve())
            if st.session_state.get("donnees_id") != id_source:
                st.session_state.df = pd.read_excel(choix)
                st.session_state.donnees_id = id_source
                st.session_state.pop("selection_cibles", None)
            df = st.session_state.df
            st.caption(f"Fichier : `{choix.name}`")

            if exp.a_explication(choix.name) and hasattr(st, "dialog"):
                if st.button("📖 Expliquer ce cas", key=f"expliquer_{choix.name}"):
                    contenu = exp.charger_contenu(choix.name)
                    titre = exp.titre_pour(choix.name)

                    @st.dialog(titre)
                    def popup_explication():
                        st.markdown(contenu)

                    popup_explication()
else:
    fichier_excel = st.file_uploader(
        "Charger votre fichier Excel (.xlsx)", type=["xlsx"], key="fichier_excel")
    if fichier_excel:
        id_source = f"upload:{fichier_excel.name}:{fichier_excel.size}"
        if st.session_state.get("donnees_id") != id_source:
            st.session_state.df = pd.read_excel(fichier_excel)
            st.session_state.donnees_id = id_source
            st.session_state.pop("selection_cibles", None)
        df = st.session_state.df
        st.caption(f"Fichier : `{fichier_excel.name}`")

if df is not None:
    st.subheader("Aperçu des données")
    st.dataframe(df.head(10), use_container_width=True)
    st.caption(f"{len(df)} lignes × {len(df.columns)} colonnes")

    # Suggestion automatique de préréglage
    suggestion = suggerer_prereglage(len(df))
    if suggestion != st.session_state.get('prereglage'):
        st.info(f"💡 Pour {len(df)} lignes, le préréglage **{suggestion}** est recommandé.")

    # Sélection des colonnes cibles
    colonnes_cible = st.multiselect(
        "🎯 Colonnes à prédire (cibles)",
        options=list(df.columns),
        key=f"selection_cibles_{st.session_state.get('donnees_id', 'none')}",
    )
    if not colonnes_cible:
        st.info("Sélectionnez au moins une colonne cible pour continuer.")
        st.stop()

    # Mode
    mode = st.radio(
        "Mode", ["Régression", "Classification"],
        horizontal=True, key="mode_radio",
        help="Régression = prédire un nombre. Classification = prédire une catégorie (0, 1, 2...).")
    mode_str = 'regression' if mode == "Régression" else 'classification'
    if mode_str == 'classification':
        st.caption(
            "En mode Classification, seul le réseau de neurones est entraîné "
            "(comparaison avec régression linéaire : mode Régression uniquement)."
        )

    animer = st.checkbox("Animer l'entraînement (mise à jour à chaque époque)", value=True)

    # ── ENTRAÎNER ──
    if st.button("🚀 Entraîner le réseau", type="primary", key="btn_entrainer"):
        X, y, colonnes_entree = preparer_donnees(df, colonnes_cible)
        n_lignes = X.shape[0]
        idx_train, idx_test = indices_decoupe(n_lignes, test_pct=test_pct, graine=graine)

        # ── Régression linéaire (baseline, régression uniquement) ──
        reg = None
        mae_reg = r2_reg = y_test_reel = None
        if mode_str == 'regression':
            if X.shape[1] >= n_lignes:
                st.warning(
                    f"Plus de colonnes d'entrée ({X.shape[1]}) que de lignes ({n_lignes}) : "
                    "la régression linéaire peut être instable."
                )
            reg = RegressionLineaire().ajuster(X[idx_train], y[idx_train])
            y_pred_reg = reg.predire(X[idx_test])
            y_test_reel = y[idx_test]
            mae_reg = np.atleast_1d(calculer_mae(y_test_reel, y_pred_reg))
            r2_reg = np.atleast_1d(calculer_r2(y_test_reel, y_pred_reg))

            st.subheader("📐 Régression linéaire multiple (référence)")
            st.caption(
                "Modèle classique ajusté sur le même jeu d'entraînement, "
                "évalué sur le même jeu de test."
            )
            afficher_metriques_regression(mae_reg, r2_reg, colonnes_cible)
            if reg.rank < X.shape[1] + 1:
                st.caption(
                    f"Rang effectif du modèle : {reg.rank} "
                    "(certaines entrées sont redondantes ou trop corrélées)."
                )

        # Normalisation
        norm_X = Normaliseur().ajuster(X)
        X_n = norm_X.transformer(X)

        classes = None
        if mode_str == 'classification':
            st.session_state.pop('regression', None)
            if y.shape[1] != 1:
                st.error("La classification ne supporte qu'une seule colonne cible.")
                st.stop()
            classes = sorted(np.unique(y[:, 0]).astype(int).tolist())
            n_classes = len(classes)
            # One-hot encode
            y_oh = np.zeros((y.shape[0], n_classes), dtype=np.float64)
            for i, c in enumerate(classes):
                y_oh[y[:, 0] == c, i] = 1.0
            y_n = y_oh
            norm_y = None
            n_sorties = n_classes
        else:
            norm_y = Normaliseur().ajuster(y)
            y_n = norm_y.transformer(y)
            n_sorties = y.shape[1]

        # Découper (mêmes indices que la régression)
        X_train = X_n[idx_train]
        X_test = X_n[idx_test]
        y_train = y_n[idx_train]
        y_test = y_n[idx_test]

        if mode_str == 'regression':
            st.divider()
            st.subheader("🧠 Réseau de neurones")

        # Architecture
        arch = [X_n.shape[1]]
        for _ in range(couches):
            arch.append(neurones)
        arch.append(n_sorties)

        reseau = CerveauPoche(
            architecture=arch,
            activation=activation,
            mode=mode_str,
            taux_apprentissage=lr,
            optimiseur=optimiseur,
            graine=graine,
        )

        # Placeholders pour l'animation
        barre = st.progress(0, text="Entraînement...")
        col1, col2, col3 = st.columns(3)
        with col1:
            ph_mae = st.empty()
        with col2:
            ph_pred = st.empty()
        with col3:
            ph_res = st.empty()

        etat = {'historique': None}

        def rappel_epoque(ep, hist):
            etat['historique'] = hist
            barre.progress((ep + 1) / epoques,
                           text=f"Époque {ep + 1}/{epoques}")

            if not animer:
                return

            # ── MAE ──
            fig1, ax1 = plt.subplots(figsize=(4, 3))
            tracer_mae(hist, colonnes_cible, norm_y, None, ax1)
            fig1.tight_layout()
            ph_mae.pyplot(fig1)
            plt.close(fig1)

            # ── Prédit vs Réel / Confusion ──
            pred_val = reseau.predire(X_test)
            if mode_str == 'regression' and norm_y is not None:
                y_test_reel = norm_y.inverser(y_test)
                y_pred_reel = norm_y.inverser(pred_val)
                fig2, ax2 = plt.subplots(figsize=(4, 3))
                tracer_pred_vs_reel(y_test_reel, y_pred_reel, colonnes_cible, ax2)
                fig2.tight_layout()
                ph_pred.pyplot(fig2)
                plt.close(fig2)

                fig3, ax3 = plt.subplots(figsize=(4, 3))
                tracer_residus(y_test_reel, y_pred_reel, colonnes_cible, ax3)
                fig3.tight_layout()
                ph_res.pyplot(fig3)
                plt.close(fig3)
            elif mode_str == 'classification':
                y_cls_vrai = np.array([classes[i] for i in np.argmax(y_test, axis=1)])
                y_cls_pred = np.array([classes[i] for i in np.argmax(pred_val, axis=1)])
                fig2, ax2 = plt.subplots(figsize=(4, 3))
                tracer_confusion(y_cls_vrai, y_cls_pred, classes, ax2)
                fig2.tight_layout()
                ph_pred.pyplot(fig2)
                plt.close(fig2)

                acc = np.mean(y_cls_vrai == y_cls_pred) * 100
                fig3, ax3 = plt.subplots(figsize=(4, 3))
                ax3.text(0.5, 0.5, f"{acc:.1f}%", transform=ax3.transAxes,
                         fontsize=48, ha='center', va='center', fontweight='bold',
                         color=COULEURS[0])
                ax3.set_title("Précision", fontsize=11, fontweight='bold')
                ax3.axis('off')
                fig3.tight_layout()
                ph_res.pyplot(fig3)
                plt.close(fig3)

        # ── Lancer l'entraînement ──
        reseau.entrainer(X_train, y_train, epoques=epoques, taille_lot=taille_lot,
                         X_val=X_test, y_val=y_test, rappel=rappel_epoque)

        barre.progress(1.0, text="Terminé !")

        # Rendu final (si pas d'animation, dessiner une fois)
        if not animer and etat['historique']:
            rappel_epoque(epoques - 1, etat['historique'])

        # Puces d'aide sous chaque graphique
        with col1:
            ag_aide.afficher_puce_aide(
                "mae", "Courbe d'erreur (MAE)", ag_aide.AIDE_COURBE_MAE)
        with col2:
            if mode_str == 'regression':
                ag_aide.afficher_puce_aide(
                    "pred", "Prédit vs Réel", ag_aide.AIDE_PREDIT_REEL)
            else:
                ag_aide.afficher_puce_aide(
                    "confusion", "Matrice de confusion", ag_aide.AIDE_MATRICE_CONFUSION)
        with col3:
            if mode_str == 'regression':
                ag_aide.afficher_puce_aide(
                    "residus", "Résidus", ag_aide.AIDE_RESIDUS)
            else:
                ag_aide.afficher_puce_aide(
                    "precision", "Précision", ag_aide.AIDE_PRECISION)

        # ── Métriques finales ──
        pred_final = reseau.predire(X_test)

        if mode_str == 'regression' and norm_y is not None:
            y_test_reel = norm_y.inverser(y_test)
            y_pred_reel = norm_y.inverser(pred_final)
            mae_par_cible = np.atleast_1d(calculer_mae(y_test_reel, y_pred_reel))
            r2_par_cible = np.atleast_1d(calculer_r2(y_test_reel, y_pred_reel))

            st.subheader("📊 Métriques réseau (jeu de test)")
            afficher_metriques_regression(mae_par_cible, r2_par_cible, colonnes_cible)

            # ── Comparaison ──
            st.subheader("⚖️ Comparaison régression vs réseau")
            st.dataframe(
                tableau_comparaison(
                    colonnes_cible, mae_reg, mae_par_cible, r2_reg, r2_par_cible),
                use_container_width=True, hide_index=True,
            )

            # ── Recommandation ──
            mae_train_nn = mae_val_nn = None
            if etat['historique'] and etat['historique']['mae_train']:
                mae_train_nn = etat['historique']['mae_train'][-1]
                if etat['historique']['mae_val']:
                    mae_val_nn = etat['historique']['mae_val'][-1]
                    if norm_y is not None:
                        echelle = float(np.mean(norm_y.echelle_))
                        mae_train_nn *= echelle
                        mae_val_nn *= echelle

            titre, message, style = recommander_reseau(
                mae_reg, mae_par_cible, r2_reg, r2_par_cible,
                n_lignes, mae_train_nn, mae_val_nn,
            )
            st.subheader("💡 Recommandation")
            if style == 'success':
                st.success(f"**{titre}** — {message}")
            elif style == 'info':
                st.info(f"**{titre}** — {message}")
            else:
                st.warning(f"**{titre}** — {message}")
            st.caption(
                "Outil d'aide à la décision — votre expertise métier reste indispensable."
            )

            if reg is not None and recommandation_favorise_regression(titre):
                afficher_formules_regression(reg, colonnes_entree, colonnes_cible)

        elif mode_str == 'classification':
            y_cls_vrai = np.array([classes[i] for i in np.argmax(y_test, axis=1)])
            y_cls_pred = np.array([classes[i] for i in np.argmax(pred_final, axis=1)])
            acc = np.mean(y_cls_vrai == y_cls_pred) * 100
            st.subheader("📊 Métriques sur les données de test")
            st.metric("Précision", f"{acc:.1f} %")
            st.caption(f"{int(np.sum(y_cls_vrai == y_cls_pred))} / {len(y_cls_vrai)} "
                       "prédictions correctes")

        # Sauvegarder dans la session
        st.session_state.reseau = reseau
        st.session_state.norm_X = norm_X
        st.session_state.norm_y = norm_y
        st.session_state.colonnes_entree = colonnes_entree
        st.session_state.colonnes_cible = colonnes_cible
        st.session_state.mode = mode_str
        st.session_state.classes = classes
        if reg is not None:
            st.session_state.regression = reg
        else:
            st.session_state.pop('regression', None)
        st.session_state.pop("resultat_rapide", None)

        st.success("✅ Entraînement terminé !")

        # ── Bouton de sauvegarde ──
        st.subheader("💾 Sauvegarder le modèle entraîné")
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        bundle = reseau.vers_bytes(
            norm_X=norm_X, norm_y=norm_y,
            colonnes_entree=colonnes_entree,
            colonnes_cible=colonnes_cible,
            mode_cls_classes=classes,
        )
        st.download_button(
            "⬇️ Télécharger le modèle (.zip)",
            data=bundle,
            file_name=f"cerveau_{ts}.zip",
            mime="application/zip",
            key="btn_sauver",
        )

# ── Prédiction en lot ──────────────────────────────────────

st.divider()
st.subheader("📋 Prédiction sur un jeu de données complet")

if "reseau" in st.session_state and "df" in st.session_state:
    if st.button("Générer les prédictions", key="btn_lot"):
        reseau = st.session_state.reseau
        nX = st.session_state.norm_X
        nY = st.session_state.norm_y
        col_e = st.session_state.colonnes_entree
        col_c = st.session_state.colonnes_cible
        mode = st.session_state.get('mode', 'regression')
        classes = st.session_state.get('classes')

        df_out = st.session_state.df.copy()

        # Garder uniquement les colonnes d'entrée numériques
        non_num = df_out.select_dtypes(include=['object', 'category']).columns.tolist()
        X_all = df_out.drop(columns=non_num).dropna()
        X_vals = X_all[col_e].values.astype(np.float64)
        X_n = nX.transformer(X_vals)
        pred_n = reseau.predire(X_n)

        if mode == 'classification' and classes is not None:
            pred_classes = np.array([classes[i] for i in np.argmax(pred_n, axis=1)])
            df_out = df_out.loc[X_all.index].copy()
            df_out[f"PREDICTION_{col_c[0]}"] = pred_classes
        else:
            pred_nn = nY.inverser(pred_n)
            df_out = df_out.loc[X_all.index].copy()
            reg = st.session_state.get('regression')
            pred_reg = reg.predire(X_vals) if reg is not None else None
            for i, c in enumerate(col_c):
                if pred_reg is not None:
                    df_out[f"PRED_REG_{c}"] = pred_reg[:, i].round(2)
                df_out[f"PRED_NN_{c}"] = pred_nn[:, i].round(2)

        st.dataframe(df_out.head(20), use_container_width=True)

        # Téléchargement Excel
        buf = io.BytesIO()
        df_out.to_excel(buf, index=False, engine='openpyxl')
        buf.seek(0)
        st.download_button(
            "⬇️ Télécharger les prédictions (.xlsx)",
            data=buf.getvalue(),
            file_name="predictions.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="btn_download_pred",
        )
else:
    st.info("Entraînez ou chargez un modèle, puis chargez des données pour prédire.")
