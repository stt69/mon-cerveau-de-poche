## Apprendre l'addition

---

Cas **pédagogique** : le réseau apprend à reproduire une calculatrice. Ici, il doit prédire **A + B**.

Chaque ligne contient deux nombres **A** et **B**, et la cible **Somme** = A + B. Aucun bruit : la règle est exacte. Si le réseau converge bien (R² proche de 1), c'est la preuve qu'il a « compris » l'addition.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_arithmetique_addition.xlsx`

| Colonne | Description | Exemple |
|---------|-------------|---------|
| A | Premier nombre (0–1000) | 347 |
| B | Second nombre (0–1000) | 582 |
| **Somme** | **A + B** | **929** |

---

### Pas à pas

1. Chargez le fichier, cible **Somme**.
2. Préréglage **Petit** suffit (règle simple).
3. Entraînez — vous devriez obtenir un R² très élevé.
4. Prédisez : A=125, B=875 → attendez **1000**.

---

### À retenir

L'addition est **linéaire** : la régression linéaire devrait déjà bien performer. Comparez régression et réseau dans le tableau comparatif.
