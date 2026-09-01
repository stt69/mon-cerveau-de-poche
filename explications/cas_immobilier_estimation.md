## Chapitre 24 — Estimer la valeur d'un bien immobilier

---

« Combien vaut ce bien ? » C'est la question que se posent agents immobiliers, courtiers et investisseurs plusieurs fois par semaine. On sait intuitivement que la surface, l'emplacement et l'état général font varier le prix — mais de combien exactement ? Et quelle prime pour un balcon, un parking, ou un bon diagnostic énergétique ?

Ce chapitre transforme votre historique de ventes en outil d'estimation. Entraîné sur les transactions passées de votre secteur, le réseau chiffre ce que votre intuition saisit à peu près : le prix au m² par quartier, l'impact d'un état « à rénover », la décote d'un appartement éloigné du centre. Il ne remplace pas une visite sur place — il vous donne une base chiffrée pour cadrer un mandat, vérifier une offre ou repérer une opportunité.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_immobilier_estimation.xlsx`

Le fichier contient environ 400 ventes réalisées sur trois ans dans un bassin immobilier (ville moyenne et périphérie). Chaque ligne correspond à une transaction aboutie.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Surface_m2 | Surface habitable (m²) | 85 |
| Nb_pieces | Nombre de pièces | 4 |
| Etage | Étage (0 = RDC ou maison) | 3 |
| Annee_construction | Année de construction | 1998 |
| Etat | État général (1 = à rénover … 5 = neuf) | 3 |
| Balcon | Balcon ou terrasse (0/1) | 1 |
| Parking | Place de parking ou garage (0/1) | 0 |
| Distance_centre_km | Distance au centre-ville (km) | 2.5 |
| **Prix_euros** | **Prix de vente réalisé (€)** | **385 000** |

La colonne **Prix_euros** est la cible. Les huit autres colonnes servent d'entrées.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les grandes tendances : les biens proches du centre se vendent-ils plus cher ? Les biens avec parking ? Le réseau va quantifier ces effets — et surtout leurs combinaisons (petit appartement au 5e sans ascenseur vs même surface avec parking en périphérie, par exemple).

---

### Pas à pas

#### Étape 1 — Charger le fichier

Ouvrez *Mon Cerveau de Poche*. Chargez `cas_immobilier_estimation.xlsx`.

Vérifiez l'aperçu : environ 400 lignes, 9 colonnes, pas de cellule vide, valeurs numériques partout.

#### Étape 2 — Choisir la cible

Sélectionnez **Prix_euros** comme colonne cible.

Les huit autres colonnes deviennent automatiquement les entrées.

#### Étape 3 — Choisir les réglages

Avec 400 lignes, vous êtes dans le cas « jeu de données moyen ». Utilisez le préréglage **Moyen** ou :

| Paramètre | Valeur recommandée |
|-----------|-------------------|
| Couches cachées | 2 |
| Neurones | 16 |
| Époques | 300 |
| Taux d'apprentissage | 0.001 |

#### Étape 4 — Entraîner

Cliquez sur **« Entraîner le modèle »**.

Observez la courbe MAE : elle devrait descendre puis se stabiliser. Avec 400 ventes, l'entraînement prend quelques secondes.

#### Étape 5 — Analyser les résultats

Consultez le MAE et le R². Par exemple :
- **MAE = 18 000 €** sur des prix moyens de 350 000 € → erreur d'environ 5 % — très bon pour de l'estimation immobilière
- **R² > 0.85** → le réseau capture bien les variations de prix dans votre secteur

Le graphique **Prédit vs Réel** : les points doivent suivre la diagonale. Des points très éloignés signalent des ventes atypiques (négociation exceptionnelle, défaut caché, etc.).

#### Étape 6 — Prédire

Entrez les caractéristiques d'un bien à estimer, par exemple :

| Entrée | Valeur |
|--------|--------|
| Surface_m2 | 75 |
| Nb_pieces | 3 |
| Etage | 2 |
| Annee_construction | 2005 |
| Etat | 4 |
| Balcon | 1 |
| Parking | 1 |
| Distance_centre_km | 1.2 |

Le réseau affiche un prix estimé — par exemple **342 000 €**. Ajustez ensuite à la hausse ou à la baisse selon ce que vous voyez sur place (vue, bruit, charme du bien) : le réseau ne connaît que ce qui est dans le tableau.

---

### Interpréter le résultat pour prendre une décision

**Pour un agent immobilier — prise de mandat :**
Vous proposez un prix de mise en vente argumenté. « Mon historique et mon modèle estiment ce bien autour de 340 000 €. Avec la rénovation récente de la cuisine, nous pouvons viser 355 000 €. »

**Pour un courtier — cohérence du dossier :**
Le client achète à 400 000 € alors que le réseau estime 340 000 €. Signal d'alerte : bien surévalué, risque pour le financement ou revente difficile.

**Pour un investisseur — repérage d'opportunités :**
Comparez le prix demandé sur une annonce avec l'estimation réseau. Un écart de −10 % ou plus peut valoir une visite prioritaire.

**Tester des scénarios :**
- « Si le vendeur rénove (Etat 2 → 4), combien ça ajoute ? »
- « Sans parking, combien perd-on ? »

Entrez deux prédictions côte à côte dans l'application : le réseau chiffre le retour sur investissement des travaux ou la décote d'un défaut.

> **Key takeaway** : enrichissez le fichier à chaque nouvelle vente réalisée. Plus l'historique est riche et local, plus l'estimation est fine — bien plus qu'une moyenne nationale tirée d'un site généraliste.

---

### Exercice

1. Chargez `cas_immobilier_estimation.xlsx` et entraînez le modèle sur **Prix_euros**.
2. Notez le MAE et le R².
3. Estimez un appartement 65 m², 3 pièces, 4e étage, construit en 1990, état correct (3), sans balcon, avec parking, à 3 km du centre.
4. Refaites la même prédiction en changeant uniquement **Etat** à 5 (neuf/rénové). Observez l'écart.
5. Si vous avez un bien réel dans votre portefeuille, entrez ses caractéristiques et comparez l'estimation au prix que vous aviez en tête.
