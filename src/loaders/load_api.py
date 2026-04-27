import os

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

# TODO: remplacer par l'URL de ton API
API_URL = os.getenv("API_URL", "https://ton-api.example.com/endpoint")
API_KEY = os.getenv("API_KEY", "")


def load_api(url: str = API_URL, params: dict = None) -> pd.DataFrame:
    """
    Récupère des données depuis une API REST et retourne un DataFrame.

    TODO: adapter selon l'API
    - Ajouter les headers d'authentification si nécessaire
    - Gérer la pagination si l'API renvoie des pages
    - Adapter la clé d'extraction du JSON (ici "data", peut être "results", "items", etc.)

    Exemple avec auth par header :
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(url, headers=headers, params=params, timeout=20)

    Exemple avec pagination :
        all_data = []
        page = 1
        while True:
            r = requests.get(url, params={"page": page, **params}, timeout=20)
            batch = r.json().get("data", [])
            if not batch:
                break
            all_data.extend(batch)
            page += 1
        return pd.DataFrame(all_data)
    """
    headers = {}
    if API_KEY:
        # TODO: adapter le nom du header selon l'API (Bearer, X-Api-Key, etc.)
        headers["Authorization"] = f"Bearer {API_KEY}"

    response = requests.get(url, headers=headers, params=params or {}, timeout=20)
    response.raise_for_status()

    payload = response.json()

    # TODO: adapter la clé selon la structure JSON de ton API
    # Exemples : payload["data"], payload["results"], payload (si directement une liste)
    data = payload.get("data", payload)

    return pd.DataFrame(data)
