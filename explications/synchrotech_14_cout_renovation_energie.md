## Coût d'une rénovation énergétique

**Fichier** : `synchrotech_14_cout_renovation_energie.xlsx`
**Type** : Régression
**Cible** : `Cout_renovation_CHF`

## Le contexte

Estimer le budget d'une rénovation énergétique (isolation, chauffage, fenêtres) avant de conseiller un propriétaire ou une PPE.

## Les données

| Colonne | Signification |
|---------|---------------|
| Surface_m2 | Surface |
| Annee_construction | Année |
| Isolation_actuelle | 0–2 |
| Type_travaux | 0 = isolation, 1 = chauffage, 2 = complet |
| Nb_fenetres | Nombre de fenêtres |
| Chauffage_remplace | 0/1 |
| **Cout_renovation_CHF** | **Coût travaux (cible)** |

## Pas à pas

1. Cible = `Cout_renovation_CHF`
2. Comparez un scénario « isolation seule » vs « complet »
