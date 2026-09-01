## Anticiper les ressources humaines IT

---

Combien de développeurs, d'ops et de support mobiliser ce mois-ci ? Projets actifs, tickets et déploiements prévus orientent la charge.

Ce cas prédit **plusieurs postes en heures** (multi-sorties) pour la planification RH IT.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_info_rh.xlsx`

Le fichier contient environ 150 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Mois | Mois (1–12) | 6 |
| Projets_actifs | Projets actifs | 9 |
| Tickets_support | Tickets support | 55 |
| Deploiements_prevus | Déploiements prévus | 2 |
| **Dev_heures** | **Heures développement** | **350** |
| **Ops_heures** | **Heures ops** | **155** |
| **Support_heures** | **Heures support** | **110** |
| **Management_heures** | **Heures management** | **70** |

La colonne **Dev_heures** / **Ops_heures** / **Support_heures** / **Management_heures** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_info_rh.xlsx`. Vérifiez : environ 150 lignes, 8 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Dev_heures
- Ops_heures
- Support_heures
- Management_heures

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
| Projets_actifs | 9 |
| Tickets_support | 55 |
| Deploiements_prevus | 2 |

Le réseau affiche simultanément : **Dev_heures**, **Ops_heures**, **Support_heures**, **Management_heures**.

---

### Interpréter le résultat pour prendre une décision

Affectez équipes dev/ops/support selon les heures prédites.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_info_rh.xlsx` et sélectionnez les cibles : Dev_heures, Ops_heures, Support_heures, Management_heures.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
