## Délai de mise en location

**Fichier** : `synchrotech_25_delai_mise_location.xlsx`
**Type** : Régression
**Cible** : `Delai_location_jours`

## Le contexte

Prévoir combien de jours un objet restera vacant avant signature du bail.

## Les données

| Colonne | Signification |
|---------|---------------|
| Loyer_demande_CHF | Loyer demandé |
| Surface_m2 | Surface |
| Etat | 0–2 |
| Meuble | 0/1 |
| Mois_mise_dispo | Mois (1–12) |
| Visites_semaine1 | Visites 1ʳᵉ semaine |
| **Delai_location_jours** | **Délai (cible)** |

## Pas à pas

1. Cible = `Delai_location_jours`
2. Observez l'effet des visites de la première semaine
