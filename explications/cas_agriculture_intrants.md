## Anticiper les besoins en intrants

---

Semences, engrais, eau, phytos : anticiper les intrants évite les commandes urgentes et les gaspillages.

Ce cas prédit **plusieurs intrants en parallèle** (multi-sorties) selon la culture et la surface.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_agriculture_intrants.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Culture | Culture (1–6) | 3 |
| Surface_ha | Surface (ha) | 10.2 |
| Type_sol | Type de sol (1–4) | 2 |
| Analyse_azote | Azote dans le sol | 45.0 |
| **Semences_kg** | **Semences (kg)** | **40** |
| **Engrais_N_kg** | **Engrais azoté (kg)** | **70** |
| **Eau_m3** | **Eau (m³)** | **200** |
| **Phyto_L** | **Produits phytosanitaires (L)** | **5** |
| **Carburant_L** | **Carburant (L)** | **60** |

La colonne **Semences_kg** / **Engrais_N_kg** / **Eau_m3** / **Phyto_L** / **Carburant_L** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_agriculture_intrants.xlsx`. Vérifiez : environ 200 lignes, 9 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Semences_kg
- Engrais_N_kg
- Eau_m3
- Phyto_L
- Carburant_L

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
| Culture | 3 |
| Surface_ha | 10.2 |
| Type_sol | 2 |
| Analyse_azote | 45.0 |

Le réseau affiche simultanément : **Semences_kg**, **Engrais_N_kg**, **Eau_m3**, **Phyto_L**, **Carburant_L**.

---

### Interpréter le résultat pour prendre une décision

Commandes intrants alignées sur les prédictions multi-sorties.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_agriculture_intrants.xlsx` et sélectionnez les cibles : Semences_kg, Engrais_N_kg, Eau_m3, Phyto_L, Carburant_L.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
