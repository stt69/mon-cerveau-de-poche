## Estimer le prix de vente d'un appartement

**Fichier** : `synchrotech_11_prix_vente_appartement.xlsx`
**Type** : Régression
**Cible** : `Prix_vente_CHF`

## Le contexte

Objectiver une estimation de vente à partir de surface, pièces, étage, année, canton, balcon, parking et état de rénovation — plutôt que de se fier uniquement à trois comparables.

## Les données

| Colonne | Signification |
|---------|---------------|
| Surface_m2 | Surface habitable |
| Pieces | Nombre de pièces |
| Etage | Étage (0 = rez) |
| Annee_construction | Année de construction |
| Canton | 0 = VS, 1 = VD, 2 = GE |
| Balcon | 0/1 |
| Parking | 0/1 |
| Renove | 0 = non, 1 = partiel, 2 = complet |
| **Prix_vente_CHF** | **Prix de vente (cible)** |

## Pas à pas

1. Chargez le fichier, cible = `Prix_vente_CHF`
2. Préréglage **Moyen** (~180 lignes)
3. Entraînez ; notez MAE et R² ; lisez la recommandation régression vs réseau

## Application concrète

Appartement 95 m², 4 pièces, 3ᵉ étage, construit en 1998, canton VD, balcon + parking, rénové partiellement. Comparez la prédiction à votre grille locale.
