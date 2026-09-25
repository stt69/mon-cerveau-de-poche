## Estimer le loyer mensuel

**Fichier** : `synchrotech_13_loyer_mensuel.xlsx`
**Type** : Régression
**Cible** : `Loyer_mensuel_CHF`

## Le contexte

Fixer un loyer demandé cohérent pour un objet en location : surface, pièces, meublé, quartier, parking, charges incluses.

## Les données

| Colonne | Signification |
|---------|---------------|
| Surface_m2 | Surface |
| Pieces | Nombre de pièces |
| Meuble | 0/1 |
| Quartier_note | Note 1–5 |
| Parking | 0/1 |
| Charges_incluses | 0/1 |
| **Loyer_mensuel_CHF** | **Loyer mensuel (cible)** |

## Pas à pas

1. Entraînez sur `Loyer_mensuel_CHF`
2. Prédisez pour un 3,5 pièces non meublé, quartier note 4, parking, charges séparées
