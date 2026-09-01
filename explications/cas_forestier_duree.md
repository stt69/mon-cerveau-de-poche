## Chapitre 53 — Prévoir le temps d'exploitation d'un chantier forestier

---

Combien de jours pour exploiter cette parcelle ? Le volume, la pente, l'accessibilité et la météo modifient fortement la durée réelle constatée.

Ce chapitre estime la **durée d'exploitation en jours**.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_forestier_duree.xlsx`

Le fichier contient environ 150 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Volume_m3_estime | Volume estimé (m³) | 160.0 |
| Pente_pct | Pente (%) | 30.0 |
| Accessibilite | Accessibilité (1–3) | 2 |
| Meteo_prevue | Météo prévue (1–4) | 2 |
| Nb_machines | Nombre de machines | 2 |
| **Duree_jours** | **Durée (jours)** | **10.5** |

La colonne **Duree_jours** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_forestier_duree.xlsx`.

Vérifiez l'aperçu : environ 150 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Duree_jours** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 150 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** (chapitre 10). Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Volume_m3_estime | 160.0 |
| Pente_pct | 30.0 |
| Accessibilite | 2 |
| Meteo_prevue | 2 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Planifiez machines et équipes selon la durée prédite.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_forestier_duree.xlsx` et entraînez sur **Duree_jours**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
