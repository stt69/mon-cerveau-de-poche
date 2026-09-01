## Chapitre 71 — Détecter les lots à risque de défaut d'affinage

---

Une meule qui part en défaut à l'affinage, c'est des semaines de travail perdues. Les paramètres de fabrication et de cave laissent parfois présager le résultat final.

Ce chapitre classifie la **qualité d'affinage** (classification) pour prioriser les contrôles.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_fromagerie_affinage.xlsx`

Le fichier contient environ 500 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_fromage | Type de fromage (1–5) | 3 |
| Saison_fabrication | Saison de fabrication (1–4) | 2 |
| MG_gL | Matière grasse (g/L) | 39.0 |
| Proteines_gL | Protéines (g/L) | 33.0 |
| Acidite_Dornic | Acidité Dornic | 17.0 |
| Cellules_somatiques | Cellules somatiques | 275 |
| Temperature_chauffage_C | Température de chauffage (°C) | 53.0 |
| Duree_brassage_min | Durée de brassage (min) | 45 |
| pH_demoulage | pH au démoulage | 5.4 |
| Temperature_cave_C | Température de cave (°C) | 13.0 |
| Humidite_cave_pct | Humidité cave (%) | 91.5 |
| Duree_affinage_mois | Durée d'affinage (mois) | 7 |
| Frequence_frottage | Fréquence de frottage | 4 |
| Retournements | Nombre de retournements | 35 |
| **Qualite** | **Qualité (classes 0–2)** | **1** |

La colonne **Qualite** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_fromagerie_affinage.xlsx`. Vérifiez que **Qualite** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Qualite**. L'application bascule en mode **Classification**.

#### Étape 3 — Choisir les réglages

Préréglage **Grand** (2 couches, 32 neurones, 400 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le modèle »**. Observez la **précision** monter au fil des époques.

#### Étape 5 — Analyser les résultats

Consultez la **précision** et la **matrice de confusion**. Identifiez quel type d'erreur est le plus coûteux dans votre métier (faux positifs vs faux négatifs).

#### Étape 6 — Prédire et agir

Entrez les caractéristiques d'un nouveau cas :

| Entrée | Valeur |
|--------|--------|
| Type_fromage | 3 |
| Saison_fabrication | 2 |
| MG_gL | 39.0 |
| Proteines_gL | 33.0 |

Le réseau renvoie une **classe prédite** pour **Qualite**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Meules classées « défaut probable » → contrôle sensoriel et affinage renforcé.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_fromagerie_affinage.xlsx` et choisissez **Qualite** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
