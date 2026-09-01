## Prévoir le taux de réussite d'une formation

---

Avant de lancer une session, le formateur veut savoir si le public est prêt à réussir. Format, durée, taille du groupe et niveau d'entrée influencent le taux de réussite.

Ce cas prédit le **taux de réussite (%)** à partir de l'historique de vos formations.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_enseignement_reussite.xlsx`

Le fichier contient environ 100 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Format | Format de formation (1–3) | 2 |
| Duree_heures | Durée (heures) | 64 |
| Nb_participants | Nombre de participants | 17 |
| Niveau_moyen_entree | Niveau moyen à l'entrée | 8.5 |
| Formateur_experience | Expérience formateur (années) | 10 |
| **Taux_reussite_pct** | **Taux de réussite (%)** | **62.5** |

La colonne **Taux_reussite_pct** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_enseignement_reussite.xlsx`.

Vérifiez l'aperçu : environ 100 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Taux_reussite_pct** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 100 lignes, utilisez le préréglage **Petit** (1 couche, 8 neurones, 200 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** . Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Format | 2 |
| Duree_heures | 64 |
| Nb_participants | 17 |
| Niveau_moyen_entree | 8.5 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Adaptez le format ou la durée si le taux prédit est faible pour ce profil de groupe.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_enseignement_reussite.xlsx` et entraînez sur **Taux_reussite_pct**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
