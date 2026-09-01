## Détecter les zones à risque sanitaire forestier

---

Scolytes, sécheresse, densité excessive : certaines parcelles méritent une surveillance renforcée. Le réseau apprend à classer le risque sanitaire à partir de l'historique forestier.

Ce cas entraîne un modèle de **classification** sur le **risque sanitaire** des peuplements.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_forestier_sanitaire.xlsx`

Le fichier contient environ 250 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Essence | Essence forestière (1–5) | 3 |
| Age_peuplement | Âge du peuplement (années) | 70 |
| Densite | Densité du peuplement | 450 |
| Secheresse_jours | Jours de sécheresse | 30 |
| Temperature_max_ete | Température max été (°C) | 33.5 |
| Altitude_m | Altitude (m) | 900 |
| **Risque_sanitaire** | **Risque sanitaire (classes 0–2)** | **1** |

La colonne **Risque_sanitaire** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_forestier_sanitaire.xlsx`. Vérifiez que **Risque_sanitaire** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Risque_sanitaire**. L'application bascule en mode **Classification**.

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
| Essence | 3 |
| Age_peuplement | 70 |
| Densite | 450 |
| Secheresse_jours | 30 |

Le réseau renvoie une **classe prédite** pour **Risque_sanitaire**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Parcelles à risque sanitaire élevé → surveillance ou coupe sanitaire.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_forestier_sanitaire.xlsx` et choisissez **Risque_sanitaire** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
