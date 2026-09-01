## Chapitre 54 — Anticiper les besoins en matériel et personnel forestier

---

Machines, carburant, main-d'œuvre, rotations : préparer un chantier forestier, c'est chiffrer plusieurs postes en même temps.

Ce chapitre prédit **quatre postes de ressources** (multi-sorties) à partir du volume et du terrain.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_forestier_ressources.xlsx`

Le fichier contient environ 150 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Volume_m3 | Volume m3 | 160.0 |
| Pente_pct | Pente (%) | 30.0 |
| Distance_route_km | Distance à la route (km) | 2.5 |
| Type_coupe | Type de coupe (1–3) | 2 |
| **Heures_machine** | **Heures machine** | **30** |
| **Carburant_L** | **Carburant (L)** | **150** |
| **Main_oeuvre_jours** | **Main-d'œuvre (jours)** | **10.5** |
| **Transport_rotations** | **Rotations transport** | **7** |

La colonne **Heures_machine** / **Carburant_L** / **Main_oeuvre_jours** / **Transport_rotations** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_forestier_ressources.xlsx`. Vérifiez : environ 150 lignes, 8 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Heures_machine
- Carburant_L
- Main_oeuvre_jours
- Transport_rotations

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
| Volume_m3 | 160.0 |
| Pente_pct | 30.0 |
| Distance_route_km | 2.5 |
| Type_coupe | 2 |

Le réseau affiche simultanément : **Heures_machine**, **Carburant_L**, **Main_oeuvre_jours**, **Transport_rotations**.

---

### Interpréter le résultat pour prendre une décision

Budget chantier = somme des postes prédits (carburant, MO, machine).

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_forestier_ressources.xlsx` et sélectionnez les cibles : Heures_machine, Carburant_L, Main_oeuvre_jours, Transport_rotations.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
