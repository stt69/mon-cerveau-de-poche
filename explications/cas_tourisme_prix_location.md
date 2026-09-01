## Chapitre 17 — Fixer le bon prix pour une location saisonnière

---

Fixer le prix d'une nuit en location saisonnière, c'est trouver le bon équilibre entre attractivité et marge. Capacité, équipements, saison et avis clients jouent tous un rôle.

Ce chapitre estime le **prix par nuit** à partir d'annonces comparables.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_tourisme_prix_location.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Capacite_personnes | Capacité (personnes) | 7 |
| Nb_chambres | Nombre de chambres | 3 |
| Distance_centre_km | Distance au centre (km) | 7.5 |
| Piscine | Piscine (0/1) | 0 |
| Note_avis | Note moyenne des avis (1–5) | 3.8 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Vue_mer | Vue mer (0/1) | 0 |
| **Prix_nuit_euros** | **Prix par nuit (€)** | **110** |

La colonne **Prix_nuit_euros** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_tourisme_prix_location.xlsx`.

Vérifiez l'aperçu : environ 300 lignes, 8 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Prix_nuit_euros** comme colonne cible.

Les 7 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 300 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** (chapitre 10). Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Capacite_personnes | 7 |
| Nb_chambres | 3 |
| Distance_centre_km | 7.5 |
| Piscine | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Comparez votre prix actuel à la prédiction pour ajuster avant la haute saison.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_tourisme_prix_location.xlsx` et entraînez sur **Prix_nuit_euros**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
