def create_combined_feature(movies_df):
    movies_df['combined_features'] = movies_df['overview'].fillna('') + ' ' + \
                                      movies_df['genres'].fillna('') + ' ' + \
                                      movies_df['keywords'].fillna('')
    return movies_df

def extract_keywords(movies_df):
    # Assuming keywords are in a JSON-like string format
    movies_df['keywords'] = movies_df['keywords'].apply(lambda x: eval(x) if isinstance(x, str) else [])
    return movies_df

def create_feature_matrix(movies_df):
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['combined_features'])
    
    return tfidf_matrix, tfidf_vectorizer