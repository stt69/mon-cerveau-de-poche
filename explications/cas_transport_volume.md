## Chapitre 65 — Prévoir le volume de courses et livraisons

---

Combien de courses demain ? Les jours fériés, la météo et les grèves font varier l'activité d'un réseau de transport.

Ce chapitre prédit le **nombre de courses** pour planifier véhicules et chauffeurs.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_transport_volume.xlsx`

Le fichier contient environ 500 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Jour_semaine | Jour de la semaine (1–7) | 4 |
| Mois | Mois (1–12) | 6 |
| Jour_ferie | Jour férié (0/1) | 0 |
| Vacances | Période de vacances (0/1) | 0 |
| Meteo | Conditions météo (1–4) | 2 |
| Evenement_local | Événement local (0/1) | 1 |
| Greve_transports | Grève transports (0/1) | 0 |
| Temperature_C | Température (°C) | 16.5 |
| **Nb_courses** | **Nombre de courses** | **40** |

La colonne **Nb_courses** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_transport_volume.xlsx`.

Vérifiez l'aperçu : environ 500 lignes, 9 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Nb_courses** comme colonne cible.

Les 8 autres colonnes deviennent automatiquement les entrées.

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
| Jour_ferie | 0 |
| Vacances | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Planifiez véhicules et chauffeurs selon le volume de courses prédit.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_transport_volume.xlsx` et entraînez sur **Nb_courses**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
