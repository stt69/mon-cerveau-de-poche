## Détecter les patients à risque

---

Repérer tôt les patients à risque permet d'adapter le suivi et la prévention. L'âge, l'IMC, la tension, la glycémie et les habitudes de vie interagissent de façon complexe.

Ce cas entraîne un modèle de **classification** sur des dossiers anonymisés. Il ne remplace pas le jugement clinique : il aide à prioriser le suivi.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_sante_risque.xlsx`

Le fichier contient environ 500 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Age | Âge du patient | 54 |
| IMC | Indice de masse corporelle | 29.0 |
| Tension_sys | Tension systolique (mmHg) | 135 |
| Glycemie | Glycémie (g/L) | 1.6 |
| Fumeur | Fumeur (0/1) | 0 |
| Activite_physique | Activité physique (0–3) | 1 |
| **Risque** | **Niveau de risque (classes 0–2)** | **1** |

La colonne **Risque** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_sante_risque.xlsx`. Vérifiez que **Risque** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Risque**. L'application bascule en mode **Classification**.

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
| Age | 54 |
| IMC | 29.0 |
| Tension_sys | 135 |
| Glycemie | 1.6 |

Le réseau renvoie une **classe prédite** pour **Risque**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Priorisez le suivi préventif pour les patients classés à risque élevé — toujours avec validation clinique.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_sante_risque.xlsx` et choisissez **Risque** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
