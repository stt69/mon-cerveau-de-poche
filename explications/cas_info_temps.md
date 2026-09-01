## Chapitre 60 — Estimer le temps de développement

---

« Combien de jours pour livrer cette fonctionnalité ? » Les estimations IT sont notoriously optimistes. Un modèle entraîné sur vos projets passés donne une base plus réaliste.

Ce chapitre prédit la **durée de développement en jours**.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_info_temps.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_projet | Type de projet (1–5) | 3 |
| Nb_fonctionnalites | Nombre de fonctionnalités | 26 |
| Complexite | Complexité (1–5) | 3 |
| Client_technique | Client technique (0/1) | 0 |
| Equipe | Taille de l'équipe | 4 |
| Techno_nouvelle | Technologie nouvelle (0/1) | 0 |
| **Duree_jours** | **Durée (jours)** | **40** |

La colonne **Duree_jours** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_info_temps.xlsx`.

Vérifiez l'aperçu : environ 200 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Duree_jours** comme colonne cible.

Les 6 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 200 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** (chapitre 10). Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Type_projet | 2 |
| Nb_fonctionnalites | 15 |
| Complexite | 3 |
| Client_technique | 1 |
| Equipe | 4 |
| Techno_nouvelle | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Estimation ± MAE pour le planning sprint et la promesse client.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_info_temps.xlsx` et entraînez sur **Duree_jours**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
