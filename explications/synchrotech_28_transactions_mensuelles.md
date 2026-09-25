## Transactions mensuelles du marché local

**Fichier** : `synchrotech_28_transactions_mensuelles.xlsx`
**Type** : Régression
**Cible** : `Nb_transactions`

## Le contexte

Anticiper le nombre de transactions locales selon taux hypothécaire, confiance, annonces et prix au m² moyen.

## Les données

| Colonne | Signification |
|---------|---------------|
| Mois | Période (texte — peut être ignorée) |
| Taux_hypotheque | Taux |
| Indice_confiance | Indice |
| Nb_annonces_neuves | Annonces |
| Prix_m2_moyen | Prix m² moyen |
| **Nb_transactions** | **Transactions (cible)** |

## Pas à pas

1. Cible = `Nb_transactions`
2. Simulez une hausse de taux de 0,5 point
