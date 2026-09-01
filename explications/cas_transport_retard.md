## Détecter les trajets à risque de retard

---

Un trajet en heure de pointe, par mauvais temps, avec travaux sur l'itinéraire : le risque de retard monte. Le repérer à l'avance permet de prévenir le client ou de choisir un autre créneau.

Ce cas classifie les trajets selon le **risque de retard** (classification).

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_transport_retard.xlsx`

Le fichier contient environ 500 lignes de données réalistes (synthétiques mais cohérentes). Chaque ligne correspond à un cas historique.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Heure_depart | Tranche horaire de départ (1–5) | 3 |
| Jour_semaine | Jour de la semaine (1–7) | 4 |
| Zone | Zone géographique (1–3) | 2 |
| Distance_km | Distance (km) | 50.5 |
| Meteo | Conditions météo (1–4) | 2 |
| Evenement | Événement spécial (0/1) | 0 |
| Travaux | Travaux sur l'itinéraire (0/1) | 0 |
| Heure_pointe | Heure de pointe (0/1) | 0 |
| Type_vehicule | Type de véhicule (1–3) | 2 |
| Anciennete_chauffeur | Ancienneté chauffeur (années) | 10 |
| **Retard** | **Retard (classes 0–2)** | **1** |

La colonne **Retard** est la cible.

Ouvrez le fichier dans Excel avant de lancer l'application. Repérez les tendances à l'œil nu — le réseau les quantifiera de façon systématique.

---

### Pas à pas (classification)

#### Étape 1 — Charger le fichier

Chargez `programs/excel/cas_transport_retard.xlsx`. Vérifiez que **Retard** contient un petit nombre de classes distinctes (typiquement 3).

#### Étape 2 — Choisir la cible

Sélectionnez **Retard**. L'application bascule en mode **Classification**.

#### Étape 3 — Choisir les réglages

Préréglage **Grand** (2 couches, 32 neurones, 400 époques) ou valeurs par défaut.

#### Étape 4 — Entraîner

Cliquez **« Entraîner le modèle »**. Observez la **précision** monter au fil des époques.

#### Étape 5 — Analyser les résultats

Consultez la **précision** et la **matrice de confusion**. Identifiez quel type d'erreur est le plus coûteux dans votre métier (faux positifs vs faux négatifs).

#### Étape 6 — Prédire et agir

Entrez les caractéristiques d'un nouveau cas :

| Entrée | Valeur |
|--------|--------|
| Heure_depart | 3 |
| Jour_semaine | 4 |
| Zone | 2 |
| Distance_km | 50.5 |

Le réseau renvoie une **classe prédite** pour **Retard**. Utilisez ce signal pour prioriser vos actions — toujours avec validation humaine.

---

### Interpréter le résultat pour prendre une décision

Trajets à risque de retard → marge horaire ou itinéraire alternatif.

> **Key takeaway** : enrichissez le fichier avec vos propres données au fil du temps. Plus l'historique est riche et local, plus les prédictions sont utiles.

---

### Exercice

1. Chargez `cas_transport_retard.xlsx` et choisissez **Retard** comme cible (classification).
2. Entraînez le modèle ; notez la précision et étudiez la matrice de confusion.
3. Prédisez la classe pour un cas type (voir étape 6).
4. Modifiez une entrée pour basculer la prédiction vers une autre classe.
5. Listez trois cas réels et vérifiez si le modèle confirme votre intuition.
