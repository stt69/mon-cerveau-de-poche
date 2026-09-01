## Chapitre 12 — Prévoir les ventes du mois prochain

---

Premier cas pratique. Premier vrai test avec vos propres résultats.

Ce chapitre est le modèle que suivront tous les chapitres de la Partie III. Une fois cette méthode maîtrisée, vous pourrez l'appliquer à n'importe quel domaine.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_pratique_ventes.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Mois | Mois (1–12) | 6 |
| Temperature_moy_C | Température moyenne (°C) | 16.5 |
| Jours_ouvres | Jours ouvrés dans la période | 20 |
| Promotion | Promotion en cours (0/1) | 0 |
| Vacances_scolaires | Vacances scolaires (0/1) | 0 |
| Evenement_local | Événement local (0/1) | 0 |
| **Ventes_euros** | **Chiffre d'affaires (€)** | **8000** |

La colonne **Ventes_euros** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_pratique_ventes.xlsx`.

Vérifiez l'aperçu : environ 200 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Ventes_euros** comme colonne cible.

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
| Mois | 6 |
| Temperature_moy_C | 16.5 |
| Jours_ouvres | 20 |
| Promotion | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Utilisez la prédiction ± MAE pour fixer l'objectif commercial du mois. Testez l'impact d'une promotion en passant **Promotion** à 1.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_pratique_ventes.xlsx` et entraînez sur **Ventes_euros**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
