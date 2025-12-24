import streamlit as st
import pickle
import pandas as pd
import requests
import os

# ---------- PATH SETUP ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

simi_path = os.path.join(BASE_DIR, 'simi.pkl')
movies_dict_path = os.path.join(BASE_DIR, 'moviesdict.pkl')

# ---------- LOAD FILES ----------
similarity = pickle.load(open(simi_path, 'rb'))
movies_dict = pickle.load(open(movies_dict_path, 'rb'))

movies = pd.DataFrame(movies_dict)

# ---------- TMDB POSTER ----------
def fetch_poster(movie_id):
    api_key = "5bf271582f232c240d2a6ffc4461142d"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get('poster_path'):
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    
    return "https://via.placeholder.com/500x750.png?text=No+Image"

# ---------- RECOMMENDER ----------
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ---------- STREAMLIT UI ----------
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    if not names:
        st.error("❌ Sorry, no recommendations found.")
    else:
        cols = st.columns(len(names))
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.text(name)
                st.image(poster)
