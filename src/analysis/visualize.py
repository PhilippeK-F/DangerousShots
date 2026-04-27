import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
PALETTE = {"Décès": "#e74c3c", "Blessure": "#f39c12"}


def plot_distribution(df: pd.DataFrame, column: str, title: str = None) -> plt.Figure:
    """Histogramme + courbe de densité pour une colonne numérique."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[column].dropna(), kde=True, ax=ax, color="#2c3e50")
    ax.set_title(title or f"Distribution — {column}")
    ax.set_xlabel(column)
    plt.tight_layout()
    return fig


def plot_bar(df: pd.DataFrame, x: str, y: str, title: str = None) -> plt.Figure:
    """Graphique en barres générique."""
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=df, x=x, y=y, ax=ax, color="#2c3e50")
    ax.set_title(title or f"{y} par {x}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return fig


def plot_timeseries(df: pd.DataFrame, date_col: str, value_col: str, title: str = None) -> plt.Figure:
    """Courbe temporelle."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df[date_col], df[value_col], marker="o", linewidth=2, color="#e74c3c")
    ax.set_title(title or f"{value_col} dans le temps")
    ax.set_xlabel(date_col)
    ax.set_ylabel(value_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def plot_correlation(df: pd.DataFrame, title: str = "Matrice de corrélation") -> plt.Figure:
    """Heatmap de corrélation."""
    fig, ax = plt.subplots(figsize=(8, 6))
    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title(title)
    plt.tight_layout()
    return fig


def plot_gravite_par_genre(df: pd.DataFrame) -> plt.Figure:
    """Incidents (décès vs blessures) par genre simplifié."""
    fig, ax = plt.subplots(figsize=(10, 5))
    agg = df.groupby(["genre_simplifie", "gravite"]).size().reset_index(name="count")
    sns.barplot(data=agg, x="genre_simplifie", y="count", hue="gravite",
                palette=PALETTE, ax=ax)
    ax.set_title("Incidents par genre — Décès vs Blessures")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Nombre d'incidents")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    return fig


def plot_evolution_annuelle(df_agg: pd.DataFrame) -> plt.Figure:
    """Évolution annuelle des incidents et décès."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(df_agg["annee"], df_agg["nb_incidents"], color="#2c3e50",
           alpha=0.7, label="Incidents")
    ax.bar(df_agg["annee"], df_agg["nb_deces"], color="#e74c3c",
           alpha=0.9, label="Décès")
    ax.set_title("Évolution annuelle des incidents sur tournage")
    ax.set_xlabel("Année")
    ax.set_ylabel("Nombre")
    ax.legend()
    plt.tight_layout()
    return fig


def plot_type_accident(df: pd.DataFrame) -> plt.Figure:
    """Top types d'accidents."""
    agg = df["type_accident"].value_counts().reset_index()
    agg.columns = ["type_accident", "count"]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=agg, y="type_accident", x="count", ax=ax, color="#e74c3c")
    ax.set_title("Répartition par type d'accident")
    ax.set_xlabel("Nombre d'incidents")
    ax.set_ylabel("")
    plt.tight_layout()
    return fig


def plot_budget_vs_gravite(df: pd.DataFrame) -> plt.Figure:
    """Scatter plot budget vs gravité."""
    fig, ax = plt.subplots(figsize=(10, 5))
    for gravite, color in PALETTE.items():
        subset = df[df["gravite"] == gravite]
        ax.scatter(subset["budget_million_usd"], [gravite] * len(subset),
                   color=color, s=100, alpha=0.7, label=gravite)
    ax.set_title("Budget du film vs Gravité de l'incident")
    ax.set_xlabel("Budget (M$)")
    ax.legend()
    plt.tight_layout()
    return fig


def plot_note_imdb_par_genre(df: pd.DataFrame) -> plt.Figure:
    """Note IMDb moyenne par genre simplifié."""
    agg = df.groupby("genre_simplifie")["note_imdb"].mean().reset_index()
    agg = agg.dropna().sort_values("note_imdb", ascending=False)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=agg, x="genre_simplifie", y="note_imdb", ax=ax, color="#2c3e50")
    ax.set_title("Note IMDb moyenne par genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Note IMDb")
    ax.set_ylim(0, 10)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    return fig


def plot_boxoffice_vs_gravite(df: pd.DataFrame) -> plt.Figure:
    """Box-office moyen selon la gravité de l'incident."""
    agg = df.groupby("gravite")["box_office_million_usd"].mean().reset_index().dropna()
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(data=agg, x="gravite", y="box_office_million_usd",
                palette={"Décès": "#e74c3c", "Blessure": "#f39c12"}, ax=ax)
    ax.set_title("Box-office moyen par gravité d'incident (M$)")
    ax.set_xlabel("")
    ax.set_ylabel("Box-office moyen (M$)")
    plt.tight_layout()
    return fig


def plot_roi_par_tranche_budget(df: pd.DataFrame) -> plt.Figure:
    """ROI moyen par tranche de budget."""
    agg = df.groupby("tranche_budget", observed=True)["roi"].mean().reset_index().dropna()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=agg, x="tranche_budget", y="roi", ax=ax, color="#27ae60")
    ax.set_title("ROI moyen par tranche de budget")
    ax.set_xlabel("Tranche de budget")
    ax.set_ylabel("ROI (box-office / budget)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    return fig


def plot_note_vs_budget(df: pd.DataFrame) -> plt.Figure:
    """Scatter plot note IMDb vs budget."""
    data = df.dropna(subset=["note_imdb", "budget_million_usd"])
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = data["gravite"].map({"Décès": "#e74c3c", "Blessure": "#f39c12"})
    ax.scatter(data["budget_million_usd"], data["note_imdb"],
               c=colors, s=80, alpha=0.8)
    ax.set_title("Note IMDb vs Budget — couleur par gravité")
    ax.set_xlabel("Budget (M$)")
    ax.set_ylabel("Note IMDb")
    from matplotlib.patches import Patch
    legend = [Patch(color="#e74c3c", label="Décès"), Patch(color="#f39c12", label="Blessure")]
    ax.legend(handles=legend)
    plt.tight_layout()
    return fig