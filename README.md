<img width="1812" height="360" alt="Screenshot 2026-07-03 122610" src="https://github.com/user-attachments/assets/f678efab-206b-4436-9425-62dfe91d9ff6" />
# 🎬 CineMatch: Machine Learning Movie Recommender System

A content-based movie recommendation system built using Python and Machine Learning. The application analyzes movie metadata (genres, keywords, cast, crew, and overview) to calculate textual similarity and recommend the top 5 closest movies to a user's selection. 

The frontend interface is built with Streamlit and dynamically fetches real-time movie posters using **The Movie Database (TMDB) API**.

---

## 🚀 Features
* **Content-Based Filtering:** Analyzes tags using natural language processing (NLP) to find structural thematic matches.
* **Vector Space Modeling:** Uses Scikit-Learn's `CountVectorizer` and **Cosine Similarity** to mathematically compute vector distances between over 4,800 movies.
* **Dynamic Web UI:** Built with Streamlit for a fast, responsive, and interactive user experience.
* **Live Media Fetching:** Integrates TMDB API to pull official high-resolution movie posters on the fly.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (`CountVectorizer`, `cosine_similarity`)
* **Serialization:** Pickle
* **Web Framework:** Streamlit
* **API Integration:** Requests (TMDB API)

---

## 💻 Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd movie-recommender

## csv Data Source

The project utilizes the **TMDB 5000 Movie Dataset** from Kaggle, which consists of two main files:
* `tmdb_5000_movies.csv`: Contains metadata such as budget, genres, homepage, id, keywords, original_language, overview, popularity, production_companies, release_date, revenue, runtime, vote_average, and vote_count.
* `tmdb_5000_credits.csv`: Contains movie cast and crew details for all 4,800+ entries.

## 📸 Application Preview

| Main Interface | Dynamic Recommendations with Posters |
| :---: | :---: |
| ![Dropdown Selection](YOUR_IMAG<img width="1788" height="648" alt="Screenshot 2026-07-03 122634" src="https://github.com/user-attachments/assets/dc46ab5d-7c04-4047-99e4-1d48436af544" />
E_LINK_1) | ![Movie Poster Layout](YOUR_IMAGE<img width="1812" height="360" alt="Screenshot 2026-07-03 122610" src="https://github.com/user-attachments/assets/64a0e2d1-f3d0-4ac7-902c-84d976a30cdf" />
) |
