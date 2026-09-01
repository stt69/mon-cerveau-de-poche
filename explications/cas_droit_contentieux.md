## Chapitre 43 — Détecter les dossiers à risque de contentieux

---

Certains dossiers dégénèrent en contentieux, d'autres se règlent à l'amiable. Le montant en jeu, les délais de réponse et l'historique de litiges sont des signaux.

Ce chapitre entraîne un modèle de **classification** pour repérer les dossiers à risque de contentieux.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_droit_contentieux.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_dossier | Type de dossier (1–6) | 3 |
| Montant_enjeu | Montant en jeu (€) | 100500.0 |
| Delai_reponse_client | Délai de réponse client (jours) | 15 |
| Documents_complets | Dossier complet (0/1) | 0 |
| Relances_envoyees | Relances envoyées | 2 |
| Historique_litiges | Historique de litiges (0–3) | 1 |
| **Risque_contentieux** | **Risque de contentieux (classes 0–2)** | **1** |

La colonne **Risque_contentieux** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_droit_contentieux.xlsx`. Vérifiez que **Risque_contentieux** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Risque_contentieux**. L'application bascule en mode **Classification**.

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
| Type_dossier | 3 |
| Montant_enjeu | 100500.0 |
| Delai_reponse_client | 15 |
| Documents_complets | 0 |

Le réseau renvoie une **classe prédite** pour **Risque_contentieux**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Dossiers à risque → relances renforcées, médiation anticipée, provision honoraires.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_droit_contentieux.xlsx` et choisissez **Risque_contentieux** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
