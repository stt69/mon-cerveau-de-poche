## Chapitre 46 — Anticiper le temps de post-production

---

Tri, retouche, montage : la post-production mange une part importante du temps total d'un projet photo. Le nombre de photos brutes et le niveau de retouche changent tout.

Ce chapitre prédit **trois postes de temps en heures** (multi-sorties) pour chiffrer et planifier la post-prod.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_photo_postprod.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_projet | Type de projet (1–5) | 3 |
| Nb_photos_brutes | Photos brutes | 525 |
| Niveau_retouche | Niveau de retouche (1–3) | 2 |
| Format_livraison | Format de livraison (1–3) | 2 |
| **Heures_tri** | **Heures de tri** | **2.5** |
| **Heures_retouche** | **Heures de retouche** | **5** |
| **Heures_montage** | **Heures de montage** | **3** |

La colonne **Heures_tri** / **Heures_retouche** / **Heures_montage** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_photo_postprod.xlsx`. Vérifiez : environ 200 lignes, 7 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Heures_tri
- Heures_retouche
- Heures_montage

Les 4 colonnes restantes deviennent les entrées. Le réseau prédit 3 sorties **en parallèle**.

#### Étape 3 — Choisir les réglages

Préréglage **Moyen** (2 couches, 16 neurones, 300 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**. La régression linéaire s'affiche d'abord, puis le réseau (courbe d'erreur pour chaque sortie).

#### Étape 5 — Analyser les résultats

Consultez le tableau comparatif et la recommandation. Vérifiez MAE et R² pour chaque cible.

#### Étape 6 — Prédire

Entrez les entrées du prochain cas :

| Entrée | Valeur |
|--------|--------|
| Type_projet | 3 |
| Nb_photos_brutes | 525 |
| Niveau_retouche | 2 |
| Format_livraison | 2 |

Le réseau affiche simultanément : **Heures_tri**, **Heures_retouche**, **Heures_montage**.

---

### Interpréter le résultat pour prendre une décision

Chiffrez la post-prod dans le devis client à partir des heures prédites.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_photo_postprod.xlsx` et sélectionnez les cibles : Heures_tri, Heures_retouche, Heures_montage.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
