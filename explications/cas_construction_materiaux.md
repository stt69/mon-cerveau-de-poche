## Chapitre 22 — Anticiper les besoins en matériaux

---

Avant de commander béton, acier et bois, il faut estimer les quantités. Le métré détaillé reste indispensable, mais un premier chiffrage rapide à partir du type d'ouvrage et de la surface fait gagner du temps.

Ce chapitre utilise un modèle **multi-sorties** : le réseau prédit plusieurs matériaux en une seule passe, à partir de l'historique de vos chantiers.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_construction_materiaux.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_ouvrage | Type d'ouvrage (1–5) | 3 |
| Surface_m2 | Surface (m²) | 260 |
| Etages | Nombre d'étages | 2 |
| Fondations | Type de fondations (1–3) | 2 |
| **Beton_m3** | **Béton (m³)** | **25** |
| **Acier_kg** | **Acier (kg)** | **600** |
| **Bois_m3** | **Bois (m³)** | **9.5** |
| **Isolation_m2** | **Isolation (m²)** | **60** |
| **Tuiles_m2** | **Tuiles (m²)** | **55** |

La colonne **Beton_m3** / **Acier_kg** / **Bois_m3** / **Isolation_m2** / **Tuiles_m2** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_construction_materiaux.xlsx`. Vérifiez : environ 200 lignes, 9 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Beton_m3
- Acier_kg
- Bois_m3
- Isolation_m2
- Tuiles_m2

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
| Type_ouvrage | 3 |
| Surface_m2 | 260 |
| Etages | 2 |
| Fondations | 2 |

Le réseau affiche simultanément : **Beton_m3**, **Acier_kg**, **Bois_m3**, **Isolation_m2**, **Tuiles_m2**.

---

### Interpréter le résultat pour prendre une décision

Comparez les quantités prédites avec votre métré habituel. Le réseau accélère la préparation des commandes fournisseurs.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_construction_materiaux.xlsx` et sélectionnez les cibles : Beton_m3, Acier_kg, Bois_m3, Isolation_m2, Tuiles_m2.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
