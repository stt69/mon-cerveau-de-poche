## Estimer le coût matière d'un plat

---

Combien coûte réellement un plat au fournisseur ? Entre la complexité, la saison et la gamme, le food cost varie fortement — difficile à estimer à l'œil.

Ce cas estime le **coût matière (CHF)** d'un plat à partir de ses caractéristiques.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_gastronomie_foodcost.xlsx`

Le fichier contient environ 280 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un plat du menu.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_plat | Type de plat (1–5) | 3 |
| Nb_ingredients | Nombre d'ingrédients | 8 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Gamme | Gamme (1=standard … 3=haute) | 2 |
| Portion_g | Portion (g) | 180 |
| Origine_bio | Bio (0/1) | 1 |
| Complexite | Complexité (1–5) | 4 |
| **Cout_matiere_CHF** | **Coût matière (CHF)** | **12.5** |

La colonne **Cout_matiere_CHF** est la cible.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Chargez `cas_gastronomie_foodcost.xlsx`. Vérifiez : environ 280 lignes, 8 colonnes.

#### Étape 2 — Choisir la cible

Sélectionnez **Cout_matiere_CHF** comme colonne cible.

#### Étape 3 — Entraîner

Préréglage **Moyen** recommandé. Cliquez **« Entraîner le réseau »**.

#### Étape 4 — Analyser et prédire

Consultez MAE et R². Prédisez le coût matière d'un nouveau plat pour ajuster le prix de vente et la marge.

---

### Interpréter le résultat

Un food cost prédit à 14 CHF pour une vente à 45 CHF laisse une marge brute confortable avant main-d'œuvre et charges.

> **Key takeaway** : recalculez vos fiches techniques au fil des saisons — le modèle s'améliore avec vos propres données.

---

### Exercice

1. Entraînez le modèle sur `cas_gastronomie_foodcost.xlsx`.
2. Prédisez le coût d'un plat avec 10 ingrédients, gamme 3, portion 220 g.
3. Comparez avec votre fiche technique habituelle.
