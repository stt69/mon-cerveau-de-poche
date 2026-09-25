## Acceptation d'une offre

**Fichier** : `synchrotech_23_offre_acceptee.xlsx`
**Type** : Classification
**Cible** : `Offre_acceptee` (0/1)

## Le contexte

Estimer la probabilité qu'une offre soit acceptée selon l'écart à la demande, le délai déjà écoulé, le nombre d'offres et le financement.

## Les données

| Colonne | Signification |
|---------|---------------|
| Offre_vs_demande_pct | Ratio offre / prix demandé |
| Delai_vente_jours | Jours déjà en vente |
| Nb_offres_concurrentes | Nombre d'offres |
| Financement_acquereur | 0/1 |
| Condition_suspensive | 0/1 |
| **Offre_acceptee** | **1 = acceptée** |

## Pas à pas

1. Classification sur `Offre_acceptee`
2. Simulez une offre à 92 % du prix demandé, sans condition suspensive
