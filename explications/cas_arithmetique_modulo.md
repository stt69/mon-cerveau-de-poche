## Apprendre le modulo (reste)

---

Cas **pédagogique** : prédire le **reste de la division euclidienne** A mod B (colonne **Reste**).

Exemple : 17 mod 5 = **2**. Opération discrète et non-linéaire — le réseau doit apprendre un motif périodique.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_arithmetique_modulo.xlsx`

| Colonne | Description | Exemple |
|---------|-------------|---------|
| A | Dividende (0–9999) | 17 |
| B | Diviseur (2–99) | 5 |
| **Reste** | **A mod B** | **2** |

---

### Pas à pas

1. Cible : **Reste**.
2. Préréglage **Moyen** — l'opération modulo est plus difficile qu'une addition.
3. Testez A=100, B=7 → **2**.

---

### À retenir

Les résultats sont entiers et bornés (toujours < B). Un R² élevé montre que le réseau peut apprendre des règles « à trous », pas seulement des droites.
