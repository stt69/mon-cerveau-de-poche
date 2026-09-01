## Chapitre 39 — Détecter le risque de décrochage

---

Un élève qui décroche laisse souvent des signaux avant la rupture : absentéisme, notes en baisse, retards. Les repérer tôt permet d'intervenir.

Ce chapitre entraîne un modèle de **classification** pour estimer le risque de décrochage. Données anonymisées ; l'objectif est l'accompagnement, jamais la stigmatisation.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_enseignement_decrochage.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Assiduite_pct | Assiduité (%) | 65.0 |
| Notes_moyennes | Notes moyennes | 10.0 |
| Retards_par_mois | Retards par mois | 10 |
| Participation | Participation (1–5) | 3 |
| Distance_domicile_km | Distance domicile–établissement (km) | 15.2 |
| Boursier | Boursier (0/1) | 0 |
| **Risque_decrochage** | **Risque de décrochage (classes 0–2)** | **1** |

La colonne **Risque_decrochage** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_enseignement_decrochage.xlsx`. Vérifiez que **Risque_decrochage** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Risque_decrochage**. L'application bascule en mode **Classification**.

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
| Assiduite_pct | 65.0 |
| Notes_moyennes | 10.0 |
| Retards_par_mois | 10 |
| Participation | 3 |

Le réseau renvoie une **classe prédite** pour **Risque_decrochage**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Risque élevé → plan d'accompagnement (tuteur, entretien, aménagement horaire).

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_enseignement_decrochage.xlsx` et choisissez **Risque_decrochage** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
