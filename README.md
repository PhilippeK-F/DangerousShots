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
| Power BI | Dashboard analytics |
| Docker | Conteneurisation |
| GitHub | Versioning |

---

## Structure du projet

```
DangerousShots/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── accidents_clean.csv     # Dataset enrichi (25 incidents, 24 colonnes)
│
├── src/
│   ├── loaders/
│   │   └── load_csv.py
│   └── analysis/
│       ├── clean.py
│       ├── analyze.py
│       └── visualize.py
│
├── dashboard/
│   ├── streamlit_app.py            # Dashboard Streamlit (3 onglets)
│   └── DangerousShots.pbix         # Dashboard Power BI
│
├── notebooks/
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

## Dashboards

### Streamlit (3 onglets)
- **Sécurité** — évolution annuelle, incidents par genre, types d'accidents, budget vs gravité
- **Production & Budget** — note IMDb vs budget, box-office par gravité, ROI par tranche de budget
- **Données brutes** — table complète + export CSV

### Power BI
- 3 KPI Cards : Note IMDb moyenne, Total incidents, Box-office moyen
- 2 Slicers : Pays de tournage, Genre
- Line chart : Incidents par année
- Bar chart : Accidents par type
- Table : Films avec notes, gravité et budget
- Carte : Incidents par pays de tournage

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

## Principaux enseignements

1. **Les chutes sont la première cause d'accident** — 10 incidents sur 25, loin devant les cascades (4) et les explosions (2)
2. **Les techniciens représentent 80% des victimes** — cascadeurs, cadreurs et équipes techniques sont les plus exposés
3. **Les films d'action concentrent la majorité des incidents** — explosions, cascades moto et véhicules
4. **Le budget n'est pas un facteur protecteur** — plusieurs blockbusters à plus de 200M$ sont impliqués
5. **Les USA sont le pays de tournage le plus à risque** — volume de production oblige
6. **Note IMDb moyenne des films concernés : 7.34/10** — ce sont majoritairement de grosses productions populaires

---

## Conclusion

Ce projet met en lumière une réalité souvent invisible du cinéma : derrière les blockbusters les plus populaires et les mieux notés se cachent des accidents graves, parfois mortels, qui touchent avant tout les techniciens de l'ombre.

L'analyse montre que ni le budget, ni la notoriété d'une production ne garantissent la sécurité sur un plateau. Les chutes et accidents de cascade restent les causes dominantes, et les séries TV — malgré un volume de production croissant — restent sous-documentées dans les données publiques disponibles.

Ce dataset, construit manuellement à partir de sources publiques, constitue une base de travail qu'il serait pertinent d'enrichir via un scraping systématique de Wikipedia et des rapports OSHA pour une analyse plus exhaustive.

---

## Auteur

**Philippe Kirstetter-Fender**
Projet personnel — Data Analyst / Data Engineer

En recherche active d'un poste de Data Engineer en France et à l'étranger.