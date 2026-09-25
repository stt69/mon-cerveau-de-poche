## Commission d'agence

**Fichier** : `synchrotech_15_commission_agence.xlsx`
**Type** : Régression
**Cible** : `Commission_CHF`

## Le contexte

Anticiper la commission selon le prix de transaction, le type de mandat (vente / location) et l'exclusivité.

## Les données

| Colonne | Signification |
|---------|---------------|
| Prix_transaction_CHF | Prix de la transaction |
| Type_mandat | 0 = vente, 1 = location |
| Exclusive | 0/1 |
| **Commission_CHF** | **Commission (cible)** |

## Pas à pas

1. Entraînez ; vérifiez que la MAE reste proportionnelle aux montants
2. Testez vente exclusive vs non exclusive à prix égal
