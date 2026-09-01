## Anticiper les besoins en consommables

---

Rupture de gants ou surstock de médicaments : les deux coûtent cher. Anticiper la consommation de consommables à partir de l'activité prévue évite les commandes de dernière minute.

Ce cas prédit **plusieurs catégories de consommables en même temps** (multi-sorties) à partir du volume d'activité du cabinet ou de l'établissement.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_sante_consommables.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Mois | Mois (1–12) | 6 |
| Nb_consultations | Nombre de consultations | 400 |
| Nb_chirurgies | Nombre de chirurgies | 22 |
| Saison_grippe | Saison grippale (0/1) | 0 |
| **Gants_boites** | **Gants (boîtes)** | **35** |
| **Compresses_boites** | **Compresses (boîtes)** | **25** |
| **Desinfectant_L** | **Désinfectant (L)** | **17.5** |
| **Seringues_boites** | **Seringues (boîtes)** | **14** |
| **Medicaments_lots** | **Médicaments (lots)** | **50** |

La colonne **Gants_boites** / **Compresses_boites** / **Desinfectant_L** / **Seringues_boites** / **Medicaments_lots** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_sante_consommables.xlsx`. Vérifiez : environ 200 lignes, 9 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Gants_boites
- Compresses_boites
- Desinfectant_L
- Seringues_boites
- Medicaments_lots

Les 4 colonnes restantes deviennent les entrées. Le réseau prédit 5 sorties **en parallèle**.

#### Étape 3 — Choisir les réglages

Préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**. La régression linéaire s'affiche d'abord, puis le réseau (courbe d'erreur pour chaque sortie).

#### Étape 5 — Analyser les résultats

Consultez le tableau comparatif et la recommandation. Vérifiez MAE et R² pour chaque cible.

#### Étape 6 — Prédire

Entrez les entrées du prochain cas :

| Entrée | Valeur |
|--------|--------|
| Mois | 6 |
| Nb_consultations | 400 |
| Nb_chirurgies | 22 |
| Saison_grippe | 0 |

Le réseau affiche simultanément : **Gants_boites**, **Compresses_boites**, **Desinfectant_L**, **Seringues_boites**, **Medicaments_lots**.

---

### Interpréter le résultat pour prendre une décision

Passez commande fournisseur dès que les prédictions dépassent le stock de sécurité.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_sante_consommables.xlsx` et sélectionnez les cibles : Gants_boites, Compresses_boites, Desinfectant_L, Seringues_boites, Medicaments_lots.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
