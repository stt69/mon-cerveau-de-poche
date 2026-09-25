## Vente rapide (moins de 90 jours)

**Fichier** : `synchrotech_17_vente_rapide.xlsx`
**Type** : Classification
**Cible** : `Vente_rapide` (0/1)

## Le contexte

Repérer les mandats susceptibles de partir rapidement selon l'écart au marché, l'état, les photos, l'exclusivité et l'activité de visites.

## Les données

| Colonne | Signification |
|---------|---------------|
| Prix_m2_vs_marche | Écart relatif au marché |
| Etat_bien | 0–2 |
| Photos_pro | 0/1 |
| Mandat_exclusif | 0/1 |
| Nb_visites_30j | Visites sur 30 jours |
| Baisse_prix | 0/1 |
| **Vente_rapide** | **1 = vente < 90 jours** |

## Pas à pas

1. Mode **Classification**, cible = `Vente_rapide`
2. Lisez la matrice de confusion et la précision
3. Simulez un bien surévalué avec peu de visites
