import streamlit as st
import pickle
import pandas as pd
import requests 

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    api_key = "5bf271582f232c240d2a6ffc4461142d"
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5bf271582f232c240d2a6ffc4461142d'.format(movie_id))
    data = response.json()
    
    if 'poster_path' in data and data['poster_path']:  # Handle missing poster
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    
    return "https://via.placeholder.com/500x750.png?text=No+Image"

# Function to recommend movies based on similarity matrix
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []  # Handle case when movie is not found
    
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    # Sort movies based on similarity scores
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    recommended_posters = []
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_posters

# Load movie similarity matrix and movie data
similarity = pickle.load(open(r'C:\Users\Hp\Desktop\Movie-recommender-system-main\simi.pkl', 'rb'))
movies_dict = pickle.load(open(r'C:\Users\Hp\Desktop\Movie-recommender-system-main\moviesdict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    if not names:
        st.error("❌ Sorry, no recommendations found. Try a different movie.")
    else:
        cols = st.columns(len(names))  # Dynamically create columns based on number of recommendations
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.text(name)
                st.image(poster)
