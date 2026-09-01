## Chapitre 14 — Estimer un prix ou un coût

---

Fixer le bon prix d'un meuble sur mesure, c'est jongler entre matériaux, dimensions et finition. Votre historique de devis contient déjà la logique implicite de votre atelier.

Ce chapitre estime le **prix de vente** à partir des caractéristiques du meuble.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_pratique_prix.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_meuble | Type de meuble (1–5) | 3 |
| Bois | Essence de bois (1–4) | 2 |
| Largeur_cm | Largeur (cm) | 120 |
| Hauteur_cm | Hauteur (cm) | 135 |
| Finition | Finition (1–3) | 2 |
| Sur_mesure | Sur mesure (0/1) | 0 |
| **Prix_euros** | **Prix (€)** | **600** |

La colonne **Prix_euros** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_pratique_prix.xlsx`.

Vérifiez l'aperçu : environ 200 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Prix_euros** comme colonne cible.

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
| Type_meuble | 3 |
| Bois | 2 |
| Largeur_cm | 120 |
| Hauteur_cm | 135 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Fourchette prix = prédiction ± MAE. Argumentez le devis client avec des données.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_pratique_prix.xlsx` et entraînez sur **Prix_euros**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
