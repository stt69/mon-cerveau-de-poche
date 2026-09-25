## Charges annuelles décomposées

**Fichier** : `synchrotech_16_charges_annuelles.xlsx`
**Type** : Régression multi-sorties
**Cibles** : `Charge_chauffage`, `Charge_eau`, `Charge_entretien`, `Charge_assurance`

## Le contexte

Prévoir la répartition des charges d'un logement pour la gérance ou la communication aux locataires / PPE.

## Les données

| Colonne | Signification |
|---------|---------------|
| Surface_m2 | Surface |
| Annee_construction | Année |
| Nb_logements_immeuble | Nombre de logements |
| Type_chauffage | 0–2 |
| **Charge_*** | **Quatre cibles de charges annuelles** |

## Pas à pas

1. Sélectionnez les **quatre** colonnes cibles
2. Mode **Régression**
3. Observez MAE et R² par poste
