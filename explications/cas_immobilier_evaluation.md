## Détecter les biens sous-évalués ou surévalués

---

Chaque semaine, des dizaines de nouvelles annonces apparaissent. Repérer les bonnes affaires ou les biens surévalués permet de prioriser les visites et de conseiller efficacement vendeurs et acheteurs.

Ce cas utilise un réseau de **classification** entraîné sur des annonces déjà jugées. Vous obtenez un filtre objectif pour scanner les nouvelles annonces.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_immobilier_evaluation.xlsx`

Le fichier contient environ 350 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Surface_m2 | Surface (m²) | 135 |
| Prix_affiche | Prix affiché (€) | 340000.0 |
| Prix_m2_quartier | Prix au m² du quartier (€/m²) | 5000.0 |
| Etat | État général (1–5) | 3 |
| Nb_pieces | Nombre de pièces | 4 |
| Etage | Étage (0=RDC ou maison) | 4 |
| **Evaluation** | **Évaluation (classes 0–2)** | **1** |

La colonne **Evaluation** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_immobilier_evaluation.xlsx`. Vérifiez que **Evaluation** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Evaluation**. L'application bascule en mode **Classification**.

#### Étape 3 — Choisir les réglages

Préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le modèle »**. Observez la **précision** monter au fil des époques.

#### Étape 5 — Analyser les résultats

Consultez la **précision** et la **matrice de confusion**. Identifiez quel type d'erreur est le plus coûteux dans votre métier (faux positifs vs faux négatifs).

#### Étape 6 — Prédire et agir

Entrez les caractéristiques d'un nouveau cas :

| Entrée | Valeur |
|--------|--------|
| Surface_m2 | 135 |
| Prix_affiche | 340000.0 |
| Prix_m2_quartier | 5000.0 |
| Etat | 3 |

Le réseau renvoie une **classe prédite** pour **Evaluation**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Les biens classés « sous-évalués » méritent une visite prioritaire ; vérifiez toujours sur place (vices, bruit, motivation du vendeur).

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_immobilier_evaluation.xlsx` et choisissez **Evaluation** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
