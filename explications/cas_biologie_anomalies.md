## Détecter les échantillons anormaux

---

Un échantillon anormal peut signaler une erreur de prélèvement, de stockage ou de manipulation. Le repérer tôt évite de valider un résultat faux.

Ce cas entraîne un modèle de **classification** pour détecter les échantillons anormaux.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_biologie_anomalies.xlsx`

Le fichier contient environ 500 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_echantillon | Type d'échantillon (1–5) | 3 |
| Valeur_mesuree | Valeur mesurée | 50.0 |
| Ecart_reference | Écart vs référence (%) | 0.0 |
| Temperature_stockage | Température de stockage (°C) | 13.5 |
| Delai_analyse_h | Délai avant analyse (h) | 36 |
| Operateur | Opérateur (1–8) | 4 |
| **Anomalie** | **Anomalie (classes 0–2)** | **1** |

La colonne **Anomalie** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_biologie_anomalies.xlsx`. Vérifiez que **Anomalie** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Anomalie**. L'application bascule en mode **Classification**.

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
| Type_echantillon | 3 |
| Valeur_mesuree | 50.0 |
| Ecart_reference | 0.0 |
| Temperature_stockage | 13.5 |

Le réseau renvoie une **classe prédite** pour **Anomalie**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Échantillons anormaux → recontrôle ou nouveau prélèvement avant validation.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_biologie_anomalies.xlsx` et choisissez **Anomalie** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
