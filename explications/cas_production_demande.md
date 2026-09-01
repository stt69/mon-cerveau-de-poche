## Prévoir la demande pour planifier la production

---

Produire ni trop (stock mort) ni trop peu (rupture) : anticiper la demande est le cœur de la planification industrielle. Saison, marketing et conjoncture influencent les commandes reçues.

Ce cas prédit le volume de **commandes reçues** pour les semaines à venir, afin d'ajuster production et approvisionnements.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_production_demande.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Semaine | Numéro de semaine (1–52) | 26 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Campagne_marketing | Campagne marketing (0/1) | 0 |
| Conjoncture | Conjoncture économique (1–3) | 2 |
| Prix_moyen | Prix moyen (€) | 45.0 |
| **Commandes_recues** | **Commandes reçues** | **55** |

La colonne **Commandes_recues** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_production_demande.xlsx`.

Vérifiez l'aperçu : environ 300 lignes, 6 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Commandes_recues** comme colonne cible.

Les 5 autres colonnes deviennent automatiquement les entrées.

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
| Semaine | 20 |
| Saison | 2 |
| Campagne_marketing | 1 |
| Conjoncture | 2 |
| Prix_moyen | 45 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Planifiez production et effectif sur 4 semaines à partir des prévisions hebdomadaires.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_production_demande.xlsx` et entraînez sur **Commandes_recues**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
