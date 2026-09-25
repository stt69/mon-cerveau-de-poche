## Risque d'impayé de loyer

**Fichier** : `synchrotech_30_risque_impaye.xlsx`
**Type** : Classification
**Cible** : `Retard_paiement_12m` (0/1)

## Le contexte

Identifier les dossiers locatifs à risque d'impayé pour la gérance (ratio loyer/revenu, garantie, historique, type de bail).

## Les données

| Colonne | Signification |
|---------|---------------|
| Ratio_loyer_revenu | Part du loyer dans le revenu |
| Garantie | 0 = non, 1 = caution, 2 = assurance |
| Anciennete_bail_mois | Ancienneté du bail |
| Incidents_passes | Nombre d'incidents |
| Type_bail | 0 = standard, 1 = temporaire |
| **Retard_paiement_12m** | **1 = retard / impayé** |

## Pas à pas

1. Classification sur `Retard_paiement_12m`
2. Lisez la précision et la matrice de confusion
3. Discutez les leviers (garantie, ratio) avec un scénario de gérance
