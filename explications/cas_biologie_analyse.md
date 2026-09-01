## Prévoir les résultats d'une analyse

---

Avant même de lancer l'analyse, certains paramètres laissent présager le résultat. Le réseau apprend ces corrélations sur l'historique du laboratoire.

Ce cas prédit la **concentration résultat** à partir du protocole et de l'échantillon.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_biologie_analyse.xlsx`

Le fichier contient environ 400 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_echantillon | Type d'échantillon (1–5) | 3 |
| Volume_mL | Volume (mL) | 25.2 |
| Reactif | Réactif (1–4) | 2 |
| Temperature_reaction | Température de réaction (°C) | 40.0 |
| Temps_reaction_min | Temps de réaction (min) | 62 |
| **Concentration_resultat** | **Concentration résultat** | **3** |

La colonne **Concentration_resultat** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_biologie_analyse.xlsx`.

Vérifiez l'aperçu : environ 400 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Concentration_resultat** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 400 lignes, utilisez le préréglage **Grand** (2 couches, 32 neurones, 400 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** . Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Type_echantillon | 3 |
| Volume_mL | 25.2 |
| Reactif | 2 |
| Temperature_reaction | 40.0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Validez les protocoles dont le résultat prédit sort des normes avant de lancer la série.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_biologie_analyse.xlsx` et entraînez sur **Concentration_resultat**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
