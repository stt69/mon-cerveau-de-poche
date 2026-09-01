## Détecter les défauts qualité

---

Un lot défectueux coûte cher : retours clients, reprise, réputation. La qualité dépend de la machine, de l'opérateur, des conditions atelier et de la matière.

Ce cas entraîne un modèle de **classification** pour signaler les lots à risque de défaut qualité.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_production_qualite.xlsx`

Le fichier contient environ 400 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Machine | Machine (1–5) | 3 |
| Operateur_experience | Expérience opérateur (années) | 8 |
| Temperature_atelier | Température atelier (°C) | 25.0 |
| Humidite_pct | Humidité (%) | 55.0 |
| Vitesse_ligne | Vitesse de ligne | 100.0 |
| Matiere_lot | Lot de matière (1–10) | 5 |
| **Qualite** | **Qualité (classes 0–2)** | **1** |

La colonne **Qualite** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_production_qualite.xlsx`. Vérifiez que **Qualite** contient un petit nombre de classes distinctes (typiquement 3).

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
| Machine | 3 |
| Operateur_experience | 8 |
| Temperature_atelier | 25.0 |
| Humidite_pct | 55.0 |

Le réseau renvoie une **classe prédite** pour **Qualite**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Lots classés « défaut probable » : contrôle renforcé ou réglage machine avant lancement.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_production_qualite.xlsx` et choisissez **Qualite** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
