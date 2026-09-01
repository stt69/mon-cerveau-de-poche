## Apprendre la puissance

---

Cas **pédagogique** : prédire **A^B** (colonne **Puissance**).

A va de 2 à 20, B (exposant) de 2 à 5. Exemple : 2^10 = 1024. Opération **fortement non-linéaire**.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_arithmetique_puissance.xlsx`

| Colonne | Description | Exemple |
|---------|-------------|---------|
| A | Base (2–20) | 3 |
| B | Exposant (2–5) | 4 |
| **Puissance** | **A^B** | **81** |

---

### Pas à pas

1. Cible : **Puissance**.
2. Préréglage **Moyen** ou **Grand**.
3. Testez A=2, B=10 → **1024**.

---

### À retenir

Les valeurs cibles peuvent être grandes : le réseau normalise en interne, mais vérifiez que les prédictions restent cohérentes sur les grands exposants.
