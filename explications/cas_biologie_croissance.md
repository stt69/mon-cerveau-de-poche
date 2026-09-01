## Estimer la croissance d'une culture biologique

---

En laboratoire, la croissance d'une culture dépend du milieu, de la température, du pH et du substrat. Prédire la densité optique finale aide à planifier les expériences.

Ce cas estime la **densité optique** à partir des paramètres de culture.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_biologie_croissance.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Milieu | Milieu de culture (1–4) | 2 |
| Temperature_C | Température (°C) | 31.0 |
| pH | pH | 6.5 |
| Duree_incubation_h | Durée d'incubation (h) | 39 |
| Concentration_substrat | Concentration substrat | 5.0 |
| **Densite_optique** | **Densité optique** | **0.85** |

La colonne **Densite_optique** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_biologie_croissance.xlsx`.

Vérifiez l'aperçu : environ 300 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Densite_optique** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 300 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** . Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Milieu | 2 |
| Temperature_C | 31.0 |
| pH | 6.5 |
| Duree_incubation_h | 39 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Ajustez température ou pH si la croissance prédite est insuffisante.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_biologie_croissance.xlsx` et entraînez sur **Densite_optique**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
