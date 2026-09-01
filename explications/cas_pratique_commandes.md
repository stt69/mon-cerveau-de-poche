## Anticiper les commandes fournisseurs

---

Au chapitre précédent, le réseau prédisait un seul chiffre : les ventes. Ici, on passe à la vitesse supérieure : le réseau prédit **plusieurs chiffres à la fois**.

Vous allez anticiper les commandes fournisseurs d'un restaurant en une seule passe.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_pratique_commandes.xlsx`

Le fichier contient environ 200 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Semaine | Numéro de semaine (1–52) | 26 |
| Saison | Saison (1=printemps … 4=hiver) | 2 |
| Nb_couverts_prevu | Couverts prévus | 165 |
| Evenement | Événement spécial (0/1) | 0 |
| Meteo | Conditions météo (1–4) | 2 |
| **Legumes_kg** | **Légumes commandés (kg)** | **55** |
| **Viandes_kg** | **Viandes commandées (kg)** | **35** |
| **Poissons_kg** | **Poissons commandés (kg)** | **16** |
| **Boissons_L** | **Boissons commandées (L)** | **80** |

La colonne **Legumes_kg** / **Viandes_kg** / **Poissons_kg** / **Boissons_L** est les cibles.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (multi-sorties)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_pratique_commandes.xlsx`. Vérifiez : environ 200 lignes, 9 colonnes.

#### Étape 2 — Choisir les cibles

Sélectionnez **toutes les colonnes cibles** en même temps :
- Legumes_kg
- Viandes_kg
- Poissons_kg
- Boissons_L

Les 5 colonnes restantes deviennent les entrées. Le réseau prédit 4 sorties **en parallèle**.

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
| Semaine | 26 |
| Saison | 2 |
| Nb_couverts_prevu | 165 |
| Evenement | 0 |

Le réseau affiche simultanément : **Legumes_kg**, **Viandes_kg**, **Poissons_kg**, **Boissons_L**.

---

### Interpréter le résultat pour prendre une décision

Passez commande chez vos fournisseurs dès que les prédictions sont disponibles. Vérifiez la cohérence entre viande, légumes et boissons.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_pratique_commandes.xlsx` et sélectionnez les cibles : Legumes_kg, Viandes_kg, Poissons_kg, Boissons_L.
2. Entraînez le modèle et notez le MAE / R² pour chaque sortie.
3. Prédisez le prochain cas avec les valeurs de l'étape 6.
4. Modifiez une entrée clé et observez l'impact sur toutes les sorties.
5. Comparez avec votre estimation habituelle pour un cas réel de votre activité.
