## Chapitre 19 — Prévoir les besoins en personnel saisonnier

---

Combien de couverts prévoir samedi soir ? Sous-estimer, c'est des clients mécontents ; sur-estimer, c'est du gaspillage et du surcoût.

Ce chapitre prédit le **nombre de couverts** pour planifier le personnel en restauration touristique.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_tourisme_personnel.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Jour_semaine | Jour de la semaine (1–7) | 4 |
| Mois | Mois (1–12) | 6 |
| Reservations | Nombre de réservations | 85 |
| Evenement | Événement spécial (0/1) | 0 |
| Groupe | Groupe prévu (0/1) | 0 |
| **Nb_couverts** | **Nombre de couverts** | **80** |

La colonne **Nb_couverts** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_tourisme_personnel.xlsx`.

Vérifiez l'aperçu : environ 300 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Nb_couverts** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

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
| Jour_semaine | 4 |
| Mois | 6 |
| Reservations | 85 |
| Evenement | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Convertissez les couverts prédits en shifts de personnel (cuisine + salle).

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_tourisme_personnel.xlsx` et entraînez sur **Nb_couverts**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
