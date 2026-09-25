## Visites mensuelles du portefeuille

**Fichier** : `synchrotech_21_visites_mensuelles.xlsx`
**Type** : Régression
**Cible** : `Nb_visites`

## Le contexte

Prévoir le volume de visites d'un portefeuille courtage selon les biens actifs, nouveaux mandats, occupation et budget publicitaire.

## Les données

| Colonne | Signification |
|---------|---------------|
| Mois | Période (AAAA-MM) — à ignorer si non numérique |
| Nb_biens_actifs | Mandats actifs |
| Nb_nouveaux_mandats | Nouveaux mandats |
| Taux_occupation_pct | Taux d'occupation |
| Budget_pub_CHF | Budget pub |
| **Nb_visites** | **Nombre de visites (cible)** |

## Pas à pas

1. Si la colonne `Mois` est ignorée (texte), c'est normal
2. Entraînez sur les colonnes numériques, cible = `Nb_visites`
