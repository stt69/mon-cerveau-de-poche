## Estimer le rendement fromager

---

Combien de kilos de meules pour ce volume de lait ? Le rendement fromager dépend de la matière grasse, des protéines, de la saison et des paramètres de fabrication.

Ce cas estime le **poids des meules (kg)** à partir des caractéristiques du lait et du procédé.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_fromagerie_rendement.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_fromage | Type de fromage (1–5) | 3 |
| Volume_lait_L | Volume de lait (L) | 500.0 |
| MG_gL | Matière grasse (g/L) | 39.0 |
| Proteines_gL | Protéines (g/L) | 33.0 |
| Nb_producteurs | Nombre de producteurs | 4 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Temperature_lait_C | Température du lait (°C) | 8.0 |
| Acidite_Dornic | Acidité Dornic | 17.0 |
| Presure | Présure (1–2) | 1 |
| Temperature_chauffage_C | Température de chauffage (°C) | 53.0 |
| Duree_brassage_min | Durée de brassage (min) | 45 |
| **Poids_meules_kg** | **Poids des meules (kg)** | **40** |

La colonne **Poids_meules_kg** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_fromagerie_rendement.xlsx`.

Vérifiez l'aperçu : environ 300 lignes, 12 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Poids_meules_kg** comme colonne cible.

Les 11 autres colonnes deviennent automatiquement les entrées.

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
| Type_fromage | 3 |
| Volume_lait_L | 500.0 |
| MG_gL | 39.0 |
| Proteines_gL | 33.0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Rendement prédit aide à planifier saloirage et commandes de lait.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_fromagerie_rendement.xlsx` et entraînez sur **Poids_meules_kg**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
