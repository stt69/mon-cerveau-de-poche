## Prévoir les volumes de lait collectés

---

La collecte de lait varie avec la saison, l'alpage, la météo et le nombre de producteurs. Prévoir le volume hebdomadaire aide à dimensionner cuves et transport.

Ce cas prédit le **volume de lait collecté (L)**.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_fromagerie_collecte.xlsx`

Le fichier contient environ 156 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Semaine | Numéro de semaine (1–52) | 26 |
| Mois | Mois (1–12) | 6 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Nb_producteurs | Nombre de producteurs | 8 |
| Vaches_lactation | Vaches en lactation | 80 |
| Alpage | Alpage (0/1) | 0 |
| Temperature_moy_C | Température moyenne (°C) | 11.5 |
| Pluviometrie_mm | Pluviométrie (mm) | 42.5 |
| Prix_lait_ct_L | Prix du lait (ct/L) | 70.0 |
| **Volume_lait_L** | **Volume de lait (L)** | **2750** |

La colonne **Volume_lait_L** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_fromagerie_collecte.xlsx`.

Vérifiez l'aperçu : environ 156 lignes, 10 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Volume_lait_L** comme colonne cible.

Les 9 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 156 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** . Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Semaine | 26 |
| Mois | 6 |
| Saison | 2 |
| Nb_producteurs | 8 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Dimensionnez cuves et tournées de collecte selon le volume prédit.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_fromagerie_collecte.xlsx` et entraînez sur **Volume_lait_L**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
