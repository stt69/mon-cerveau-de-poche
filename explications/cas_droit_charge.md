## Anticiper la charge du cabinet

---

Répartir la charge entre contentieux, conseil et fiscal en fin de mois, c'est un puzzle récurrent. Le nombre de dossiers ouverts et les audiences prévues donnent des indices.

Ce cas prédit **plusieurs pôles d'activité en heures** (multi-sorties) pour anticiper la charge du cabinet.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_droit_charge.xlsx`

Le fichier contient environ 150 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Mois | Mois (1–12) | 6 |
| Dossiers_ouverts | Dossiers ouverts | 50 |
| Audiences_prevues | Audiences prévues | 11 |
| Fiscalite_saison | Saison fiscale (0/1) | 0 |
| **Heures_civil** | **Heures civil** | **130** |
| **Heures_penal** | **Heures pénal** | **70** |
| **Heures_fiscal** | **Heures fiscal** | **65** |
| **Heures_admin** | **Heures administratif** | **75** |

La colonne **Heures_civil** / **Heures_penal** / **Heures_fiscal** / **Heures_admin** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_droit_charge.xlsx`. Vérifiez : environ 150 lignes, 8 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Heures_civil
- Heures_penal
- Heures_fiscal
- Heures_admin

Les 4 colonnes restantes deviennent les entrées. Le réseau prédit 4 sorties **en parallèle**.

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
| Dossiers_ouverts | 50 |
| Audiences_prevues | 11 |
| Fiscalite_saison | 0 |

Le réseau affiche simultanément : **Heures_civil**, **Heures_penal**, **Heures_fiscal**, **Heures_admin**.

---

### Interpréter le résultat pour prendre une décision

Répartissez les affectations internes selon les heures prédites par pôle.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_droit_charge.xlsx` et sélectionnez les cibles : Heures_civil, Heures_penal, Heures_fiscal, Heures_admin.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
