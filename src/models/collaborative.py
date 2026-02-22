class CollaborativeRecommender:
    def __init__(self, ratings_df, movies_df):
        self.ratings_df = ratings_df
        self.movies_df = movies_df
        self.user_item_matrix = None

    def create_user_item_matrix(self):
        self.user_item_matrix = self.ratings_df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

    def calculate_similarity(self):
        from sklearn.metrics.pairwise import cosine_similarity
        return cosine_similarity(self.user_item_matrix)

    def get_recommendations(self, user_id, num_recommendations=5):
        if self.user_item_matrix is None:
            self.create_user_item_matrix()
        
        similarity_matrix = self.calculate_similarity()
        user_index = self.user_item_matrix.index.get_loc(user_id)
        similar_users = list(enumerate(similarity_matrix[user_index]))
        similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[1:]

        recommended_movies = {}
        for similar_user_index, similarity_score in similar_users:
            similar_user_id = self.user_item_matrix.index[similar_user_index]
            user_ratings = self.user_item_matrix.loc[similar_user_id]
            for movie_id, rating in user_ratings.items():
                if rating > 0 and movie_id not in recommended_movies:
                    recommended_movies[movie_id] = similarity_score * rating

        recommended_movies = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
        recommended_movie_ids = [movie[0] for movie in recommended_movies[:num_recommendations]]
        
        return self.movies_df[self.movies_df['movieId'].isin(recommended_movie_ids)]