## Estimer la durée d'un service

---

Combien de temps une table occupe-t-elle la salle ? La rotation des couverts dépend du nombre de plats, de la taille du groupe et de l'expérience de l'équipe.

Ce cas prédit la **durée du service (min)** pour planifier les réservations.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_gastronomie_service.xlsx`

Environ 250 services passés.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Nb_couverts | Nombre de couverts | 42 |
| Formule | Formule (1=déjeuner … 3=dégustation) | 3 |
| Nb_services | Nombre de services | 6 |
| Experience_salle | Expérience salle (1–5) | 4 |
| Jour_semaine | Jour (1–7) | 6 |
| Groupe | Groupe (0/1) | 0 |
| **Duree_service_min** | **Durée du service (min)** | **165** |

La colonne **Duree_service_min** est la cible.

---

### Pas à pas

Chargez le fichier, sélectionnez **Duree_service_min**, entraînez (préréglage **Moyen**), prédisez.

---

### Interpréter le résultat

Un service prédit à 180 min avec formule dégustation → ne pas enchaîner deux rotations sur la même table le même soir.

> **Key takeaway** : ajustez les créneaux de réservation selon la durée prédite par formule.

---

### Exercice

1. Entraînez le modèle et notez le MAE.
2. Prédisez pour 50 couverts, formule 3, 7 services.
3. Combien de rotations possibles entre 19 h et 23 h ?
