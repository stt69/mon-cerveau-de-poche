## Chapitre 29 — Prévoir la fréquentation d'un cabinet

---

Anticiper le nombre de consultations permet d'ajuster les plannings, les remplacements et les créneaux d'urgence. La fréquentation d'un cabinet varie selon le jour, la saison, la météo et les épidémies.

Ce chapitre transforme l'historique de fréquentation en outil de prévision pour les semaines à venir.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_sante_frequentation.xlsx`

Le fichier contient environ 500 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Jour_semaine | Jour de la semaine (1–7) | 4 |
| Mois | Mois (1–12) | 6 |
| Vacances | Période de vacances (0/1) | 0 |
| Epidemie | Épidémie en cours (0/1) | 0 |
| Meteo | Conditions météo (1–4) | 2 |
| Temperature | Température (°C) | 15.0 |
| **Nb_consultations** | **Nombre de consultations** | **25** |

La colonne **Nb_consultations** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_sante_frequentation.xlsx`.

Vérifiez l'aperçu : environ 500 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Nb_consultations** comme colonne cible.

Les 6 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 500 lignes, utilisez le préréglage **Grand** (2 couches, 32 neurones, 400 époques) ou gardez les valeurs par défaut de l'application.

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
| Vacances | 0 |
| Epidemie | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Ajustez les plannings des praticiens et les créneaux d'urgence selon la fréquentation prédite.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_sante_frequentation.xlsx` et entraînez sur **Nb_consultations**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
