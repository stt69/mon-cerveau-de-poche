## Chapitre 28 — Estimer la durée d'un traitement

---

« Combien de temps pour ce traitement ? » Les patients posent la question ; les équipes médicales aussi pour organiser les lits et les rendez-vous. La durée varie selon l'âge, la pathologie, la sévérité et le protocole.

Ce chapitre entraîne le réseau sur des dossiers anonymisés pour estimer la **durée de traitement en jours**. Les données doivent rester anonymisées et conformes à la réglementation.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_sante_duree_traitement.xlsx`

Le fichier contient environ 400 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Age | Âge du patient | 54 |
| Pathologie | Type de pathologie (1–6) | 3 |
| Severite | Sévérité (1–5) | 3 |
| Antecedents | Antécédents (0–3) | 1 |
| Traitement | Type de traitement (1–4) | 2 |
| Sport_regulier | Sport régulier (0/1) | 0 |
| **Duree_jours** | **Durée (jours)** | **35** |

La colonne **Duree_jours** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_sante_duree_traitement.xlsx`.

Vérifiez l'aperçu : environ 400 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Duree_jours** comme colonne cible.

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
| Age | 55 |
| Pathologie | 3 |
| Severite | 2 |
| Antecedents | 1 |
| Traitement | 2 |
| Sport_regulier | 1 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

La durée prédite aide à planifier les lits et les rendez-vous de contrôle. Ne remplace pas l'avis médical individualisé.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_sante_duree_traitement.xlsx` et entraînez sur **Duree_jours**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
