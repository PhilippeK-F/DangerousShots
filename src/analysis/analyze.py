import pandas as pd


def summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Statistiques descriptives sur les colonnes numériques."""
    return df[["annee", "budget_million_usd"]].describe()


def aggregate(df: pd.DataFrame) -> pd.DataFrame:
    """Incidents par année."""
    return (
        df.groupby("annee")
        .agg(nb_incidents=("film", "count"), nb_deces=("deces", "sum"))
        .reset_index()
    )


def compute_kpis(df: pd.DataFrame) -> dict:
    """KPIs principaux du dashboard DangerousShots."""
    return {
        "🎬 Incidents totaux": len(df),
        "💀 Décès": int(df["deces"].sum()),
        "🤕 Blessures": int((~df["deces"]).sum()),
        "💰 Budget moyen (M$)": f"{df['budget_million_usd'].mean():.0f}M",
    }


def incidents_par_genre(df: pd.DataFrame) -> pd.DataFrame:
    """Nombre d'incidents par genre simplifié."""
    return (
        df.groupby("genre_simplifie")
        .agg(nb_incidents=("film", "count"), nb_deces=("deces", "sum"))
        .reset_index()
        .sort_values("nb_incidents", ascending=False)
    )


def incidents_par_categorie_victime(df: pd.DataFrame) -> pd.DataFrame:
    """Incidents par catégorie de victime (Acteur / Technicien)."""
    return (
        df.groupby("categorie_victime")
        .agg(nb_incidents=("film", "count"), nb_deces=("deces", "sum"))
        .reset_index()
    )


def incidents_par_type_accident(df: pd.DataFrame) -> pd.DataFrame:
    """Top types d'accidents."""
    return (
        df.groupby("type_accident")
        .agg(nb_incidents=("film", "count"))
        .reset_index()
        .sort_values("nb_incidents", ascending=False)
    )


def incidents_par_tranche_budget(df: pd.DataFrame) -> pd.DataFrame:
    """Incidents par tranche de budget."""
    return (
        df.groupby("tranche_budget", observed=True)
        .agg(nb_incidents=("film", "count"), nb_deces=("deces", "sum"))
        .reset_index()
    )


def incidents_par_annee(df: pd.DataFrame) -> pd.DataFrame:
    """Évolution annuelle des incidents."""
    return (
        df.groupby("annee")
        .agg(nb_incidents=("film", "count"), nb_deces=("deces", "sum"))
        .reset_index()
        .sort_values("annee")
    )