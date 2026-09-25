## Répartition d'un budget de rénovation

**Fichier** : `synchrotech_29_budget_renovation_postes.xlsx`
**Type** : Régression multi-sorties
**Cibles** : `Part_cuisine`, `Part_sdb`, `Part_toiture`, `Part_facade`

## Le contexte

Répartir un budget total de rénovation entre postes (cuisine, salles de bain, toiture, façade) selon la priorité et le type de bien.

## Les données

| Colonne | Signification |
|---------|---------------|
| Budget_total_CHF | Budget total |
| Surface_m2 | Surface |
| Priorite | 0–2 |
| Type_bien | 0/1 |
| **Part_*** | **Quatre montants (cibles)** |

## Pas à pas

1. Sélectionnez les quatre cibles `Part_*`
2. Vérifiez que la somme des prédictions reste proche du budget
