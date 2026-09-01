## Détecter le risque de no-show

---

Une table réservée qui reste vide, c'est du chiffre perdu et du gaspillage en cuisine. Certains créneaux et profils de clients no-show plus souvent que d'autres.

Ce cas entraîne un modèle de **classification** pour estimer le risque de no-show (0 = présent, 1 = absent).

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_gastronomie_noshow.xlsx`

Environ 300 réservations historiques.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Jour_semaine | Jour (1–7) | 5 |
| Heure_service | Heure du service | 20 |
| Nb_convives | Nombre de convives | 4 |
| Delai_reservation_j | Délai de réservation (jours) | 14 |
| Meteo | Météo (1–4) | 2 |
| Evenement | Événement local (0/1) | 0 |
| Premiere_visite | Première visite (0/1) | 1 |
| **No_show** | **No-show (0/1)** | **0** |

La colonne **No_show** est la cible.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Chargez `cas_gastronomie_noshow.xlsx`.

#### Étape 2 — Choisir la cible

Sélectionnez **No_show** (classification binaire).

#### Étape 3 — Entraîner et analyser

Consultez la matrice de confusion et la précision. Un modèle utile repère les réservations à risque.

---

### Interpréter le résultat

Réservation à risque élevé → demander une confirmation, acompte ou sur-réservation légère — jamais pour stigmatiser un client.

> **Key takeaway** : l'objectif est d'optimiser le remplissage, pas de juger les clients.

---

### Exercice

1. Entraînez le classifieur et notez la précision.
2. Testez une réservation : samedi 21 h, 6 convives, première visite, météo 3.
3. Quelle action concrète prendriez-vous en salle ?
