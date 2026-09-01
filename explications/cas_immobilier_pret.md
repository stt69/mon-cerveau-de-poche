## Chapitre 26 — Anticiper le montant d'un prêt accordé

---

Un couple entre dans votre bureau : « On peut emprunter combien ? » Vous connaissez la règle des 33 % d'endettement, le poids du CDI, l'importance de l'apport. Vous faites un calcul rapide sur une feuille — et la banque accorde parfois 20 000 € de moins, parfois 15 000 € de plus. Pourquoi ? Parce que les banques appliquent des critères officiels *et* des pratiques réelles que seul l'historique révèle.

Ce chapitre entraîne le réseau sur vos dossiers passés pour estimer le **montant réellement accordé** — pas le montant théorique du calculateur, mais ce que votre réseau bancaire a effectivement validé pour des profils similaires.

---

### Le fichier exemple

> **Fichier** : `programs/excel/cas_immobilier_pret.xlsx`

Environ 500 dossiers traités sur trois ans par un courtier en prêts immobiliers.

| Colonne | Description | Exemple |
|---------|-------------|---------|
| Revenu_mensuel | Revenus nets mensuels de l'emprunteur (€) | 4 200 |
| Apport_euros | Apport personnel (€) | 45 000 |
| Charges_mensuelles | Charges existantes — crédits, pensions… (€) | 380 |
| Duree_pret_mois | Durée souhaitée (mois) | 240 |
| Type_bien | Bien visé (1 = résidence principale, 2 = secondaire, 3 = locatif, 4 = autre) | 1 |
| Taux_interet_pct | Taux obtenu ou simulé (%) | 3.2 |
| **Montant_accorde** | **Montant du prêt accordé (€)** | **310 000** |

La colonne **Montant_accorde** est la cible.

---

### Pas à pas

#### Étape 1 — Charger le fichier

Chargez `cas_immobilier_pret.xlsx`.

Vérifiez : ~500 lignes, 7 colonnes, pas de valeurs manquantes.

#### Étape 2 — Choisir la cible

Sélectionnez **Montant_accorde**.

#### Étape 3 — Choisir les réglages

500 lignes → préréglage **Moyen** ou **Grand** selon les résultats.

#### Étape 4 — Entraîner

Lancez l'entraînement. Avec 500 dossiers, la convergence est rapide.

#### Étape 5 — Analyser les résultats

- **MAE = 12 000 €** sur des prêts moyens de 280 000 € → erreur ~4 % — excellent pour pré-qualifier un client
- **R² > 0.85** → le réseau reproduit bien la logique réelle des accords bancaires

Comparez mentalement avec le calcul « règle des 33 % » : l'écart entre théorie et prédiction réseau reflète les pratiques non écrites (reste à vivre, politique interne de la banque, profil client).

#### Étape 6 — Pré-qualifier un dossier

Exemple — couple en résidence principale :

| Entrée | Valeur |
|--------|--------|
| Revenu_mensuel | 5 800 |
| Apport_euros | 60 000 |
| Charges_mensuelles | 290 |
| Duree_pret_mois | 300 |
| Type_bien | 1 |
| Taux_interet_pct | 3.4 |

**Calcul théorique rapide :** (5 800 − 290) × 33 % ≈ 1 827 €/mois de mensualité max → environ 380 000 € sur 25 ans.

**Prédiction réseau :** par exemple **352 000 €** (MAE ± 12 000 €).

La différence n'est pas une erreur — c'est l'expérience passée qui parle. Utilisez la prédiction réseau pour cadrer la recherche de bien dès le premier rendez-vous.

---

### Interpréter le résultat pour prendre une décision

**Scénarios à tester en direct avec le client :**

| Question du client | Modification dans le fichier |
|--------------------|------------------------------|
| « Si je rembourse mon crédit auto avant ? » | Charges_mensuelles − 350 € |
| « Si on emprunte sur 20 ans au lieu de 25 ? » | Duree_pret_mois = 240 |
| « Si on vise un investissement locatif ? » | Type_bien = 3 |
| « Si mon conjoint ne travaille pas en CDI ? » | (nécessite une colonne supplémentaire dans vos propres données) |

**Limites à garder en tête :**
- Le réseau ne remplace pas la négociation bancaire
- Un dossier atypique (fort patrimoine, revenus variables) peut échapper au modèle
- Mettez à jour le fichier régulièrement : les critères bancaires évoluent

> **Key takeaway** : cet outil donne au courtier une longueur d'avance. Le client repart du premier contact avec une fourchette crédible — et vous montez un dossier aligné sur la réalité du terrain, pas sur une calculette optimiste.

---

### Exercice

1. Entraînez le modèle sur **Montant_accorde**.
2. Notez le MAE et le R².
3. Pré-qualifiez ce profil : revenus 3 400 €/mois, apport 25 000 €, charges 520 €, durée 240 mois, résidence principale, taux 3.1 %.
4. Refaites la prédiction en augmentant l'apport à 55 000 €. Quel gain de capacité d'emprunt le réseau estime-t-il ?
5. Comparez la prédiction réseau avec le calcul manuel des 33 % d'endettement. Comment expliqueriez-vous l'écart à un client ?
