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

## 🛠 Technologies Used

1.  **Data Loading:** The system loads movie data and the similarity matrix from `.pkl` files.
2.  **Frontend:** Streamlit
3.  **Data Manipulation:** Pandas, NumPy
4.  **Machine Learning:** Scikit-learn (Cosine Similarity)
5.  **API:** The Movie Database (TMDB) API
6.  **Version Control:** Git & Git LFS
   
---

## 📦 Installation

**1️⃣ Clone the repository**
   ```text
git clone [https://github.com/mehak-ai/Movie-recommender-system-main.git](https://github.com/mehak-ai/Movie-recommender-system-main.git)
cd Movie-recommender-system-main
```

**2️⃣ Install dependencies**
   ```text
pip install -r requirements.txt
```

**3️⃣ Configure Large Files (Important)**
   This project uses Git LFS for the .pkl files. If the files are small pointers after cloning, run:
```text
git lfs pull
```

**4️⃣ Run the app**
  ```text
streamlit run app.py
```
The app should open automatically in your browser at http://localhost:8501.

---

## 🔑 TMDB API Setup

To fetch posters, you need a TMDB API Key.

1. Create an account at TheMovieDB.org.
2. Navigate to Settings -> API to generate your key.
3. For local use, replace the key variable in app.py or use environment variables.
4. For Streamlit Cloud, add your key to the "Secrets" management:
   
   ```text
   TMDB_API_KEY = "your_api_key_here"
   ```
   
---


