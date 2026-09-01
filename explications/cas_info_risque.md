## Chapitre 63 — Détecter les projets à risque de dérapage

---

Scope qui dérive, client non technique, techno inconnue : certains projets IT dérapent systématiquement. Les repérer tôt permet d'allouer un chef de projet expérimenté ou de revoir le périmètre.

Ce chapitre classifie le **risque de dérapage** (classification).

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_info_risque.xlsx`

Le fichier contient environ 250 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_projet | Type de projet (1–5) | 3 |
| Complexite | Complexité (1–5) | 3 |
| Taille_equipe | Taille de l'équipe | 5 |
| Client_technique | Client technique (0/1) | 0 |
| Cahier_charges | Cahier des charges (0/1) | 0 |
| Changements_scope | Changements de scope | 5 |
| Experience_chef | Expérience du chef de chantier (années) | 10 |
| Techno_nouvelle | Technologie nouvelle (0/1) | 0 |
| **Risque_derapage** | **Risque de dérapage (classes 0–2)** | **1** |

La colonne **Risque_derapage** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_info_risque.xlsx`. Vérifiez que **Risque_derapage** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Risque_derapage**. L'application bascule en mode **Classification**.

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
| Type_projet | 3 |
| Complexite | 3 |
| Taille_equipe | 5 |
| Client_technique | 0 |

Le réseau renvoie une **classe prédite** pour **Risque_derapage**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Projets à risque → chef expérimenté, cadrage scope, revues fréquentes.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_info_risque.xlsx` et choisissez **Risque_derapage** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
