# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, data_path: str):
        self.data = pd.read_csv(data_path)
        self.data.columns = self.data.columns.str.strip()

        # Normalize to Movie_Name internally
        if 'Movie_Title' in self.data.columns:
            self.data.rename(columns={'Movie_Title': 'Movie_Name'}, inplace=True)

        self.data.fillna('', inplace=True)
        self._prepare_model()

    def _prepare_model(self):
        self.data['combined_features'] = (
            self.data['Movie_Genre'] + ' ' +
            self.data['Movie_Tagline'] + ' ' +
            self.data['Movie_Keywords'] + ' ' +
            self.data['Movie_Director'] + ' ' +
            self.data['Movie_Cast']
        )

        vectorizer = TfidfVectorizer(stop_words='english')
        self.feature_matrix = vectorizer.fit_transform(self.data['combined_features'])
        self.similarity_matrix = cosine_similarity(self.feature_matrix)

    def recommend(self, movie_title: str, top_n: int = 6):
        if movie_title not in self.data['Movie_Name'].values:
            return []
        idx = self.data[self.data['Movie_Name'] == movie_title].index[0]
        similarity_scores = list(enumerate(self.similarity_matrix[idx]))
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        recommended_titles = [self.data.iloc[i[0]]['Movie_Name'] for i in sorted_scores]
        return recommended_titles
