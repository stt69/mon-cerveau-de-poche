## Prévoir le taux d'occupation d'un hébergement

---

Quel taux d'occupation pour la semaine prochaine ? Ajuster le prix ou anticiper le personnel suppose de connaître la demande à venir.

Ce cas prédit le **taux d'occupation (%)** à partir de l'historique hebdomadaire de votre hébergement.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_tourisme_occupation.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Semaine | Numéro de semaine (1–52) | 26 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Vacances_scolaires | Vacances scolaires (0/1) | 0 |
| Meteo_score | Score météo (1–5) | 3 |
| Evenement_local | Événement local (0/1) | 0 |
| Prix_nuitee | Prix de la nuitée (€) | 130.0 |
| **Taux_occupation_pct** | **Taux d'occupation (%)** | **55** |

La colonne **Taux_occupation_pct** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_tourisme_occupation.xlsx`.

Vérifiez l'aperçu : environ 300 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Taux_occupation_pct** comme colonne cible.

Les 6 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 300 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** . Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Semaine | 26 |
| Saison | 2 |
| Vacances_scolaires | 0 |
| Meteo_score | 3 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Testez différents **Prix_nuitee** pour voir l'impact sur l'occupation prédite.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_tourisme_occupation.xlsx` et entraînez sur **Taux_occupation_pct**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
