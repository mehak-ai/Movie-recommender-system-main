Here is a **clean, copy-paste ready `README.md`** for your repository.
You can directly paste this into **README.md** on GitHub — no changes needed.

---

```markdown
# 🎬 Movie Recommender System

A **content-based movie recommendation system** built using **Python** and **Streamlit**.  
The app recommends similar movies based on cosine similarity and displays movie posters using the **TMDB API**.

🔗 **Live App:**  
https://movie-recommender-system-main-9edcwkajtrp3tdqor9xuhf.streamlit.app/

---

## 📌 Description

This project allows users to select a movie and get **top 5 recommended movies** that are similar in content.  
It uses a **precomputed similarity matrix** and movie metadata stored in pickle files for fast recommendations.

---

## 🚀 Features

- Content-based movie recommendations
- Cosine similarity for matching movies
- Movie posters fetched using TMDB API
- Interactive Streamlit UI
- Deployed on Streamlit Cloud

---

## 🧠 How It Works

1. Load movie data and similarity matrix from `.pkl` files  
2. User selects a movie from dropdown  
3. System finds most similar movies  
4. TMDB API fetches posters using movie IDs  
5. Results displayed with movie titles and posters  

---

## 📂 Project Structure

```

Movie-recommender-system-main/
├── app.py
├── simi.pkl
├── moviesdict.pkl
├── requirements.txt
├── .gitattributes
├── .gitignore
└── README.md

````

---

## 🛠 Technologies Used

- Python  
- Streamlit  
- Pandas & NumPy  
- Scikit-learn  
- TMDB API  
- Git LFS  

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mehak-ai/Movie-recommender-system-main.git
cd Movie-recommender-system-main
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## 📁 Large Files (Important)

This project uses **Git LFS** for large `.pkl` files.

If files don’t download automatically, run:

```bash
git lfs pull
```

---

## 🔑 TMDB API Key

Create a TMDB account and get your API key from:
[https://www.themoviedb.org/](https://www.themoviedb.org/)

For Streamlit Cloud, add this in **Secrets**:

```
TMDB_API_KEY = "your_api_key_here"
```

---

## 📌 Topics

```
movie-recommender-system
machine-learning
content-based-recommendation
streamlit
python
cosine-similarity
tmdb-api
```

---

## 📬 Author

**Mehak**
GitHub: [https://github.com/mehak-ai](https://github.com/mehak-ai)

---

⭐ If you like this project, don’t forget to star the repository!

```


Just tell me 👍
```
