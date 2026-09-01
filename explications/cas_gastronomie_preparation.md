## Estimer le temps de préparation

---

Combien de minutes en cuisine avant le service ? Entre le menu du jour, les couverts et l'équipe, l'estimation varie — et un mauvais chiffrage retarde tout le service.

Ce cas prédit le **temps de préparation (min)** pour planifier la brigade.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_gastronomie_preparation.xlsx`

Environ 260 lignes. Chaque ligne = un service passé.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Complexite_menu | Complexité du menu (1–5) | 4 |
| Couverts_prevus | Couverts prévus | 55 |
| Postes_cuisine | Postes cuisine actifs | 5 |
| Type_service | Type (1=déjeuner … 3=dîner gastronomique) | 3 |
| Jour_semaine | Jour (1–7) | 6 |
| Evenement | Événement spécial (0/1) | 0 |
| Experience_chef | Expérience du chef (1–5) | 4 |
| **Temps_prep_min** | **Temps de préparation (min)** | **95** |

La colonne **Temps_prep_min** est la cible.

---

### Pas à pas

#### Étape 1 — Charger et entraîner

Chargez le fichier, sélectionnez **Temps_prep_min**, préréglage **Moyen**, entraînez.

#### Étape 2 — Prédire

Entrez les paramètres du prochain service pour estimer le temps de mise en place.

---

### Interpréter le résultat

Planifiez les shifts cuisine : si 110 min sont prédits pour 60 couverts, prévoyez une brigade renforcée dès 15 h.

> **Key takeaway** : croisez la prédiction avec votre feuille de route habituelle pour affiner les plages horaires.

---

### Exercice

1. Entraînez et notez le MAE.
2. Prédisez pour un samedi soir, 70 couverts, menu complexité 5.
3. Quelle décision prendriez-vous sur l'heure d'arrivée de l'équipe ?
