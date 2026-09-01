## Chapitre 50 — Anticiper les besoins en réactifs

---

Commander les réactifs au bon moment évite les ruptures en pleine série d'analyses. Le volume d'analyses prévues et le type dominant déterminent la consommation.

Ce chapitre prédit **plusieurs réactifs et consommables** (multi-sorties) pour le mois à venir.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_biologie_reactifs.xlsx`

Le fichier contient environ 150 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Mois | Mois (1–12) | 6 |
| Nb_analyses_prevues | Analyses prévues | 275 |
| Type_analyses_dominant | Type d'analyses dominant (1–4) | 2 |
| Projets_recherche | Projets de recherche (1–5) | 3 |
| **Reactif_A_mL** | **Réactif A (mL)** | **250** |
| **Reactif_B_mL** | **Réactif B (mL)** | **150** |
| **Milieux_culture** | **Milieux de culture** | **60** |
| **Pipettes_boites** | **Pipettes (boîtes)** | **12.5** |
| **Gants_boites** | **Gants (boîtes)** | **22.5** |

La colonne **Reactif_A_mL** / **Reactif_B_mL** / **Milieux_culture** / **Pipettes_boites** / **Gants_boites** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_biologie_reactifs.xlsx`. Vérifiez : environ 150 lignes, 9 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Reactif_A_mL
- Reactif_B_mL
- Milieux_culture
- Pipettes_boites
- Gants_boites

Les 4 colonnes restantes deviennent les entrées. Le réseau prédit 5 sorties **en parallèle**.

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
| Nb_analyses_prevues | 275 |
| Type_analyses_dominant | 2 |
| Projets_recherche | 3 |

Le réseau affiche simultanément : **Reactif_A_mL**, **Reactif_B_mL**, **Milieux_culture**, **Pipettes_boites**, **Gants_boites**.

---

### Interpréter le résultat pour prendre une décision

Commandez réactifs avant le seuil de stock critique.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_biologie_reactifs.xlsx` et sélectionnez les cibles : Reactif_A_mL, Reactif_B_mL, Milieux_culture, Pipettes_boites, Gants_boites.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
