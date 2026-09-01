## Détecter les projets rentables vs déficitaires

---

Tous les projets photo ne se valent pas : certains rapportent, d'autres coûtent plus qu'ils ne rapportent. Repérer les profils rentables aide à choisir les missions.

Ce cas classifie les projets selon leur **rentabilité** (classification).

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_photo_rentabilite.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_projet | Type de projet (1–5) | 3 |
| Tarif_facture | Tarif facturé (€) | 1050.0 |
| Heures_totales | Heures totales | 16.0 |
| Deplacement_km | Déplacement (km) | 50.0 |
| Materiel_loue | Matériel loué (0/1) | 0 |
| Sous_traitance | Sous-traitance (0/1) | 0 |
| **Rentabilite** | **Rentabilité (classes 0–2)** | **1** |

La colonne **Rentabilite** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_photo_rentabilite.xlsx`. Vérifiez que **Rentabilite** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Rentabilite**. L'application bascule en mode **Classification**.

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
| Tarif_facture | 1050.0 |
| Heures_totales | 16.0 |
| Deplacement_km | 50.0 |

Le réseau renvoie une **classe prédite** pour **Rentabilite**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Projets classés non rentables → revoir tarif, durée ou refuser la mission.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_photo_rentabilite.xlsx` et choisissez **Rentabilite** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
