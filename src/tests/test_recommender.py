import unittest
from src.models.collaborative import CollaborativeFiltering
from src.models.content_based import ContentBasedRecommendation

class TestRecommender(unittest.TestCase):

    def setUp(self):
        self.collab_model = CollaborativeFiltering()
        self.content_model = ContentBasedRecommendation()

    def test_collaborative_filtering(self):
        # Assuming we have a method to train and recommend
        self.collab_model.train()
        recommendations = self.collab_model.recommend(user_id=1)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

    def test_content_based_recommendation(self):
        # Assuming we have a method to recommend based on a movie
        recommendations = self.content_model.recommend(movie_id=1)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

if __name__ == '__main__':
    unittest.main()