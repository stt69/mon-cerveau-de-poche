## Anticiper les besoins en présure, ferments et sel

---

Présure, ferments, sel, toiles, morge : les besoins d'une fromagerie dépendent du volume de lait et du mix de fabrications prévu.

Ce cas prédit **cinq fournitures en parallèle** (multi-sorties) pour le mois à venir.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_fromagerie_fournitures.xlsx`

Le fichier contient environ 120 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Mois | Mois (1–12) | 6 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Volume_lait_L | Volume de lait (L) | 3500.0 |
| Fabrications_gruyere | Fabrications Gruyère | 17 |
| Fabrications_vacherin | Fabrications Vacherin | 6 |
| Fabrications_autres | Autres fabrications | 5 |
| Temperature_cave_C | Température de cave (°C) | 13.0 |
| Meules_en_affinage | Meules en affinage | 175 |
| **Presure_L** | **Présure (L)** | **3.5** |
| **Ferments_doses** | **Ferments (doses)** | **9** |
| **Sel_kg** | **Sel (kg)** | **25** |
| **Toiles_unites** | **Toiles (unités)** | **15** |
| **Morge_L** | **Morge (L)** | **6** |

La colonne **Presure_L** / **Ferments_doses** / **Sel_kg** / **Toiles_unites** / **Morge_L** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_fromagerie_fournitures.xlsx`. Vérifiez : environ 120 lignes, 13 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Presure_L
- Ferments_doses
- Sel_kg
- Toiles_unites
- Morge_L

Les 8 colonnes restantes deviennent les entrées. Le réseau prédit 5 sorties **en parallèle**.

#### Étape 3 — Choisir les réglages

Préréglage **Petit** (1 couche, 8 neurones, 200 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**. La régression linéaire s'affiche d'abord, puis le réseau (courbe d'erreur pour chaque sortie).

#### Étape 5 — Analyser les résultats

Consultez le tableau comparatif et la recommandation. Vérifiez MAE et R² pour chaque cible.

#### Étape 6 — Prédire

Entrez les entrées du prochain cas :

| Entrée | Valeur |
|--------|--------|
| Mois | 6 |
| Saison | 2 |
| Volume_lait_L | 3500.0 |
| Fabrications_gruyere | 17 |

Le réseau affiche simultanément : **Presure_L**, **Ferments_doses**, **Sel_kg**, **Toiles_unites**, **Morge_L**.

---

### Interpréter le résultat pour prendre une décision

Commandes présure/ferments/sel avant rupture de stock.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_fromagerie_fournitures.xlsx` et sélectionnez les cibles : Presure_L, Ferments_doses, Sel_kg, Toiles_unites, Morge_L.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
