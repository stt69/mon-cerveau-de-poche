## Chapitre 18 — Anticiper la fréquentation d'un site touristique

---

Un musée, un site touristique : la fréquentation varie selon le jour, la météo et les vacances. Anticiper les entrées et les recettes boutique aide à dimensionner l'accueil.

Ce chapitre prédit **plusieurs flux en parallèle** (entrées, boutique, cafétéria) — multi-sorties.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_tourisme_frequentation.xlsx`

Le fichier contient environ 400 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Jour_semaine | Jour de la semaine (1–7) | 4 |
| Mois | Mois (1–12) | 6 |
| Vacances | Période de vacances (0/1) | 0 |
| Meteo | Conditions météo (1–4) | 2 |
| Croisiere | Passage de croisière (0/1) | 0 |
| **Entrees** | **Nombre d'entrées** | **200** |
| **Recette_boutique** | **Recettes boutique (€)** | **600** |
| **Recette_cafeteria** | **Recettes cafétéria (€)** | **400** |

La colonne **Entrees** / **Recette_boutique** / **Recette_cafeteria** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_tourisme_frequentation.xlsx`. Vérifiez : environ 400 lignes, 8 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Entrees
- Recette_boutique
- Recette_cafeteria

Les 5 colonnes restantes deviennent les entrées. Le réseau prédit 3 sorties **en parallèle**.

#### Étape 3 — Choisir les réglages

Préréglage **Grand** (2 couches, 32 neurones, 400 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**. La régression linéaire s'affiche d'abord, puis le réseau (courbe d'erreur pour chaque sortie).

#### Étape 5 — Analyser les résultats

Consultez le tableau comparatif et la recommandation. Vérifiez MAE et R² pour chaque cible.

#### Étape 6 — Prédire

Entrez les entrées du prochain cas :

| Entrée | Valeur |
|--------|--------|
| Jour_semaine | 4 |
| Mois | 6 |
| Vacances | 0 |
| Meteo | 2 |

Le réseau affiche simultanément : **Entrees**, **Recette_boutique**, **Recette_cafeteria**.

---

### Interpréter le résultat pour prendre une décision

Planifiez l'accueil et les approvisionnements selon les trois prédictions.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_tourisme_frequentation.xlsx` et sélectionnez les cibles : Entrees, Recette_boutique, Recette_cafeteria.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
