# 🎬 Movie Recommendation System

![App UI](https://github.com/Vineetg2003/Movie_Recommendation_Model/blob/master/image.png)

A smart **content-based movie recommendation system** built using **Scikit-learn**, **TF-IDF**, and **Streamlit**. It recommends movies based on **genre**, **cast**, **keywords**, **tagline**, and **director** — trained on a dataset of **4,761 movies**.

---

## 🚀 Features

- ✅ Content-based movie recommendations using TF-IDF + cosine similarity
- 🎯 Based on genre, cast, tagline, keywords, and director
- 🖥️ Modern dark-mode UI with animated movie cards
- 💡 Real-time interaction with Streamlit
- 📦 Modular structure: easy to extend and maintain
---

## 📁 Project Structure

```text
Movie_Recommendation_Model/
├── app.py
├── recommender.py
├── data/
│   └── Movies Recommendation.csv
├── assets/
│   └── image.png
└── README.md
```

---

## 🧠 Tech Stack

- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)

---

## 🔧 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Movie_Recommendation_Model.git
cd Movie_Recommendation_Model
pip install streamlit pandas scikit-learn
streamlit run app.py
```

### 📝 Dataset
- Location: data/Movies Recommendation.csv
- 📊 Contains 4,761 movies
- 🔹 Columns:

Movie_Title, Movie_Genre, Movie_Tagline, Movie_Keywords, Movie_Director, Movie_Cast, etc.

- Note: Movie_Title is renamed internally to Movie_Name.

### 💡 Future Enhancements

- ✅ Integrate TMDB API for posters
- ✅ Add filters by genre, language, year
- ✅ Keyword-based search
- ✅ Option to download recommendations
- ✅ Deploy on Streamlit Cloud / Hugging Face Spaces
