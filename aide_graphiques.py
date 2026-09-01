"""Textes d'aide pour les graphiques et les réglages du réseau."""

from __future__ import annotations

import streamlit as st

# ── Graphiques (résultats) ──────────────────────────────────

AIDE_COURBE_MAE = """
### La courbe d'erreur (MAE)

C'est le **premier graphique** à regarder. Il vous dit si l'entraînement s'est bien passé :

- **Descend et se stabilise** → L'entraînement est réussi. Passez aux graphiques suivants.
- **Encore en descente à la fin** → Le réseau n'a pas fini d'apprendre. Relancez avec plus d'époques.
- **Plate dès le début** → Le réseau n'apprend rien. Revoyez vos données ou augmentez la taille du réseau.
- **Remonte après avoir descendu** → Surapprentissage. Réduisez le nombre d'époques ou de neurones.

---

**MAE** (*Mean Absolute Error*) = erreur absolue moyenne.

> En moyenne, de combien le réseau se trompe-t-il ?

La courbe **pleine** correspond au jeu de **test** (données jamais vues à l'entraînement).
La courbe **pointillée** correspond au jeu d'**entraînement**.

Comparez les deux : si la courbe test remonte alors que la courbe entraînement continue de descendre, c'est un signe de **surapprentissage**.
"""

AIDE_PREDIT_REEL = """
### Le graphique Prédit vs Réel

C'est le graphique le plus parlant visuellement. Chaque point est une observation du **jeu de test** :

- **Points serrés sur la diagonale** → Le réseau prédit avec précision.
- **Nuage dispersé** → Mauvaise précision. Les données ne contiennent peut-être pas assez d'information.
- **Points décalés** → Biais systématique (le réseau surestime ou sous-estime). Ajustez les réglages.

La **diagonale grise** représente la perfection : prédit = réel.

Plus les points sont proches de cette ligne, meilleur est le modèle.
"""

AIDE_RESIDUS = """
### Le graphique des résidus

C'est le graphique de **diagnostic**. Regardez la répartition des erreurs (réel − prédit) :

- **Dispersés uniformément autour de zéro** → Le réseau a capturé tout ce qu'il pouvait.
- **En entonnoir** (erreurs croissantes) → Problème de normalisation ou données très hétérogènes.
- **En courbe** → Le réseau rate un motif. Essayez plus de neurones.
- **Points isolés très loin** → Valeurs aberrantes dans vos données. Vérifiez-les.

La ligne horizontale à **zéro** est la référence : au-dessus, le réseau **sous-estime** ; en dessous, il **surestime**.
"""

AIDE_MATRICE_CONFUSION = """
### La matrice de confusion

C'est un tableau qui montre exactement **où** le réseau se trompe en classification.

Exemple avec deux catégories (Risqué / Normal) :

|  | **Prédit : Normal** | **Prédit : Risqué** |
|---|---|---|
| **Réel : Normal** | 42 ✓ | 3 ✗ |
| **Réel : Risqué** | 5 ✗ | 10 ✓ |

- La **diagonale** contient les bonnes réponses.
- Tout ce qui est **hors diagonale** est une erreur.

Le type d'erreur qui compte dépend du contexte :
- Pour détecter des risques : mieux vaut des fausses alertes que des risques manqués.
- Pour trier des produits : mieux vaut rejeter un bon produit que d'expédier un mauvais.
"""

AIDE_PRECISION = """
### La précision (accuracy)

> **Sur 100 exemples, combien le réseau a-t-il classés correctement ?**

Une précision de **85 %** signifie que le réseau donne la bonne catégorie 85 fois sur 100.

| Précision | Verdict |
|---|---|
| > 90 % | Excellent |
| 80 % – 90 % | Bon |
| 70 % – 80 % | Correct |
| < 70 % | À améliorer |

Complétez toujours ce chiffre avec la **matrice de confusion** pour voir *quel type* d'erreur se produit.
"""

# ── Réglages (barre latérale) ───────────────────────────────

AIDE_PREREGLAGE = """
### Préréglage

Point de départ adapté à la **taille de votre fichier** :

| Taille | Couches | Neurones | Époques | Taux |
|---|---|---|---|---|
| Petit (< 200 lignes) | 1 | 8 | 200 | 0.01 |
| Moyen (200 – 2 000) | 2 | 16 | 300 | 0.001 |
| Grand (2 000+) | 2 | 32 | 500 | 0.001 |

L'application propose automatiquement un préréglage selon le nombre de lignes. Vous pouvez ensuite ajuster finement.
"""

AIDE_COUCHES = """
### Couches cachées

Chaque couche ajoute un niveau de sophistication :

- **1 couche** : relations directes (« quand X monte, Y monte »). Suffisant pour la majorité des cas.
- **2 couches** : combinaisons (« quand X monte **et** c'est le week-end, Y monte encore plus »).
- **3+ couches** : motifs subtils, mais risque de surapprentissage sur petits fichiers.

> **Règle d'or** : commencez petit. Si les résultats sont insuffisants, augmentez.
"""

AIDE_NEURONES = """
### Neurones par couche

Le nombre de neurones détermine combien d'« angles » le réseau utilise pour regarder vos données :

- **4 à 8** : vision étroite, rapide — problèmes simples.
- **16 à 32** : bon compromis, réglage le plus courant.
- **64+** : très large, risque de surapprentissage si peu de lignes.

Analogie : pour un petit restaurant, pas besoin de 50 employés sur 5 niveaux hiérarchiques.
"""

AIDE_ACTIVATION = """
### Fonction d'activation

| Fonction | Rôle | Quand l'utiliser |
|---|---|---|
| **ReLU** | Si négatif → 0, sinon garde la valeur | **Par défaut.** Fonctionne presque toujours. |
| **Sigmoid** | Compresse entre 0 et 1 | Rarement nécessaire ici |
| **Tanh** | Compresse entre -1 et 1 | Rarement nécessaire ici |

**Conseil : gardez ReLU.**
"""

AIDE_OPTIMISEUR = """
### Optimiseur

Algorithme qui décide **comment** ajuster les poids :

| Optimiseur | Rôle |
|---|---|
| **Adam** | Adapte automatiquement la vitesse de chaque poids |
| **SGD** | Ajuste tous les poids à la même vitesse |

**Conseil : gardez Adam.** Plus tolérant et plus rapide dans la plupart des cas.
"""

AIDE_TAUX_APPRENTISSAGE = """
### Taux d'apprentissage

Vitesse à laquelle le réseau corrige ses poids. Tout se lit sur la **courbe MAE** :

- **Descend proprement** → taux correct.
- **Zigzague violemment** → taux trop élevé, divisez par 2 ou 5.
- **Plate dès le début** → taux peut-être trop faible, multipliez par 2.
- **Descend puis explose** → taux beaucoup trop élevé, divisez par 5 ou 10.
"""

AIDE_EPOQUES = """
### Époques

Nombre de fois que le réseau parcourt toutes vos données. Le bon nombre, c'est **quand la courbe MAE ne descend plus** :

- Encore en descente à la fin → relancez avec **plus** d'époques.
- Stabilisée bien avant la fin → le réseau a fini.
- Remonte vers la fin → **surapprentissage**, réduisez les époques ou les neurones.
"""

AIDE_TAILLE_LOT = """
### Taille de lot

Nombre de lignes traitées **en une fois** à chaque étape d'apprentissage (mini-batch).

- **Petit lot (8–16)** : mises à jour fréquentes, utile sur petits fichiers.
- **Grand lot (64–256)** : plus stable, utile sur grands fichiers.

Les valeurs par défaut conviennent dans la plupart des cas.
"""

AIDE_DONNEES_TEST = """
### % données de test

Fraction des données **mises de côté** pour évaluer le modèle (jamais vues à l'entraînement).

Exemple : **20 %** → le réseau apprend sur 80 % des lignes, les métriques (MAE, R²) sont calculées sur les 20 % restants.

> Ne mettez pas 0 % : vous ne sauriez pas si le modèle généralise vraiment.
"""

AIDE_GRAINE = """
### Graine aléatoire

Nombre qui fixe le **hasard** (initialisation des poids, découpage train/test).

Avec la **même graine**, vous obtenez les **mêmes résultats** à chaque entraînement — utile pour comparer deux réglages.

Changez-la si vous voulez vérifier que vos résultats ne dépendent pas d'un coup de chance.
"""


def injecter_style_puces_sidebar() -> None:
    """Harmonise le fond des puces ℹ️ avec la barre latérale."""
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] div[data-testid="stPopover"] > button {
            background-color: var(--secondary-background-color) !important;
            border: 1px solid transparent !important;
            box-shadow: none !important;
            padding: 0.15rem 0.35rem !important;
            min-height: 0 !important;
        }
        section[data-testid="stSidebar"] div[data-testid="stPopover"] > button:hover {
            background-color: rgba(151, 166, 195, 0.25) !important;
            border-color: transparent !important;
        }
        section[data-testid="stSidebar"] button[kind="secondary"][data-testid="stBaseButton-secondary"] {
            background-color: var(--secondary-background-color) !important;
            border: 1px solid transparent !important;
            box-shadow: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _ouvrir_popup(titre: str, contenu: str) -> None:
    if not hasattr(st, "dialog"):
        return

    @st.dialog(titre)
    def _popup():
        st.markdown(contenu)

    _popup()


def afficher_puce_aide(cle: str, titre: str, contenu: str) -> None:
    """Puce ℹ️ centrée sous un graphique (popover, sans relancer l'entraînement)."""
    _, col_btn, _ = st.columns([2, 1, 2])
    with col_btn:
        if hasattr(st, "popover"):
            with st.popover("ℹ️", help="Explication"):
                st.markdown(f"**{titre}**\n\n{contenu}" if titre else contenu)
            return
        if hasattr(st, "dialog") and st.button("ℹ️", key=f"aide_graph_{cle}", help="Explication"):
            _ouvrir_popup(titre, contenu)


def afficher_puce_aide_reglage(cle: str, titre: str, contenu: str) -> None:
    """Puce ℹ️ à côté d'un titre de réglage (barre latérale)."""
    if hasattr(st, "popover"):
        with st.popover("ℹ️", help="Explication"):
            st.markdown(contenu)
        return
    if hasattr(st, "dialog") and st.button("ℹ️", key=f"aide_reg_{cle}", help="Explication"):
        _ouvrir_popup(titre, contenu)
