## Estimer le rendement d'une parcelle agricole

---

Quel rendement attendre de cette parcelle cette année ? Culture, sol, pluie, engrais et irrigation interagissent — l'historique de l'exploitation contient la réponse empirique.

Ce cas estime le **rendement en t/ha**.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_agriculture_rendement.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Culture | Culture (1–6) | 3 |
| Surface_ha | Surface (ha) | 10.2 |
| Type_sol | Type de sol (1–4) | 2 |
| Pluviometrie_mm | Pluviométrie (mm) | 600.0 |
| Engrais_kg_ha | Engrais (kg/ha) | 150.0 |
| Irrigation | Irrigation (0/1) | 0 |
| **Rendement_t_ha** | **Rendement (t/ha)** | **6** |

La colonne **Rendement_t_ha** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_agriculture_rendement.xlsx`.

Vérifiez l'aperçu : environ 200 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Rendement_t_ha** comme colonne cible.

Les 6 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 200 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** . Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Culture | 3 |
| Surface_ha | 10.2 |
| Type_sol | 2 |
| Pluviometrie_mm | 600.0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Rendement prédit guide les ventes à terme et la logistique de stockage.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_agriculture_rendement.xlsx` et entraînez sur **Rendement_t_ha**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
