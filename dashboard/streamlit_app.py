import sys
sys.path.insert(0, '..')

import pandas as pd
import streamlit as st

from src.loaders.load_csv import load_csv
from src.analysis.clean import clean
from src.analysis.analyze import (
    compute_kpis,
    incidents_par_genre,
    incidents_par_categorie_victime,
    incidents_par_type_accident,
    incidents_par_tranche_budget,
    incidents_par_annee,
)
from src.analysis.visualize import (
    plot_gravite_par_genre,
    plot_evolution_annuelle,
    plot_type_accident,
    plot_budget_vs_gravite,
    plot_distribution,
    plot_note_imdb_par_genre,
    plot_boxoffice_vs_gravite,
    plot_roi_par_tranche_budget,
    plot_note_vs_budget,
)

st.set_page_config(
    page_title="DangerousShots",
    page_icon="🎬",
    layout="wide",
)

st.title("DangerousShots")
st.markdown("Analyse des accidents et décès sur tournages de films et séries TV (2004–2024)")

@st.cache_data
def load_data() -> pd.DataFrame:
    return load_csv("/app/data/processed/accidents_clean.csv")

df_raw = load_data()
df = clean(df_raw)

# ---------------------------------------------------------------------------
# Sidebar — filtres
# ---------------------------------------------------------------------------
st.sidebar.header("Filtres")

annees = sorted(df["annee"].dropna().unique().tolist())
selected_annees = st.sidebar.slider(
    "Période",
    min_value=int(min(annees)),
    max_value=int(max(annees)),
    value=(int(min(annees)), int(max(annees)))
)
df = df[(df["annee"] >= selected_annees[0]) & (df["annee"] <= selected_annees[1])]

genres = df["genre_simplifie"].dropna().unique().tolist()
selected_genres = st.sidebar.multiselect("Genre", options=genres, default=genres)
df = df[df["genre_simplifie"].isin(selected_genres)]

gravites = df["gravite"].dropna().unique().tolist()
selected_gravites = st.sidebar.multiselect("Gravité", options=gravites, default=gravites)
df = df[df["gravite"].isin(selected_gravites)]

categories = df["categorie_victime"].dropna().unique().tolist()
selected_categories = st.sidebar.multiselect("Catégorie victime", options=categories, default=categories)
df = df[df["categorie_victime"].isin(selected_categories)]

types_prod = df["type_production"].dropna().unique().tolist()
selected_types = st.sidebar.multiselect("Type de production", options=types_prod, default=types_prod)
df = df[df["type_production"].isin(selected_types)]

# ---------------------------------------------------------------------------
# KPIs
# ---------------------------------------------------------------------------
st.subheader("Indicateurs clés")
kpis = compute_kpis(df)
cols = st.columns(len(kpis))
for col, (label, value) in zip(cols, kpis.items()):
    col.metric(label=label, value=value)

st.divider()

# ---------------------------------------------------------------------------
# Onglets
# ---------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["Sécurité", "Production & Budget", "Données brutes"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Évolution annuelle des incidents")
        fig = plot_evolution_annuelle(incidents_par_annee(df))
        st.pyplot(fig)
    with col2:
        st.subheader("Incidents par genre")
        fig = plot_gravite_par_genre(df)
        st.pyplot(fig)

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Types d'accidents")
        fig = plot_type_accident(df)
        st.pyplot(fig)
    with col4:
        st.subheader("Budget vs gravité")
        fig = plot_budget_vs_gravite(df)
        st.pyplot(fig)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Note IMDb vs Budget")
        fig = plot_note_vs_budget(df)
        st.pyplot(fig)
    with col2:
        st.subheader("Note IMDb par genre")
        fig = plot_note_imdb_par_genre(df)
        st.pyplot(fig)

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Box-office moyen par gravité")
        fig = plot_boxoffice_vs_gravite(df)
        st.pyplot(fig)
    with col4:
        st.subheader("ROI par tranche de budget")
        fig = plot_roi_par_tranche_budget(df)
        st.pyplot(fig)

    st.subheader("Distribution des budgets")
    fig = plot_distribution(df, "budget_million_usd", "Distribution des budgets (M$)")
    st.pyplot(fig)

with tab3:
    cols_display = ["annee", "film", "genre_simplifie", "type_production",
                    "victime", "categorie_victime", "type_accident",
                    "gravite", "budget_million_usd", "box_office_million_usd",
                    "note_imdb", "roi", "pays_tournage"]
    st.dataframe(df[cols_display].sort_values("annee", ascending=False),
                 use_container_width=True)

    with st.expander("Voir toutes les colonnes"):
        st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Télécharger CSV", csv, "dangerous_shots_export.csv", "text/csv")