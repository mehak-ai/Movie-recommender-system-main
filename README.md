# 🎬 Movie Recommender System

A **content-based movie recommendation system** built using **Python** and **Streamlit**.
The app recommends similar movies based on cosine similarity and displays movie posters using the **TMDB API**.

🔗 **Live App:**
[https://movie-recommender-system-main-9edcwkajtrp3tdqor9xuhf.streamlit.app/](https://movie-recommender-system-main-9edcwkajtrp3tdqor9xuhf.streamlit.app/)

---

## 📌 Description

This project allows users to select a movie and get the **top 5 recommended movies** that are similar in content.
It uses a **precomputed similarity matrix** and movie metadata stored in pickle files to generate fast recommendations.

---

## 🚀 Features

* **Content-Based Filtering:** Recommends movies based on metadata tags and genres.
* **Cosine Similarity:** Matches movies based on vector distance.
* **Real-time Posters:** Fetches high-quality movie posters dynamically using the TMDB API.
* **Interactive UI:** Clean and simple interface built with Streamlit.
* **Cloud Deployment:** Fully deployed and accessible via Streamlit Cloud.

---

## 🧠 How It Works

1.  **Data Loading:** The system loads movie data and the similarity matrix from `.pkl` files.
2.  **User Input:** The user selects a preferred movie from the dropdown menu.
3.  **Processing:** The system looks up the index of the movie and finds the 5 nearest vectors in the similarity matrix.
4.  **Fetching Assets:** The system uses the Movie IDs to fetch poster URLs from the TMDB API.
5.  **Output:** Titles and posters are rendered on the frontend.

---

## 📂 Project Structure

```text
Movie-recommender-system-main/
├── app.py                # Main application logic
├── simi.pkl              # Precomputed similarity matrix (Large File)
├── moviesdict.pkl        # Movie metadata dictionary
├── requirements.txt      # Python dependencies
├── .gitattributes        # Git LFS configuration
├── .gitignore            # Files to ignore
└── README.md             # Project documentation

```


Just tell me 👍
```
