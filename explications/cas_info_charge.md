## Chapitre 61 — Prévoir la charge serveur et infrastructure

---

Une mise à jour, une campagne marketing ou un pic d'utilisateurs peuvent saturer les serveurs. Anticiper la charge CPU permet de dimensionner l'infrastructure.

Ce chapitre prédit la **charge CPU (%)** à partir des métriques journalières.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_info_charge.xlsx`

Le fichier contient environ 400 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Jour_semaine | Jour de la semaine (1–7) | 4 |
| Heure | Heure (0–23) | 11 |
| Mois | Mois (1–12) | 6 |
| Mise_a_jour_recente | Mise à jour récente (0/1) | 0 |
| Campagne_marketing | Campagne marketing (0/1) | 0 |
| Nb_utilisateurs_base | Base utilisateurs | 2550 |
| **CPU_pct** | **Charge CPU (%)** | **40** |

La colonne **CPU_pct** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_info_charge.xlsx`.

Vérifiez l'aperçu : environ 400 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **CPU_pct** comme colonne cible.

Les 6 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 400 lignes, utilisez le préréglage **Grand** (2 couches, 32 neurones, 400 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** (chapitre 10). Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Jour_semaine | 4 |
| Heure | 11 |
| Mois | 6 |
| Mise_a_jour_recente | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Charge CPU prédite > seuil → scale-up ou report de déploiement.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_info_charge.xlsx` et entraînez sur **CPU_pct**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
