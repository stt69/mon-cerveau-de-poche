## Anticiper les ressources pédagogiques

---

Salles, formateurs, supports, licences : la logistique pédagogique se complique vite en début de trimestre. Anticiper les besoins évite les réservations de dernière minute.

Ce cas prédit **plusieurs ressources en parallèle** (multi-sorties) à partir du nombre de classes et d'élèves.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_enseignement_ressources.xlsx`

Le fichier contient environ 120 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Trimestre | Trimestre (1–4) | 2 |
| Nb_classes | Nombre de classes | 9 |
| Nb_eleves | Nombre d'élèves | 230 |
| Formation_continue | Formation continue (0/1) | 0 |
| **Salles_heures** | **Heures de salles** | **200** |
| **Formateurs_heures** | **Heures formateurs** | **125** |
| **Supports_imprimes** | **Supports imprimés** | **600** |
| **Licences_logiciel** | **Licences logiciel** | **50** |

La colonne **Salles_heures** / **Formateurs_heures** / **Supports_imprimes** / **Licences_logiciel** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_enseignement_ressources.xlsx`. Vérifiez : environ 120 lignes, 8 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Salles_heures
- Formateurs_heures
- Supports_imprimes
- Licences_logiciel

Les 4 colonnes restantes deviennent les entrées. Le réseau prédit 4 sorties **en parallèle**.

#### Étape 3 — Choisir les réglages

Préréglage **Petit** (1 couche, 8 neurones, 200 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le réseau »**. La régression linéaire s'affiche d'abord, puis le réseau (courbe d'erreur pour chaque sortie).

#### Étape 5 — Analyser les résultats

Consultez le tableau comparatif et la recommandation. Vérifiez MAE et R² pour chaque cible.

#### Étape 6 — Prédire

Entrez les entrées du prochain cas :

| Entrée | Valeur |
|--------|--------|
| Trimestre | 2 |
| Nb_classes | 9 |
| Nb_eleves | 230 |
| Formation_continue | 0 |

Le réseau affiche simultanément : **Salles_heures**, **Formateurs_heures**, **Supports_imprimes**, **Licences_logiciel**.

---

### Interpréter le résultat pour prendre une décision

Réservez salles et formateurs dès la prédiction disponible en début de trimestre.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_enseignement_ressources.xlsx` et sélectionnez les cibles : Salles_heures, Formateurs_heures, Supports_imprimes, Licences_logiciel.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
