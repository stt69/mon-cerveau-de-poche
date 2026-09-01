## Estimer le volume de bois d'une parcelle

---

Estimer le volume de bois sur pied avant l'exploitation conditionne le devis, le matériel et la durée du chantier. Essence, âge, densité et exposition influencent le cubage.

Ce cas prédit le **volume en m³** à partir des caractéristiques de la parcelle.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_forestier_volume.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Essence | Essence forestière (1–5) | 3 |
| Age_peuplement | Âge du peuplement (années) | 70 |
| Densite_arbres_ha | Densité (arbres/ha) | 450 |
| Altitude_m | Altitude (m) | 900 |
| Exposition | Exposition (1–4) | 2 |
| Surface_ha | Surface (ha) | 5.2 |
| **Volume_m3** | **Volume (m³)** | **95** |

La colonne **Volume_m3** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_forestier_volume.xlsx`.

Vérifiez l'aperçu : environ 200 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Volume_m3** comme colonne cible.

Les 6 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 200 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** . Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Essence | 3 |
| Age_peuplement | 70 |
| Densite_arbres_ha | 450 |
| Altitude_m | 900 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Volume prédit ± MAE sert au devis d'exploitation forestière.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_forestier_volume.xlsx` et entraînez sur **Volume_m3**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
