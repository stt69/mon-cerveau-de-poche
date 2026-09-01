## Chapitre 21 — Prévoir la durée des travaux

---

« Combien de temps pour ce chantier ? » Le client veut une date, vous voulez une estimation crédible. La durée dépend du type d'ouvrage, de la surface, de l'effectif, de la saison et des intempéries — des combinaisons que votre historique de chantiers terminés capture déjà.

Ce chapitre entraîne le réseau sur vos chantiers passés pour prédire la **durée en jours**. Vous obtenez une base chiffrée pour le planning et les engagements clients.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_construction_duree.xlsx`

Le fichier contient environ 180 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_ouvrage | Type d'ouvrage (1–5) | 3 |
| Surface_m2 | Surface (m²) | 260 |
| Effectif | Effectif sur chantier | 11 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Intemperies_jours | Jours d'intempéries | 7 |
| **Duree_jours** | **Durée (jours)** | **50** |

La colonne **Duree_jours** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_construction_duree.xlsx`.

Vérifiez l'aperçu : environ 180 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Duree_jours** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 180 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** (chapitre 10). Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Type_ouvrage | 2 |
| Surface_m2 | 120 |
| Effectif | 8 |
| Saison | 2 |
| Intemperies_jours | 3 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Utilisez la prédiction ± MAE pour annoncer une fourchette de délai au client. Testez l'impact d'un effectif supplémentaire en modifiant **Effectif**.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_construction_duree.xlsx` et entraînez sur **Duree_jours**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
