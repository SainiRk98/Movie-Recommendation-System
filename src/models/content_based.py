import ast
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self, movies_df: pd.DataFrame):
        self.movies = self._prepare(movies_df)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.vectors = self.vectorizer.fit_transform(self.movies["content"])
        self.similarity = cosine_similarity(self.vectors)

    def _extract_names(self, item):
        if pd.isna(item):
            return ""
        s = str(item).strip()
        try:
            parsed = ast.literal_eval(s)
            if isinstance(parsed, list):
                return " ".join(
                    v.get("name", "") if isinstance(v, dict) else str(v)
                    for v in parsed
                )
        except Exception:
            pass
        return s.replace(",", " ")

    def _prepare(self, df: pd.DataFrame):
        cols = [c for c in ["title", "overview", "genres", "keywords"] if c in df.columns]
        df = df[cols].copy().fillna("")

        if "genres" in df:
            df["genres"] = df["genres"].apply(self._extract_names)
        if "keywords" in df:
            df["keywords"] = df["keywords"].apply(self._extract_names)

        df["content"] = (
            df.get("overview", "")
            + " "
            + df.get("genres", "")
            + " "
            + df.get("keywords", "")
        )

        return df.reset_index(drop=True)

    def recommend(self, title: str, n: int = 5):
        title_lower = title.lower()
        mask = self.movies["title"].str.lower() == title_lower
        if not mask.any():
            return []

        idx = mask.idxmax()
        scores = sorted(
            enumerate(self.similarity[idx]),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            self.movies.iloc[i]["title"]
            for i, _ in scores[1 : n + 1]
        ]
