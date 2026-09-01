## Anticiper les besoins en matières premières

---

Commander les matières premières au bon moment et en bonne quantité limite les immobilisations et les ruptures. La consommation dépend du plan de production et du mix produits.

Ce cas prédit **plusieurs matières en une fois** (multi-sorties) à partir de la production prévue.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_production_matieres.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Mois | Mois (1–12) | 6 |
| Production_prevue_unites | Production prévue (unités) | 1050 |
| Type_produit_principal | Produit principal (1–4) | 2 |
| Nb_references | Nombre de références | 17 |
| **Matiere_A_kg** | **Matière A (kg)** | **150** |
| **Matiere_B_kg** | **Matière B (kg)** | **105** |
| **Emballage_unites** | **Emballages (unités)** | **350** |
| **Energie_kWh** | **Énergie (kWh)** | **600** |

La colonne **Matiere_A_kg** / **Matiere_B_kg** / **Emballage_unites** / **Energie_kWh** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_production_matieres.xlsx`. Vérifiez : environ 200 lignes, 8 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Matiere_A_kg
- Matiere_B_kg
- Emballage_unites
- Energie_kWh

Les 4 colonnes restantes deviennent les entrées. Le réseau prédit 4 sorties **en parallèle**.

#### Étape 3 — Choisir les réglages

Préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**. La régression linéaire s'affiche d'abord, puis le réseau (courbe d'erreur pour chaque sortie).

#### Étape 5 — Analyser les résultats

Consultez le tableau comparatif et la recommandation. Vérifiez MAE et R² pour chaque cible.

#### Étape 6 — Prédire

Entrez les entrées du prochain cas :

| Entrée | Valeur |
|--------|--------|
| Mois | 6 |
| Production_prevue_unites | 1050 |
| Type_produit_principal | 2 |
| Nb_references | 17 |

Le réseau affiche simultanément : **Matiere_A_kg**, **Matiere_B_kg**, **Emballage_unites**, **Energie_kWh**.

---

### Interpréter le résultat pour prendre une décision

Commandez matières A et B en tenant compte des délais fournisseur.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_production_matieres.xlsx` et sélectionnez les cibles : Matiere_A_kg, Matiere_B_kg, Emballage_unites, Energie_kWh.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
