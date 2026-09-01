## Estimer le temps de production

---

Combien d'heures pour cette commande ? Quel délai annoncer au client ? Le chef d'atelier a une intuition, mais elle varie selon la charge, le type de produit et la complexité.

Ce cas apprend à estimer le **temps de production en heures** à partir de l'historique réel de l'atelier.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_production_temps.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_produit | Type de produit (1–6) | 3 |
| Quantite | Quantité | 255 |
| Complexite | Complexité (1–5) | 3 |
| Charge_atelier_pct | Charge atelier (%) | 60.0 |
| Nb_postes | Nombre de postes actifs | 3 |
| **Temps_heures** | **Temps de production (h)** | **19** |

La colonne **Temps_heures** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_production_temps.xlsx`.

Vérifiez l'aperçu : environ 300 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Temps_heures** comme colonne cible.

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
| Type_produit | 2 |
| Quantite | 80 |
| Complexite | 1 |
| Charge_atelier_pct | 60 |
| Nb_postes | 3 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Temps estimé × coût horaire = base de devis. Ajoutez une marge avec le MAE.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_production_temps.xlsx` et entraînez sur **Temps_heures**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
