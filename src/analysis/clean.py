import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage du dataset DangerousShots — accidents et décès sur tournages.
    """
    # Noms de colonnes en minuscules sans espaces
    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]

    # Suppression des doublons
    df = df.drop_duplicates()

    # Suppression des lignes entièrement vides
    df = df.dropna(how="all")

    # Types corrects
    df["annee"] = pd.to_numeric(df["annee"], errors="coerce").astype("Int64")
    df["budget_million_usd"] = pd.to_numeric(df["budget_million_usd"], errors="coerce")
    df["deces"] = df["deces"].astype(bool)

    # Nettoyage texte
    for col in ["film", "pays", "genre", "victime", "role", "type_accident", "studio"]:
        if col in df.columns:
            df[col] = df[col].str.strip()

    # Gravité
    df["gravite"] = df["deces"].apply(lambda x: "Décès" if x else "Blessure")

    # Tranche budget
    df["tranche_budget"] = pd.cut(
        df["budget_million_usd"],
        bins=[0, 20, 50, 100, 200, 9999],
        labels=["Très petit (<20M)", "Petit (20-50M)", "Moyen (50-100M)",
                "Grand (100-200M)", "Blockbuster (>200M)"]
    )

    # Décennie
    df["decennie"] = df["annee"].apply(
        lambda x: "2000s" if x < 2010 else ("2010s" if x < 2020 else "2020s")
    )

    # Genre simplifié
    def simplify_genre(g):
        if any(k in str(g) for k in ["Action", "Aventure", "Western"]):
            return "Action/Aventure"
        elif any(k in str(g) for k in ["Super-héros", "SF"]):
            return "SF/Super-héros"
        elif "Horreur" in str(g):
            return "Horreur"
        elif any(k in str(g) for k in ["Drame", "Biopic", "Historique"]):
            return "Drame"
        return "Autre"

    df["genre_simplifie"] = df["genre"].apply(simplify_genre)

    return df