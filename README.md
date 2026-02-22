# Movie Recommendation System

This project is a Movie Recommendation System built using Python, Pandas, and Scikit-learn. The system provides movie recommendations based on user preferences and interactions.

## Project Structure

```
movie-recommender
├── src
│   ├── app.py
│   ├── data
│   │   ├── loaders.py
│   │   └── preprocessing.py
│   ├── models
│   │   ├── collaborative.py
│   │   └── content_based.py
│   ├── features
│   │   └── engineering.py
│   ├── utils
│   │   └── helpers.py
│   └── tests
│       └── test_recommender.py
├── notebooks
│   └── eda.ipynb
├── data
│   ├── raw
│   │   ├── movies.csv
│   │   └── ratings.csv
│   └── processed
│       └── interactions.csv
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd movie-recommender
pip install -r requirements.txt
```

## Usage

To run the movie recommendation system, execute the following command:

```bash
python src/app.py
```

Follow the prompts to receive movie recommendations based on your input.

## Features

- **Collaborative Filtering**: Generates recommendations based on user interactions and ratings.
- **Content-Based Filtering**: Provides recommendations based on movie attributes such as genres and keywords.
- **Exploratory Data Analysis**: Analyze the dataset using the provided Jupyter notebook.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.