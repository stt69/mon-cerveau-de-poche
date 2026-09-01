## Détecter ce qui ne va pas (classification)

---

Jusqu'ici, le réseau prédisait des **chiffres**. Ici, il prédit une **catégorie** : le client sera-t-il satisfait ou mécontent ?

C'est la **classification** — aussi naturelle que la régression dans *Mon Cerveau de Poche*.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_pratique_satisfaction.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Delai_livraison_jours | Délai de livraison (jours) | 8 |
| Prix_paye_euros | Prix payé (€) | 255.0 |
| Qualite_produit | Qualité perçue (1–5) | 3 |
| Service_client | Service client (1–5) | 3 |
| Premiere_commande | Premier achat (0/1) | 0 |
| Retour_effectue | Retour effectué (0/1) | 0 |
| **Satisfaction** | **Satisfaction (classes 0–2)** | **1** |

La colonne **Satisfaction** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_pratique_satisfaction.xlsx`. Vérifiez que **Satisfaction** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Satisfaction**. L'application bascule en mode **Classification**.

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
| Delai_livraison_jours | 8 |
| Prix_paye_euros | 255.0 |
| Qualite_produit | 3 |
| Service_client | 3 |

Le réseau renvoie une **classe prédite** pour **Satisfaction**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

### Lire les résultats d'une classification

En classification, la métrique principale est la **précision** : sur 100 exemples, combien de classes correctes ? Consultez aussi la **matrice de confusion** — elle montre où le réseau se trompe (faux positifs vs faux négatifs). Demandez-vous quel type d'erreur est le plus coûteux dans votre métier avant d'agir sur la prédiction.

---
---

### Interpréter le résultat pour prendre une décision

Une prédiction « mécontent » déclenche une action préventive (suivi livraison, geste commercial).

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_pratique_satisfaction.xlsx` et choisissez **Satisfaction** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
