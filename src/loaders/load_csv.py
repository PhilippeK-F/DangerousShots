import pandas as pd


def load_csv(filepath: str = "../data/processed/accidents_clean.csv", **kwargs) -> pd.DataFrame:
    """
    Charge le dataset accidents/décès de tournage en DataFrame.

    Colonnes attendues :
        annee, film, pays, genre, budget_million_usd, type_production,
        victime, role, categorie_victime, type_accident, deces, cause,
        pays_tournage, studio, gravite, tranche_budget, decennie,
        genre_simplifie, ratio_budget_risque
    """
    df = pd.read_csv(filepath, encoding="utf-8-sig", **kwargs)
    return df
