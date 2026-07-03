import streamlit as st
import pickle
import pandas as pd
import requests

# 1. Set up the web page layout
st.set_page_config(page_title="Movie Recommender System", layout="wide") # Changed to wide for posters
st.title('🎬 Movie Recommender System')
st.write("Find your next favorite movie based on content similarity!")

# 2. Define your TMDB API Key
TMDB_API_KEY = "156a1cb7e1c6ec5abce9c1a48e35c569"

# Function to fetch movie poster using TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    try:
        response = requests.get(url)
        data = response.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except Exception:
        # Fallback placeholder image if API call fails or poster isn't found
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

# 3. Load the saved model data safely
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: Could not find model files. Make sure you ran the pickle cells in your notebook!")
    st.stop()

# 4. Dropdown selector for movies
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown:",
    movie_list
)

# 5. Recommendation Logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    recommended_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_posters

# 6. Display Recommendations with Posters in Columns
if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations and posters...'):
        names, posters = recommend(selected_movie)
        
        st.subheader(f"If you liked '{selected_movie}', you should try:")
        
        # Create 5 parallel layout columns for the 5 movies
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])