## Chapitre 44 — Estimer le prix d'une prestation photo

---

Fixer un tarif photo juste — ni trop bas (on se sous-vend), ni trop haut (on perd le client) — requiert de tenir compte du type de prestation, de la durée, du retouche et du déplacement.

Ce chapitre estime le **tarif** à partir de l'historique de vos prestations.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_photo_tarif.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_prestation | Type de prestation (1–5) | 3 |
| Duree_heures | Durée (heures) | 6.5 |
| Nb_photos_retouchees | Photos retouchées | 105 |
| Deplacement_km | Déplacement (km) | 50.0 |
| Urgence | Urgence (0/1) | 0 |
| Experience_photographe | Expérience photographe (années) | 10 |
| **Tarif_euros** | **Tarif (€)** | **400** |

La colonne **Tarif_euros** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_photo_tarif.xlsx`.

Vérifiez l'aperçu : environ 200 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Tarif_euros** comme colonne cible.

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
| Type_prestation | 3 |
| Duree_heures | 6.5 |
| Nb_photos_retouchees | 105 |
| Deplacement_km | 50.0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Tarif prédit ± MAE = fourchette commerciale crédible.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_photo_tarif.xlsx` et entraînez sur **Tarif_euros**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
