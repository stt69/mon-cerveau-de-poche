## Anticiper l'approvisionnement d'un service

---

Viande, poisson, légumes, fromages, vins : pour un service gastronomique, tout se commande en parallèle. Anticiper les quantités évite ruptures et surstock.

Ce cas prédit **cinq approvisionnements en parallèle** (multi-sorties) pour le service à venir.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_gastronomie_approvisionnement.xlsx`

Environ 200 services passés.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Jour_semaine | Jour (1–7) | 6 |
| Saison | Saison (1–4) | 2 |
| Couverts_prevus | Couverts prévus | 65 |
| Formule_menu | Formule (1=déjeuner … 3=dégustation) | 3 |
| Evenement | Événement (0/1) | 0 |
| Meteo | Météo (1–4) | 2 |
| Degustation_vins | Dégustation vins (0/1) | 1 |
| **Viande_kg** | **Viande (kg)** | **14.5** |
| **Poisson_kg** | **Poisson (kg)** | **9.2** |
| **Legumes_kg** | **Légumes (kg)** | **22.0** |
| **Fromages_pieces** | **Fromages (pièces)** | **28** |
| **Vins_bouteilles** | **Vins (bouteilles)** | **42** |

Les colonnes **Viande_kg**, **Poisson_kg**, **Legumes_kg**, **Fromages_pieces**, **Vins_bouteilles** sont les cibles.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `cas_gastronomie_approvisionnement.xlsx`.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Viande_kg
- Poisson_kg
- Legumes_kg
- Fromages_pieces
- Vins_bouteilles

Les 7 colonnes restantes deviennent les entrées.

#### Étape 3 — Entraîner

Préréglage **Petit** ou **Moyen**. Le réseau prédit 5 sorties **en parallèle**.

#### Étape 4 — Prédire

| Entrée | Valeur |
|--------|--------|
| Jour_semaine | 6 |
| Saison | 2 |
| Couverts_prevus | 65 |
| Formule_menu | 3 |
| Degustation_vins | 1 |

Le réseau affiche simultanément : **Viande_kg**, **Poisson_kg**, **Legumes_kg**, **Fromages_pieces**, **Vins_bouteilles**.

---

### Interpréter le résultat

Bon de commande unique pour le chef et le sommelier : quantités cohérentes pour 65 couverts en formule dégustation.

> **Key takeaway** : une seule prédiction, cinq commandes — le réseau capture les corrélations entre postes.

---

### Exercice

1. Chargez le fichier et sélectionnez les 5 cibles.
2. Entraînez et notez le MAE pour chaque sortie.
3. Prédisez pour un samedi soir, 70 couverts, dégustation vins.
4. Modifiez `Couverts_prevus` et observez l'impact sur toutes les sorties.
