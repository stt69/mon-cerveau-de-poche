## Budget marketing par poste

**Fichier** : `synchrotech_22_budget_marketing.xlsx`
**Type** : Régression multi-sorties
**Cibles** : `Cout_photos`, `Cout_annonces`, `Cout_home_staging`, `Cout_visite_virtuelle`

## Le contexte

Répartir un budget marketing de mise en vente selon le type de bien, le segment de prix et l'exclusivité.

## Les données

| Colonne | Signification |
|---------|---------------|
| Type_bien | 0–2 |
| Prix_segment | 0 = entrée, 1 = milieu, 2 = luxe |
| Mandat_exclusif | 0/1 |
| Gamme | 0–2 |
| **Cout_*** | **Quatre postes de coût (cibles)** |

## Pas à pas

1. Sélectionnez les quatre cibles de coût
2. Comparez un bien « entrée de gamme » vs « luxe »
