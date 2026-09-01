## Chapitre 45 — Prévoir les commandes par saison

---

La saison des mariages, le budget pub et la réputation en ligne font varier le carnet de commandes d'un photographe. Anticiper permet d'ajuster la communication et la disponibilité.

Ce chapitre prédit le **nombre de commandes** mois par mois.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_photo_commandes.xlsx`

Le fichier contient environ 150 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Mois | Mois (1–12) | 6 |
| Saison_mariages | Saison mariages (0/1) | 0 |
| Budget_pub_euros | Budget publicité (€) | 250.0 |
| Nb_avis_positifs | Avis positifs | 105 |
| Concurrent_promo | Promotion concurrent (0/1) | 0 |
| **Nb_commandes** | **Nombre de commandes** | **9** |

La colonne **Nb_commandes** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_photo_commandes.xlsx`.

Vérifiez l'aperçu : environ 150 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Nb_commandes** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 150 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** (chapitre 10). Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Mois | 6 |
| Saison_mariages | 0 |
| Budget_pub_euros | 250.0 |
| Nb_avis_positifs | 105 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Renforcez la pub avant les mois à commandes prédites faibles.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_photo_commandes.xlsx` et entraînez sur **Nb_commandes**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
