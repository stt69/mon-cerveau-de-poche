## Risque de vacance locative

**Fichier** : `synchrotech_18_risque_vacance.xlsx`
**Type** : Classification
**Cible** : `Vacance_longue` (0/1)

## Le contexte

Anticiper une vacance prolongée pour prioriser les actions (ajustement de loyer, travaux, marketing).

## Les données

| Colonne | Signification |
|---------|---------------|
| Loyer_vs_marche_pct | Écart de loyer vs marché |
| Etat_logement | 0–2 |
| DPE | 0–3 |
| Etage | Étage |
| Bruit | 0/1 |
| Derniere_relocation_mois | Mois depuis dernière relocation |
| **Vacance_longue** | **1 = risque élevé** |

## Pas à pas

1. Classification sur `Vacance_longue`
2. Identifiez les leviers (loyer, DPE, bruit) sur quelques prédictions
