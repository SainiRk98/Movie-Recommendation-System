from flask import Flask, request, jsonify, render_template
from data.loaders import load_movies
from models.content_based import ContentBasedRecommender

app = Flask(__name__)

movies = load_movies()
content_based_recommender = ContentBasedRecommender(movies)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "movie title required"}), 400

    recommendations = content_based_recommender.recommend(title, n=5)
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
