## Chapitre 59 — Détecter les parcelles à risque de maladie

---

Humidité, température, rotation et traitements préventifs influencent le risque de maladie des cultures. Repérer les parcelles à risque permet d'intervenir avant les dégâts.

Ce chapitre classifie le **risque de maladie** par parcelle (classification).

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_agriculture_maladie.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Culture | Culture (1–6) | 3 |
| Humidite_pct | Humidité (%) | 62.5 |
| Temperature_moy | Température moyenne (°C) | 20.0 |
| Rotation_respect | Rotation respectée (0/1) | 0 |
| Traitement_preventif | Traitement préventif (0/1) | 0 |
| Densite_semis | Densité de semis (1–3) | 2 |
| **Risque_maladie** | **Risque maladie (classes 0–2)** | **1** |

La colonne **Risque_maladie** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_agriculture_maladie.xlsx`. Vérifiez que **Risque_maladie** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Risque_maladie**. L'application bascule en mode **Classification**.

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
| Culture | 3 |
| Humidite_pct | 62.5 |
| Temperature_moy | 20.0 |
| Rotation_respect | 0 |

Le réseau renvoie une **classe prédite** pour **Risque_maladie**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Parcelles à risque → traitement préventif ou inspection renforcée.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_agriculture_maladie.xlsx` et choisissez **Risque_maladie** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
