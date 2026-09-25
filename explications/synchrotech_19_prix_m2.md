## Prix au mètre carré

**Fichier** : `synchrotech_19_prix_m2.xlsx`
**Type** : Régression
**Cible** : `Prix_m2_CHF`

## Le contexte

Estimer un prix au m² de référence selon canton, distance au centre, vue, année et rénovation récente.

## Les données

| Colonne | Signification |
|---------|---------------|
| Surface_m2 | Surface |
| Canton | 0–2 |
| Distance_centre_km | Distance au centre |
| Vue | 0–2 |
| Annee_construction | Année |
| Renove_recent | 0/1 |
| **Prix_m2_CHF** | **Prix au m² (cible)** |

## Pas à pas

1. Entraînez sur `Prix_m2_CHF`
2. Comparez un bien en VS vs GE à distance égale
