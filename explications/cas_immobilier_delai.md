## Prévoir le délai de vente

---

« Ce bien, il va partir en combien de temps ? » Tout agent immobilier entend cette question — du vendeur, du collègue, de lui-même en regardant son portefeuille un lundi matin. On sait qu'un bien au prix du marché part plus vite qu'un bien surévalué, et que le printemps est meilleur que l'hiver. Mais de combien de jours exactement ? Et les photos professionnelles, la visite virtuelle : est-ce que ça change vraiment quelque chose ?

Ce cas apprend au réseau à prédire le **délai de vente en jours** à partir de l'historique de vos mandats aboutis. Vous pourrez trier vos mandats en cours par urgence prévue, chiffrer l'impact d'une baisse de prix, et argumenter avec des données plutôt qu'avec des impressions.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_immobilier_delai.xlsx`

Le fichier contient environ 300 mandats terminés (vendus) sur trois ans. Chaque ligne = un bien mis en vente puis vendu.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Type_bien | Type (1 = appartement, 2 = maison, 3 = terrain, 4 = autre) | 1 |
| Prix_affiche | Prix affiché initial (€) | 420 000 |
| Ecart_prix_marche_pct | Écart par rapport au marché (%, + = surévalué) | 8 |
| Saison | Saison de mise en vente (1 = printemps … 4 = hiver) | 1 |
| Nb_photos | Nombre de photos dans l'annonce | 12 |
| Visite_virtuelle | Visite virtuelle disponible (0/1) | 1 |
| **Delai_vente_jours** | **Délai entre mise en vente et acte (jours)** | **45** |

La colonne **Delai_vente_jours** est la cible.

**Point d'attention :** pour prédire le délai *avant* la mise en vente, n'utilisez que des colonnes connues à ce moment-là. Le nombre de visites réalisées, par exemple, n'existe pas encore — ce serait une fuite de données (voir ).

---

### Pas à pas

#### Étape 1 — Charger le fichier

Chargez `cas_immobilier_delai.xlsx` dans l'application.

Vérifiez : environ 300 lignes, 7 colonnes, données propres.

#### Étape 2 — Choisir la cible

Sélectionnez **Delai_vente_jours**.

#### Étape 3 — Choisir les réglages

300 lignes → préréglage **Moyen** (2 couches, 16 neurones, 300 époques).

#### Étape 4 — Entraîner

Lancez l'entraînement. La courbe MAE devrait converger en une dizaine de secondes.

#### Étape 5 — Analyser les résultats

- **MAE en jours** : par exemple 12 jours sur des délais moyens de 60 jours → erreur de 20 %, correct pour orienter le portefeuille
- **R² > 0.70** → le réseau capture une part significative des variations de délai

Regardez les résidus : le réseau sous-estime-t-il systématiquement les biens surévalués ? C'est un signal utile pour affiner vos données.

#### Étape 6 — Prédire et trier le portefeuille

Préparez un fichier avec vos mandats en cours (mêmes colonnes, sans **Delai_vente_jours**). Chargez-le en prédiction par lot, ou entrez les biens un par un :

| Bien (exemple) | Délai prédit |
|----------------|-------------|
| T3 centre, prix marché, printemps | ~22 jours |
| Maison jardin, +5 % au-dessus du marché | ~48 jours |
| T2 sans parking, +12 % au-dessus du marché | ~95 jours |

**Actions concrètes :**
- Biens à vente rapide → priorité communication, vitrine, réseaux sociaux
- Biens lents → revoir le prix, améliorer les photos, home staging

**Tester une baisse de prix :**
Entrez le même bien avec **Ecart_prix_marche_pct** = 12, puis = 5, puis = 0. Observez comment le délai prédit diminue. Vous avez un argument chiffré pour la discussion avec le vendeur.

---

### Interpréter le résultat pour prendre une décision

Le délai de vente est l'une des métriques les plus sensibles pour un agent. Un portefeuille qui traîne coûte du temps, de l'énergie et de la satisfaction client.

**Ce que le réseau quantifie mieux que l'intuition :**
- La courbe de pénalité de surévaluation : +5 % au-dessus du marché coûte combien de jours ? +15 % ?
- L'effet mesurable des photos (nombre et qualité proxy via **Nb_photos**)
- L'apport de la visite virtuelle sur le délai

**Ce que le réseau ne voit pas :**
- Le charme du bien, la vue, le vis-à-vis
- La motivation du vendeur à négocier
- Un événement local (nouvelle ligne de tram, fermeture d'usine)

Utilisez la prédiction comme **ordre de grandeur priorisé**, pas comme date exacte de signature.

---

### Exercice

1. Entraînez le modèle sur `cas_immobilier_delai.xlsx`, cible **Delai_vente_jours**.
2. Notez le MAE (en jours) et le R².
3. Prédisez le délai pour : appartement (Type_bien = 1), prix 380 000 €, +8 % au-dessus du marché, mise en vente en hiver (Saison = 4), 8 photos, sans visite virtuelle.
4. Refaites la prédiction en passant **Ecart_prix_marche_pct** à 0 et **Saison** à 1 (printemps). Comparez.
5. Listez trois mandats fictifs ou réels et classez-les par délai prédit croissant.
