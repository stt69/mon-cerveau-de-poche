## Anticiper les coûts de maintenance de la flotte

---

Carburant, pneus, entretien, réparations : anticiper les coûts de flotte permet de budgétiser et de renouveler au bon moment.

Ce cas prédit **quatre postes de maintenance** (multi-sorties) par véhicule et par mois.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_transport_maintenance.xlsx`

Le fichier contient environ 250 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_vehicule | Type de véhicule (1–3) | 2 |
| Age_vehicule | Âge du véhicule (années) | 6 |
| Kilometrage_actuel | Kilométrage actuel | 152500.0 |
| Km_mois | Kilomètres / mois | 4250.0 |
| Utilisation | Type d'utilisation (1–3) | 2 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Mois_depuis_controle | Mois depuis dernier contrôle | 6 |
| **Carburant_euros** | **Carburant (€)** | **350** |
| **Pneumatiques_euros** | **Pneumatiques (€)** | **60** |
| **Entretien_euros** | **Entretien (€)** | **150** |
| **Reparations_euros** | **Réparations (€)** | **75** |

La colonne **Carburant_euros** / **Pneumatiques_euros** / **Entretien_euros** / **Reparations_euros** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_transport_maintenance.xlsx`. Vérifiez : environ 250 lignes, 11 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Carburant_euros
- Pneumatiques_euros
- Entretien_euros
- Reparations_euros

Les 7 colonnes restantes deviennent les entrées. Le réseau prédit 4 sorties **en parallèle**.

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
| Type_vehicule | 2 |
| Age_vehicule | 6 |
| Kilometrage_actuel | 152500.0 |
| Km_mois | 4250.0 |

Le réseau affiche simultanément : **Carburant_euros**, **Pneumatiques_euros**, **Entretien_euros**, **Reparations_euros**.

---

### Interpréter le résultat pour prendre une décision

Budget maintenance = somme des quatre postes prédits par véhicule.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_transport_maintenance.xlsx` et sélectionnez les cibles : Carburant_euros, Pneumatiques_euros, Entretien_euros, Reparations_euros.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
