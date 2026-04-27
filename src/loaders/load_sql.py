import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()


def get_engine():
    """
    Crée et retourne un engine SQLAlchemy.

    TODO: choisir le bon driver selon ta base
    - PostgreSQL → postgresql+psycopg://user:password@host:port/db
    - MySQL      → mysql+mysqlconnector://user:password@host:port/db
    - SQLite     → sqlite:///chemin/vers/fichier.db
    """
    db_url = (
        f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}"
        f"/{os.getenv('DB_NAME')}"
    )
    return create_engine(db_url, pool_pre_ping=True)


def load_sql(query: str, engine=None) -> pd.DataFrame:
    """
    Exécute une requête SQL et retourne un DataFrame.

    TODO: remplacer la requête par ta vraie requête
    Exemple :
        df = load_sql("SELECT * FROM ventes WHERE date >= '2024-01-01'")
        df = load_sql("SELECT p.nom, v.montant FROM produits p JOIN ventes v ON p.id = v.produit_id")
    """
    if engine is None:
        engine = get_engine()

    # TODO: remplacer par ta requête
    query = query or "SELECT * FROM ta_table LIMIT 100"

    return pd.read_sql(text(query), engine)
