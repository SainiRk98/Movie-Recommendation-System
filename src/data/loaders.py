import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

def load_movies():
    """Load TMDB movies dataset"""
    path = BASE_DIR / "data/raw/tmdb_5000_movies.csv"
    return pd.read_csv(path)

def load_ratings():
    """Load ratings dataset"""
    path = BASE_DIR / "data/raw/ratings.csv"
    return pd.read_csv(path)

def load_data():
    movies = load_movies()
    ratings = load_ratings()
    return movies, ratings
