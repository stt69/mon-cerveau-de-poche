"""
CerveauPoche — Moteur de réseau de neurones en NumPy pur.

Livre : "Mon Cerveau de Poche"
Chapitre 73 — Sous le capot (pour les curieux)

Ce fichier contient TOUT le moteur du réseau de neurones.
Aucune dépendance lourde (pas de TensorFlow, pas de scikit-learn).
Uniquement NumPy.
"""

import numpy as np
import json
import zipfile
import io
import re


# ════════════════════════════════════════════════════════════════════
#  Normaliseur (équivalent de MinMaxScaler)
# ════════════════════════════════════════════════════════════════════

class Normaliseur:
    """
    Normalisation Min-Max : ramène chaque colonne entre 0 et 1.

    Pourquoi normaliser ?
    Si une colonne va de 0 à 100 000 et une autre de 0 à 1,
    le réseau ne "voit" que la grande colonne.
    La normalisation met toutes les colonnes sur un pied d'égalité.
    """

    def __init__(self):
        self.min_ = None
        self.echelle_ = None

    def ajuster(self, X):
        """Apprend le min et le max de chaque colonne."""
        self.min_ = X.min(axis=0)
        plage = X.max(axis=0) - self.min_
        plage[plage == 0] = 1.0  # éviter la division par zéro
        self.echelle_ = plage
        return self

    def transformer(self, X):
        """Applique la normalisation : (valeur - min) / (max - min)."""
        return (X - self.min_) / self.echelle_

    def ajuster_transformer(self, X):
        """Apprend puis transforme en une seule étape."""
        self.ajuster(X)
        return self.transformer(X)

    def inverser(self, X_norm):
        """Retransforme en valeurs originales."""
        return X_norm * self.echelle_ + self.min_

    def to_dict(self):
        return {'min': self.min_.tolist(), 'echelle': self.echelle_.tolist()}

    @classmethod
    def from_dict(cls, d):
        n = cls()
        n.min_ = np.array(d['min'])
        n.echelle_ = np.array(d['echelle'])
        return n


# ════════════════════════════════════════════════════════════════════
#  CerveauPoche — Le réseau de neurones
# ════════════════════════════════════════════════════════════════════

class CerveauPoche:
    """
    Réseau de neurones multicouche (perceptron multicouche).

    Paramètres
    ----------
    architecture : liste d'entiers
        Ex: [5, 16, 16, 1] → 5 entrées, 2 couches cachées de 16, 1 sortie.
    activation : str
        Fonction d'activation des couches cachées : 'relu', 'sigmoid', 'tanh'.
    mode : str
        'regression' (sortie linéaire, perte MSE)
        'classification' (sortie softmax, perte entropie croisée)
    taux_apprentissage : float
        Taille du pas de correction (le "learning rate").
    optimiseur : str
        'adam' (recommandé) ou 'sgd' (plus simple).
    graine : int
        Pour la reproductibilité.
    """

    VERSION = "1.0.0"

    def __init__(self, architecture, activation='relu', mode='regression',
                 taux_apprentissage=0.001, optimiseur='adam', graine=42):
        self.architecture = list(architecture)
        self.activation = activation
        self.mode = mode
        self.lr = taux_apprentissage
        self.optimiseur = optimiseur
        self.graine = graine
        self.rng = np.random.default_rng(graine)

        self._init_poids()

    # ── Initialisation des poids ────────────────────────────

    def _init_poids(self):
        """Crée les matrices de poids et biais avec une bonne initialisation."""
        self.poids = []
        self.biais = []

        for i in range(len(self.architecture) - 1):
            n_in = self.architecture[i]
            n_out = self.architecture[i + 1]

            # Initialisation He (relu) ou Xavier (sigmoid/tanh)
            if self.activation == 'relu':
                std = np.sqrt(2.0 / n_in)
            else:
                std = np.sqrt(2.0 / (n_in + n_out))

            W = self.rng.normal(0, std, (n_in, n_out))
            b = np.zeros((1, n_out))
            self.poids.append(W)
            self.biais.append(b)

        # État interne d'Adam (moments de premier et second ordre)
        if self.optimiseur == 'adam':
            self._adam_mw = [np.zeros_like(w) for w in self.poids]
            self._adam_vw = [np.zeros_like(w) for w in self.poids]
            self._adam_mb = [np.zeros_like(b) for b in self.biais]
            self._adam_vb = [np.zeros_like(b) for b in self.biais]
            self._adam_t = 0

    # ── Fonctions d'activation ──────────────────────────────

    def _activer(self, z):
        """Applique la fonction d'activation aux couches cachées."""
        if self.activation == 'relu':
            return np.maximum(0, z)
        elif self.activation == 'sigmoid':
            return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))
        elif self.activation == 'tanh':
            return np.tanh(z)
        return z

    def _activer_deriv(self, a, z):
        """Dérivée de la fonction d'activation (pour la rétropropagation)."""
        if self.activation == 'relu':
            return (z > 0).astype(np.float64)
        elif self.activation == 'sigmoid':
            return a * (1.0 - a)
        elif self.activation == 'tanh':
            return 1.0 - a ** 2
        return np.ones_like(z)

    @staticmethod
    def _softmax(z):
        """Softmax : transforme des scores en probabilités (classification)."""
        z_shift = z - z.max(axis=1, keepdims=True)
        exp_z = np.exp(z_shift)
        return exp_z / exp_z.sum(axis=1, keepdims=True)

    # ── Propagation avant ───────────────────────────────────

    def propagation_avant(self, X):
        """
        Calcule la sortie du réseau pour les entrées X.
        Exactement ce que vous avez fait à la main au chapitre 4 dans Excel,
        mais automatisé pour N neurones et N couches.
        """
        self._z = []       # valeurs avant activation
        self._a = [X]      # valeurs après activation (a[0] = entrée)

        a = X
        n_couches = len(self.poids)

        for i in range(n_couches):
            z = a @ self.poids[i] + self.biais[i]
            self._z.append(z)

            if i < n_couches - 1:
                # Couches cachées → activation choisie
                a = self._activer(z)
            else:
                # Couche de sortie
                if self.mode == 'classification':
                    a = self._softmax(z)
                else:
                    a = z  # linéaire pour la régression

            self._a.append(a)

        return a

    # ── Propagation arrière (rétropropagation) ──────────────

    def propagation_arriere(self, y):
        """
        Ajuste les poids en remontant l'erreur de la sortie vers l'entrée.
        C'est l'algorithme de la chaîne de production (chapitre 73) :
        on mesure le défaut, on remonte poste par poste.
        """
        m = y.shape[0]
        n_couches = len(self.poids)

        # Gradient initial (identique pour MSE+linéaire et softmax+cross-entropy)
        delta = (self._a[-1] - y) / m

        grad_w = [None] * n_couches
        grad_b = [None] * n_couches

        for i in range(n_couches - 1, -1, -1):
            grad_w[i] = self._a[i].T @ delta
            grad_b[i] = np.sum(delta, axis=0, keepdims=True)

            if i > 0:
                delta = delta @ self.poids[i].T
                delta *= self._activer_deriv(self._a[i], self._z[i - 1])

        # Clippage des gradients (stabilité numérique)
        norme = np.sqrt(sum(np.sum(g ** 2) for g in grad_w + grad_b))
        if norme > 5.0:
            facteur = 5.0 / (norme + 1e-8)
            grad_w = [g * facteur for g in grad_w]
            grad_b = [g * facteur for g in grad_b]

        # Mise à jour des poids
        self._mettre_a_jour(grad_w, grad_b)

    def _mettre_a_jour(self, grad_w, grad_b):
        """Applique la mise à jour des poids (SGD ou Adam)."""
        if self.optimiseur == 'adam':
            self._adam_t += 1
            b1, b2, eps = 0.9, 0.999, 1e-8
            correction1 = 1 - b1 ** self._adam_t
            correction2 = 1 - b2 ** self._adam_t

            for i in range(len(self.poids)):
                # Poids
                self._adam_mw[i] = b1 * self._adam_mw[i] + (1 - b1) * grad_w[i]
                self._adam_vw[i] = b2 * self._adam_vw[i] + (1 - b2) * grad_w[i] ** 2
                mh = self._adam_mw[i] / correction1
                vh = self._adam_vw[i] / correction2
                self.poids[i] -= self.lr * mh / (np.sqrt(vh) + eps)

                # Biais
                self._adam_mb[i] = b1 * self._adam_mb[i] + (1 - b1) * grad_b[i]
                self._adam_vb[i] = b2 * self._adam_vb[i] + (1 - b2) * grad_b[i] ** 2
                mh = self._adam_mb[i] / correction1
                vh = self._adam_vb[i] / correction2
                self.biais[i] -= self.lr * mh / (np.sqrt(vh) + eps)
        else:
            # SGD classique
            for i in range(len(self.poids)):
                self.poids[i] -= self.lr * grad_w[i]
                self.biais[i] -= self.lr * grad_b[i]

    # ── Entraînement ────────────────────────────────────────

    def entrainer(self, X, y, epoques=100, taille_lot=32,
                  X_val=None, y_val=None, rappel=None):
        """
        Entraîne le réseau sur les données.

        rappel : function(epoque, historique) → appelée après chaque époque.
                 Permet l'animation en temps réel dans l'application.
        """
        historique = {
            'mae_train': [], 'mae_val': [],
            'perte_train': [], 'perte_val': [],
        }
        m = X.shape[0]

        for ep in range(epoques):
            # Mélanger les données (mini-lots aléatoires)
            idx = self.rng.permutation(m)
            X_mel, y_mel = X[idx], y[idx]

            for debut in range(0, m, taille_lot):
                fin = min(debut + taille_lot, m)
                self.propagation_avant(X_mel[debut:fin])
                self.propagation_arriere(y_mel[debut:fin])

            # ── Métriques après chaque époque ──
            pred_t = self.propagation_avant(X)
            historique['mae_train'].append(float(np.mean(np.abs(pred_t - y))))
            historique['perte_train'].append(float(np.mean((pred_t - y) ** 2)))

            if X_val is not None:
                pred_v = self.propagation_avant(X_val)
                historique['mae_val'].append(float(np.mean(np.abs(pred_v - y_val))))
                historique['perte_val'].append(float(np.mean((pred_v - y_val) ** 2)))

            if rappel:
                rappel(ep, historique)

        return historique

    # ── Prédiction ──────────────────────────────────────────

    def predire(self, X):
        """Prédit les sorties pour de nouvelles entrées."""
        return self.propagation_avant(X)

    # ── Sauvegarde / Chargement ─────────────────────────────

    def vers_bytes(self, norm_X=None, norm_y=None,
                   colonnes_entree=None, colonnes_cible=None,
                   mode_cls_classes=None):
        """Sauvegarde le modèle complet dans un .zip en mémoire."""
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Poids (format NumPy compressé)
            d = {}
            for i, (w, b) in enumerate(zip(self.poids, self.biais)):
                d[f'W{i}'] = w
                d[f'b{i}'] = b
            pbuf = io.BytesIO()
            np.savez_compressed(pbuf, **d)
            zf.writestr('poids.npz', pbuf.getvalue())

            # Métadonnées JSON
            meta = {
                'version': self.VERSION,
                'architecture': self.architecture,
                'activation': self.activation,
                'mode': self.mode,
                'optimiseur': self.optimiseur,
                'taux_apprentissage': self.lr,
                'colonnes_entree': [str(c) for c in colonnes_entree] if colonnes_entree is not None else [],
                'colonnes_cible': [str(c) for c in colonnes_cible] if colonnes_cible is not None else [],
            }
            if norm_X:
                meta['normaliseur_X'] = norm_X.to_dict()
            if norm_y:
                meta['normaliseur_y'] = norm_y.to_dict()
            if mode_cls_classes is not None:
                meta['classes'] = [int(c) for c in mode_cls_classes]

            zf.writestr('meta.json', json.dumps(meta, ensure_ascii=False, indent=2))

        buf.seek(0)
        return buf.getvalue()

    @classmethod
    def depuis_bytes(cls, zip_bytes):
        """
        Charge un modèle depuis un .zip.
        Retourne : (reseau, norm_X, norm_y, colonnes_entree, colonnes_cible, meta)
        """
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            meta = json.loads(zf.read('meta.json'))
            poids_data = np.load(io.BytesIO(zf.read('poids.npz')))

        reseau = cls(
            architecture=meta['architecture'],
            activation=meta['activation'],
            mode=meta.get('mode', 'regression'),
            optimiseur=meta.get('optimiseur', 'adam'),
            taux_apprentissage=meta.get('taux_apprentissage', 0.001),
        )
        for i in range(len(reseau.poids)):
            reseau.poids[i] = poids_data[f'W{i}']
            reseau.biais[i] = poids_data[f'b{i}']

        norm_X = Normaliseur.from_dict(meta['normaliseur_X']) if 'normaliseur_X' in meta else None
        norm_y = Normaliseur.from_dict(meta['normaliseur_y']) if 'normaliseur_y' in meta else None

        return (reseau, norm_X, norm_y,
                meta.get('colonnes_entree', []),
                meta.get('colonnes_cible', []),
                meta)


# ════════════════════════════════════════════════════════════════════
#  Régression linéaire multiple (baseline classique)
# ════════════════════════════════════════════════════════════════════

class RegressionLineaire:
    """
    Régression linéaire multiple par moindres carrés (NumPy pur).
    y = b0 + b1*x1 + ... + bp*xp  (une équation par cible)
    """

    def ajuster(self, X, y):
        X = np.asarray(X, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64)
        if y.ndim == 1:
            y = y.reshape(-1, 1)
        n = X.shape[0]
        X_aug = np.hstack([np.ones((n, 1)), X])
        self.coef_, _, self.rank, _ = np.linalg.lstsq(X_aug, y, rcond=None)
        if self.coef_.ndim == 1:
            self.coef_ = self.coef_.reshape(-1, 1)
        self.n_entrees = X.shape[1]
        self.n_cibles = self.coef_.shape[1]
        return self

    def predire(self, X):
        X = np.asarray(X, dtype=np.float64)
        n = X.shape[0]
        X_aug = np.hstack([np.ones((n, 1)), X])
        pred = X_aug @ self.coef_
        if self.n_cibles == 1:
            return pred.reshape(-1, 1)
        return pred

    def intercept(self, idx_cible=0):
        return float(self.coef_[0, idx_cible])

    def coefficients(self, idx_cible=0):
        return self.coef_[1:, idx_cible].copy()


def _lettre_colonne_excel(index_entree, colonne_depart=2):
    """Index entrée 0 → B, 1 → C, … (ligne de données = 2)."""
    n = index_entree + colonne_depart
    lettres = ""
    while n > 0:
        n, reste = divmod(n - 1, 26)
        lettres = chr(65 + reste) + lettres
    return lettres


def _fmt_fr_nombre(x, signe_explicite=False):
    """Nombre pour équation lisible (virgule décimale, espaces milliers)."""
    if signe_explicite:
        if x >= 0:
            prefix = " + "
        else:
            prefix = " − "
        corps = f"{abs(x):,.6f}".rstrip("0").rstrip(",")
        if corps.endswith(","):
            corps += "0"
        corps = corps.replace(",", "X").replace(".", ",").replace("X", " ")
        return prefix + corps
    corps = f"{x:,.6f}".rstrip("0").rstrip(",")
    if corps.endswith(","):
        corps += "0"
    return corps.replace(",", "X").replace(".", ",").replace("X", " ")


def _fmt_excel_nombre(x):
    """Nombre dans une formule Excel (locale FR : virgule décimale)."""
    s = f"{x:.10g}".replace(".", ",")
    return s


def _nom_python_safe(nom):
    """Identifiant Python approximatif (clés dict = nom exact)."""
    s = re.sub(r"[^\w]", "_", str(nom), flags=re.UNICODE)
    if s and s[0].isdigit():
        s = "_" + s
    return s or "cible"


def formater_formules_regression(reg, colonnes_entree, colonnes_cible, ligne_excel=2):
    """
    Formats exportables pour chaque cible.
    Retourne une liste de dicts : cible, equation, excel, python, legende_excel.
    """
    colonnes_entree = [str(c) for c in colonnes_entree]
    colonnes_cible = [str(c) for c in colonnes_cible]
    resultats = []

    for j, cible in enumerate(colonnes_cible):
        b0 = reg.intercept(j)
        coefs = reg.coefficients(j)

        # ── Équation lisible ──
        parties_eq = []
        for nom, c in zip(colonnes_entree, coefs):
            if abs(c) < 1e-15:
                continue
            parties_eq.append(f"{_fmt_fr_nombre(c, signe_explicite=True)} × {nom}")
        equation = f"{cible} = {_fmt_fr_nombre(b0)}{''.join(parties_eq)}"

        # ── Formule Excel (références B2, C2, …) ──
        parties_xl = [_fmt_excel_nombre(b0)]
        legende = []
        for i, (nom, c) in enumerate(zip(colonnes_entree, coefs)):
            col = _lettre_colonne_excel(i)
            ref = f"{col}{ligne_excel}"
            legende.append(f"{col} = {nom}")
            if abs(c) < 1e-15:
                continue
            if c >= 0:
                parties_xl.append(f"+{ _fmt_excel_nombre(c)}*{ref}")
            else:
                parties_xl.append(f"{_fmt_excel_nombre(c)}*{ref}")
        excel = "=" + "".join(parties_xl)

        # ── Snippet Python ──
        nom_fn = _nom_python_safe(cible)
        lignes_py = [
            f"def predire_{nom_fn}(ligne: dict) -> float:",
            f'    """Prédiction régression linéaire — cible : {cible}."""',
            "    return (",
            f"        {b0}",
        ]
        for nom, c in zip(colonnes_entree, coefs):
            if abs(c) < 1e-15:
                continue
            nom_esc = str(nom).replace("\\", "\\\\").replace('"', '\\"')
            if c >= 0:
                lignes_py.append(f'        + {c} * ligne["{nom_esc}"]')
            else:
                lignes_py.append(f'        {c} * ligne["{nom_esc}"]')
        lignes_py.append("    )")
        lignes_py.append("")
        lignes_py.append("# Exemple :")
        lignes_py.append("# ligne = {")
        for nom in colonnes_entree:
            nom_esc = str(nom).replace("\\", "\\\\").replace('"', '\\"')
            lignes_py.append(f'#     "{nom_esc}": 0.0,')
        lignes_py.append("# }")
        lignes_py.append(f"# resultat = predire_{nom_fn}(ligne)  # → {cible}")
        python = "\n".join(lignes_py)

        resultats.append({
            "cible": cible,
            "equation": equation,
            "excel": excel,
            "python": python,
            "legende_excel": " · ".join(legende),
        })

    return resultats


def recommandation_favorise_regression(titre):
    """True si la recommandation oriente vers la régression plutôt que le réseau."""
    return titre != "Le réseau de neurones est indiqué"


def indices_decoupe(n, test_pct=0.2, graine=42):
    """Indices train / test (même logique que decouper_donnees)."""
    rng = np.random.default_rng(graine)
    idx = rng.permutation(n)
    coupe = int(n * (1 - test_pct))
    return idx[:coupe], idx[coupe:]


def recommander_reseau(mae_reg, mae_nn, r2_reg, r2_nn, n_lignes,
                       mae_train_nn=None, mae_val_nn=None):
    """
    Aide à décider si le réseau apporte un gain mesurable.
    Retourne (titre, message, style) avec style in {'success','info','warning'}.
    """
    mae_reg_m = float(np.mean(np.atleast_1d(mae_reg)))
    mae_nn_m = float(np.mean(np.atleast_1d(mae_nn)))
    r2_reg_m = float(np.mean(np.atleast_1d(r2_reg)))
    r2_nn_m = float(np.mean(np.atleast_1d(r2_nn)))

    gain_mae = (mae_reg_m - mae_nn_m) / (mae_reg_m + 1e-10)
    gain_r2 = r2_nn_m - r2_reg_m

    surapprentissage = (
        mae_train_nn is not None and mae_val_nn is not None
        and mae_val_nn > 1e-10
        and mae_train_nn < 0.5 * mae_val_nn
    )

    if r2_reg_m < 0.3 and r2_nn_m < 0.3:
        return (
            "Modèles peu performants",
            "Régression et réseau expliquent mal la cible (R² < 0,3). "
            "Vérifiez les données, les colonnes d'entrée ou le volume d'exemples "
            "avant de choisir un modèle.",
            "warning",
        )

    if r2_reg_m >= 0.95 and gain_mae < 0.05:
        # Pas de phrase sur le MAE du réseau : si gain_mae ≤ 0, la régression
        # est meilleure ; un « améliore marginalement » négatif serait trompeur.
        return (
            "La régression linéaire suffit",
            f"La régression explique déjà {r2_reg_m:.0%} de la variance "
            f"(R² = {r2_reg_m:.3f}). Un modèle simple est préférable.",
            "success",
        )

    if surapprentissage and gain_mae < 0.15 and n_lignes < 200:
        return (
            "Prudence avec le réseau",
            "Le réseau semble sur-apprendre (erreur entraînement << erreur test) "
            f"avec seulement {n_lignes} lignes. La régression linéaire est plus "
            "stable ; n'augmentez la complexité du réseau que si vous avez plus de données.",
            "warning",
        )

    if gain_mae >= 0.10 or gain_r2 >= 0.05:
        if n_lignes >= 100:
            return (
                "Le réseau de neurones est indiqué",
                f"Sur le jeu de test, le réseau réduit la MAE d'environ {gain_mae:.0%} "
                f"et gagne {gain_r2:+.3f} en R² par rapport à la régression. "
                "Des relations non linéaires sont probablement présentes.",
                "info",
            )
        return (
            "Gain visible, données limitées",
            f"Le réseau semble meilleur ({gain_mae:.0%} sur la MAE), mais avec "
            f"{n_lignes} lignes seulement, validez sur de nouvelles données avant "
            "de vous y fier.",
            "warning",
        )

    if abs(gain_mae) < 0.03 and abs(gain_r2) < 0.02:
        return (
            "La régression linéaire suffit",
            "Les deux méthodes donnent des résultats très proches sur le jeu de test. "
            "Privilégiez la régression : plus simple, plus facile à interpréter.",
            "success",
        )

    return (
        "Résultats proches",
        "Le réseau n'apporte qu'un gain modeste ou incertain. "
        "Commencez par la régression linéaire ; n'utilisez le réseau que si "
        "vous avez une raison métier de chercher des relations plus complexes.",
        "warning",
    )


# ════════════════════════════════════════════════════════════════════
#  Utilitaires
# ════════════════════════════════════════════════════════════════════

def decouper_donnees(X, y, test_pct=0.2, graine=42):
    """Sépare les données en ensemble d'entraînement et de test."""
    rng = np.random.default_rng(graine)
    n = X.shape[0]
    idx = rng.permutation(n)
    coupe = int(n * (1 - test_pct))
    return X[idx[:coupe]], X[idx[coupe:]], y[idx[:coupe]], y[idx[coupe:]]


def calculer_r2(y_vrai, y_pred):
    """R² : proportion de la variance expliquée par le modèle."""
    ss_res = np.sum((y_vrai - y_pred) ** 2, axis=0)
    ss_tot = np.sum((y_vrai - y_vrai.mean(axis=0)) ** 2, axis=0)
    r2 = 1 - ss_res / (ss_tot + 1e-10)
    return r2


def calculer_mae(y_vrai, y_pred):
    """MAE : erreur absolue moyenne, par colonne cible."""
    return np.mean(np.abs(y_vrai - y_pred), axis=0)
