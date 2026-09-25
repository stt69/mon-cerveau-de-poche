## Prévoir le délai de vente

**Fichier** : `synchrotech_12_delai_vente.xlsx`
**Type** : Régression
**Cible** : `Delai_jours`

## Le contexte

Anticiper combien de jours un mandat restera actif selon le prix demandé, le type de bien, l'état, la saison et la qualité des photos.

## Les données

| Colonne | Signification |
|---------|---------------|
| Prix_demande_CHF | Prix affiché |
| Surface_m2 | Surface |
| Type_bien | 0 = appart., 1 = maison, 2 = terrain |
| Etat | 0–2 |
| Saison_mise_marche | Mois (1–12) |
| Photos_pro | 0/1 |
| Prix_m2_marche | Prix au m² de référence |
| **Delai_jours** | **Délai de vente (cible)** |

## Pas à pas

1. Cible = `Delai_jours`
2. Observez l'effet d'un prix trop haut vs marché (`Prix_demande` vs `Prix_m2_marche × Surface`)
3. Testez avec / sans photos professionnelles
