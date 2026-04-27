# DangerousShots — Accidents et décès sur tournages (2004–2024)

## Description

Projet data analyst personnel analysant les accidents et décès survenus sur des tournages de films et séries TV entre 2004 et 2024.

L'objectif est de croiser les données de sécurité (type d'accident, gravité, catégorie de victime) avec des données de production (budget, box-office, note IMDb, genre) pour identifier des tendances et facteurs de risque.

---

## Stack technique

| Outil | Usage |
|---|---|
| Python | Pipeline de données |
| Pandas | Nettoyage et analyse |
| Matplotlib / Seaborn | Visualisations |
| Streamlit | Dashboard interactif |
| Docker | Conteneurisation |

---

## Structure du projet

```
DangerousShots/
│
├── data/
│   ├── raw/                        # Données brutes
│   └── processed/
│       └── accidents_clean.csv     # Dataset enrichi (25 incidents, 24 colonnes)
│
├── src/
│   ├── loaders/
│   │   └── load_csv.py             # Chargement des données
│   └── analysis/
│       ├── clean.py                # Nettoyage et typage
│       ├── analyze.py              # KPIs et agrégations
│       └── visualize.py            # Graphiques
│
├── dashboard/
│   └── streamlit_app.py            # Dashboard Streamlit
│
├── notebooks/                      # Analyses exploratoires Jupyter
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Dataset

**25 incidents documentés** sur la période 2004–2024, couvrant films et séries TV.

| Colonne | Description |
|---|---|
| `annee` | Année de l'incident |
| `film` | Titre du film ou de la série |
| `genre` | Genre cinématographique |
| `type_production` | Film ou Série TV |
| `budget_million_usd` | Budget de production (M$) |
| `box_office_million_usd` | Recettes mondiales (M$) |
| `note_imdb` | Note IMDb |
| `nb_votes_imdb` | Nombre de votes IMDb |
| `popularite` | Faible / Moyenne / Élevée / Très élevée |
| `roi` | Ratio box-office / budget |
| `victime` | Nom de la victime |
| `categorie_victime` | Acteur ou Technicien |
| `type_accident` | Nature de l'accident |
| `deces` | Décès (True/False) |
| `gravite` | Décès ou Blessure |
| `cause` | Description de l'accident |
| `pays_tournage` | Pays du tournage |
| `studio` | Studio de production |
| `tranche_budget` | Catégorie de budget |
| `decennie` | 2000s / 2010s / 2020s |
| `genre_simplifie` | Genre regroupé |

---

## Principaux enseignements

1. **Les techniciens sont les premières victimes** — 80% des incidents concernent cascadeurs, cadreurs et équipes techniques
2. **Les films d'action concentrent la majorité des accidents** — explosions, cascades moto et véhicules
3. **Le budget n'est pas un facteur protecteur** — plusieurs blockbusters à 200M$+ sont impliqués
4. **Les chutes et accidents de véhicules** sont les causes les plus fréquentes
5. **Les séries TV** sont sous-représentées dans les données publiques malgré un volume de production élevé

---

## Lancement

### Avec Docker

```bash
docker-compose up --build
```

Accès : **http://localhost:8501**

### Sans Docker

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
streamlit run dashboard/streamlit_app.py
```

---

## Sources

- Wikipedia — *Deaths and injuries in film and television production*
- IMDb — notes, votes et données de production
- Box Office Mojo — recettes mondiales
- Presse spécialisée (Variety, The Hollywood Reporter, Deadline)

---

## Auteur

**Philippe Kirstetter-Fender**
Projet personnel — Data Analyst / Data Engineer