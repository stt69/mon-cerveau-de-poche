## Chapitre 40 — Estimer les honoraires d'un dossier

---

« Combien ça va coûter ? » Pour un dossier juridique, la réponse dépend du type d'affaire, de la complexité, de l'enjeu financier et de l'urgence.

Ce chapitre estime les **honoraires** à partir de l'historique de votre cabinet.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_droit_honoraires.xlsx`

Le fichier contient environ 250 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_dossier | Type de dossier (1–6) | 3 |
| Complexite | Complexité (1–5) | 3 |
| Enjeu_euros | Enjeu financier (€) | 250500.0 |
| Nb_parties | Nombre de parties | 5 |
| Urgence | Urgence (0/1) | 0 |
| **Honoraires_euros** | **Honoraires (€)** | **2500** |

La colonne **Honoraires_euros** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_droit_honoraires.xlsx`.

Vérifiez l'aperçu : environ 250 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Honoraires_euros** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 250 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** (chapitre 10). Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Type_dossier | 2 |
| Complexite | 3 |
| Enjeu_euros | 50000 |
| Nb_parties | 2 |
| Urgence | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Fourchette honoraires = prédiction ± MAE pour la convention d'honoraires.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_droit_honoraires.xlsx` et entraînez sur **Honoraires_euros**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
