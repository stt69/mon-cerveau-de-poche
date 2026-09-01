## Apprendre la multiplication

---

Cas **pédagogique** : prédire **A × B** (colonne **Produit**).

A et B vont de 0 à 100. La multiplication n'est **plus linéaire** en A et B pris séparément : le réseau doit capturer l'**interaction** entre les deux entrées.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_arithmetique_multiplication.xlsx`

| Colonne | Description | Exemple |
|---------|-------------|---------|
| A | Premier facteur (0–100) | 12 |
| B | Second facteur (0–100) | 8 |
| **Produit** | **A × B** | **96** |

---

### Pas à pas

1. Cible : **Produit**.
2. Préréglage **Moyen** recommandé (non-linéarité).
3. Comparez : la régression linéaire devrait être nettement moins bonne que le réseau.

---

### À retenir

Excellent cas pour voir **quand le réseau apporte un vrai gain** sur une simple droite.
