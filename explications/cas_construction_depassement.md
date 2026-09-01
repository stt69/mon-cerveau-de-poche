## Détecter les risques de dépassement

---

Certains chantiers dépassent le budget, d'autres non. Repérer les signaux avant qu'il ne soit trop tard permet d'ajuster l'effectif, de renégocier ou d'alerter le client.

Ce cas entraîne un modèle de **classification** sur l'historique de vos dépassements. Le réseau classe chaque nouveau chantier selon son risque de dépassement.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_construction_depassement.xlsx`

Le fichier contient environ 250 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_ouvrage | Type d'ouvrage (1–5) | 3 |
| Budget_initial | Budget initial (€) | 110000.0 |
| Effectif | Effectif sur chantier | 11 |
| Meteo_risque | Risque météo (1–3) | 2 |
| Changements_plan | Changements de plan | 4 |
| Experience_chef | Expérience du chef de chantier (années) | 10 |
| **Depassement** | **Dépassement budget (classes 0–2)** | **1** |

La colonne **Depassement** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_construction_depassement.xlsx`. Vérifiez que **Depassement** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Depassement**. L'application bascule en mode **Classification**.

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
| Type_ouvrage | 3 |
| Budget_initial | 110000.0 |
| Effectif | 11 |
| Meteo_risque | 2 |

Le réseau renvoie une **classe prédite** pour **Depassement**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Un chantier classé « risque élevé » mérite un suivi budget hebdomadaire renforcé. Consultez la matrice de confusion pour voir où le modèle se trompe.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_construction_depassement.xlsx` et choisissez **Depassement** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
