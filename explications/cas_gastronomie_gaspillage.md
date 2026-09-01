## Anticiper le gaspillage alimentaire

---

Préparer trop, c'est jeter ; préparer trop peu, c'est servir en rupture. Le gaspillage dépend des écarts entre couverts prévus et réels, du menu et de la météo.

Ce cas prédit le **gaspillage (kg)** en fin de service.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_gastronomie_gaspillage.xlsx`

Environ 240 services.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Couverts_prevus | Couverts prévus | 65 |
| Couverts_reels | Couverts réalisés | 58 |
| Meteo | Météo (1–4) | 3 |
| Menu_du_jour | Menu du jour (0/1) | 1 |
| Invendus_veille_kg | Invendus de la veille (kg) | 2.5 |
| Type_cuisine | Type (1=bistro … 3=gastronomique) | 3 |
| **Gaspillage_kg** | **Gaspillage (kg)** | **8.2** |

La colonne **Gaspillage_kg** est la cible.

---

### Pas à pas

Chargez, sélectionnez **Gaspillage_kg**, entraînez, prédisez pour le prochain service.

---

### Interpréter le résultat

8 kg prédits sur un service de 60 couverts → revoir les quantités de mise en place ou proposer un plat du jour adapté.

> **Key takeaway** : suivez le gaspillage réel chaque semaine pour affiner le modèle.

---

### Exercice

1. Entraînez et comparez MAE réseau vs régression.
2. Prédisez pour 70 couverts prévus, 62 réels, menu du jour.
3. Quelle action en cuisine pour réduire le gaspillage ?
