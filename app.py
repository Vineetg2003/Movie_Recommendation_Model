# app.py

import streamlit as st
from recommender import MovieRecommender
import os

# ✅ MUST be the very first Streamlit command
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Load custom CSS (AFTER set_page_config)
def load_css():
    st.markdown("""
        <style>
            html, body, [class*="css"]  {
                font-family: 'Segoe UI', sans-serif;
                background-color: #f9f9f9;
            }
            .stButton button {
                background-color: #FF4B4B;
                color: white;
                font-weight: 600;
                border-radius: 12px;
                padding: 10px 20px;
                transition: 0.3s;
            }
            .stButton button:hover {
                background-color: #e63946;
                transform: scale(1.03);
            }
            .movie-card {
                background: linear-gradient(to right, #ffffff, #f0f0f0);
                padding: 20px;
                margin: 10px 0;
                border-radius: 16px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
                font-size: 16px;
                text-align: center;
                font-weight: 600;
            }
        </style>
    """, unsafe_allow_html=True)

# Load styles
load_css()

# Header
st.markdown("<h1 style='text-align:center;'>🎥 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("#### <p style='text-align:center;'>Find similar movies based on genre, director, cast, and keywords</p>", unsafe_allow_html=True)
st.markdown("---")

# Load model
DATA_PATH = "data/Movies Recommendation.csv"  # Make sure this path is correct
if not os.path.exists(DATA_PATH):
    st.error("❌ 'Movies Recommendation.csv' not found in the /data folder.")
else:
    recommender = MovieRecommender(DATA_PATH)

    # Movie dropdown
    movie_list = sorted(recommender.data['Movie_Name'].dropna().unique())
    selected_movie = st.selectbox("🎯 Select a Movie", ["-- Select --"] + movie_list)

    # Recommendations
    if selected_movie != "-- Select --" and st.button("✨ Get Recommendations"):
        results = recommender.recommend(selected_movie, top_n=6)

        if results:
            st.markdown("### 🎯 Top Recommendations")
            cols = st.columns(3)
            for i, movie in enumerate(results):
                with cols[i % 3]:
                    st.markdown(f"<div class='movie-card'>🎬 {movie}</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ No recommendations found. Try another title.")
