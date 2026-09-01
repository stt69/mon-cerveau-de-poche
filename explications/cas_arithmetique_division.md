## Apprendre la division

---

Cas **pédagogique** : prédire **A ÷ B** (colonne **Quotient**, arrondi à 2 décimales).

B est toujours ≥ 1 (pas de division par zéro). La division est **non-linéaire** : idéal pour comparer régression et réseau.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_arithmetique_division.xlsx`

| Colonne | Description | Exemple |
|---------|-------------|---------|
| A | Dividende (1–10000) | 144 |
| B | Diviseur (1–100) | 12 |
| **Quotient** | **A ÷ B** | **12.0** |

---

### Pas à pas

1. Cible : **Quotient**.
2. Entraînez — observez si le réseau surpasse la régression.
3. Prédisez A=100, B=4 → **25**.

---

### À retenir

La courbe d'apprentissage peut demander un peu plus d'époques : la relation 1/x est plus délicate à approximer.
