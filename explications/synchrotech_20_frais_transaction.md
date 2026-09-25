## Frais de transaction

**Fichier** : `synchrotech_20_frais_transaction.xlsx`
**Type** : Régression
**Cible** : `Frais_transaction_CHF`

## Le contexte

Estimer les frais liés à une acquisition (notaire, registre, etc.) selon prix, canton, type de bien et hypothèque.

## Les données

| Colonne | Signification |
|---------|---------------|
| Prix_achat_CHF | Prix d'achat |
| Canton | 0–2 |
| Type_bien | 0/1 |
| Premier_achat | 0/1 |
| Hypotheque_pct | Pourcentage hypothéqué |
| **Frais_transaction_CHF** | **Frais (cible)** |

## Pas à pas

1. Cible = `Frais_transaction_CHF`
2. Testez premier achat vs non, même prix
