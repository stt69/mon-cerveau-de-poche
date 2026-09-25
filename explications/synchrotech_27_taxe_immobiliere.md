## Taxe immobilière communale

**Fichier** : `synchrotech_27_taxe_immobiliere.xlsx`
**Type** : Régression
**Cible** : `Taxe_immobiliere_CHF`

## Le contexte

Estimer une taxe immobilière communale à partir de la valeur fiscale, du type de commune et du statut de résidence.

## Les données

| Colonne | Signification |
|---------|---------------|
| Valeur_fiscale_CHF | Valeur fiscale |
| Commune_type | 0 = rural, 1 = ville, 2 = grande ville |
| Taux_communal | Taux |
| Type_bien | 0/1 |
| Residence_principale | 0/1 |
| **Taxe_immobiliere_CHF** | **Taxe (cible)** |

## Pas à pas

1. Entraînez sur `Taxe_immobiliere_CHF`
2. Comparez résidence principale vs secondaire
