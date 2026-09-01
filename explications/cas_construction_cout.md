## Estimer le coût d'un chantier

---

Estimer le coût d'un chantier avant de signer un devis, c'est le défi de tout artisan ou entreprise du bâtiment.

Ce cas transforme votre historique de chantiers en outil d'estimation chiffrée.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_construction_cout.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_travaux | Type de travaux (1–5) | 3 |
| Surface_m2 | Surface (m²) | 260 |
| Etages | Nombre d'étages | 2 |
| Acces_chantier | Accessibilité chantier (1–3) | 2 |
| Zone | Zone géographique (1–3) | 2 |
| Materiaux_qualite | Qualité des matériaux (1–3) | 2 |
| **Cout_total_euros** | **Coût total (€)** | **55000** |

La colonne **Cout_total_euros** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_construction_cout.xlsx`.

Vérifiez l'aperçu : environ 200 lignes, 7 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Cout_total_euros** comme colonne cible.

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
| Type_travaux | 3 |
| Surface_m2 | 260 |
| Etages | 2 |
| Acces_chantier | 2 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Fourchette coût = prédiction ± MAE pour cadrer le premier rendez-vous client.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_construction_cout.xlsx` et entraînez sur **Cout_total_euros**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
