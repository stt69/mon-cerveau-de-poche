## Surévaluation au diagnostic

**Fichier** : `synchrotech_26_surevaluation.xlsx`
**Type** : Classification
**Cible** : `Surevaluation` (0/1)

## Le contexte

Détecter les biens dont le prix demandé est trop élevé par rapport à une estimation d'expert et à l'état du bien.

## Les données

| Colonne | Signification |
|---------|---------------|
| Prix_demande_CHF | Prix demandé |
| Estimation_expert_CHF | Estimation expert |
| Annee_construction | Année |
| DPE | 0–3 |
| Travaux_prevus_CHF | Travaux prévus |
| **Surevaluation** | **1 = surévalué** |

## Pas à pas

1. Classification sur `Surevaluation`
2. Reliez le résultat à une discussion de prise de mandat
