## Chapitre 64 — Estimer le coût d'un trajet

---

Chiffrer un trajet ou une livraison en quelques secondes, c'est ce que attendent clients et dispatchers. Distance, zone, véhicule, péages et retour à vide modulent le coût réel.

Ce chapitre estime le **coût en euros** d'une prestation de transport.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_transport_cout.xlsx`

Le fichier contient environ 300 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_prestation | Type de prestation (1–5) | 3 |
| Distance_km | Distance (km) | 150.5 |
| Duree_estimee_min | Durée estimée (min) | 155 |
| Heure_depart | Tranche horaire de départ (1–5) | 3 |
| Jour_semaine | Jour de la semaine (1–7) | 4 |
| Zone | Zone géographique (1–3) | 2 |
| Poids_kg | Poids (kg) | 1000.0 |
| Vehicule | Type de véhicule (1–4) | 2 |
| Peages | Péages (0/1) | 0 |
| Retour_vide | Retour à vide (0/1) | 0 |
| **Cout_euros** | **Coût (€)** | **120** |

La colonne **Cout_euros** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `programs/excel/cas_transport_cout.xlsx`.

Vérifiez l'aperçu : environ 300 lignes, 11 colonnes, pas de cellule vide, valeurs numériques.

#### Étape 2 — Choisir la cible

Sélectionnez **Cout_euros** comme colonne cible.

Les 10 autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 300 lignes, utilisez le préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou gardez les valeurs par défaut de l'application.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**.

En mode Régression, la **régression linéaire** s'affiche d'abord (MAE, R²). Puis le réseau s'entraîne : observez la courbe MAE descendre puis se stabiliser.

#### Étape 5 — Analyser les résultats

Consultez le **tableau comparatif** et la **recommandation** (chapitre 10). Un R² réseau > 0.75 indique que le modèle capture bien les variations. Si la régression suffit, recopiez les **formules** (équation, Excel, Python).

#### Étape 6 — Prédire

Entrez les caractéristiques du cas à estimer :

| Entrée | Valeur |
|--------|--------|
| Type_prestation | 2 |
| Distance_km | 85 |
| Duree_estimee_min | 90 |
| Heure_depart | 3 |
| Jour_semaine | 2 |
| Zone | 2 |
| Poids_kg | 500 |
| Vehicule | 2 |
| Peages | 1 |
| Retour_vide | 0 |

Comparez **régression** et **réseau** (prédiction rapide) ou utilisez les colonnes `PRED_REG_...` / `PRED_NN_...` en lot. Fourchette réaliste : prédiction ± MAE du modèle retenu.

---

### Interpréter le résultat pour prendre une décision

Coût prédit ± MAE = base de devis transport.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_transport_cout.xlsx` et entraînez sur **Cout_euros**.
2. Notez le MAE et le R².
3. Prédisez un cas type (voir étape 6).
4. Modifiez une entrée clé et comparez les deux prédictions.
5. Testez un cas de votre propre historique si disponible.
