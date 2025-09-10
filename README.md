# 🎬 100 Movies to Watch — Web Scraper

## 📖 Objective
This project scrapes the **Top 100 Movies of All Time** from the Empire Online archive and generates a text file (`movies.txt`) containing the titles in **ascending order** (starting from 1).

Example output:
```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
... and so on
```

The goal of this project is to practice **web scraping with BeautifulSoup** in Python.

---

## ⚙️ How It Works
1. Send a request to the archived Empire Online page using `requests`.
2. Parse the HTML with **BeautifulSoup**.
3. Extract the movie titles from `<h3>` tags with class `title`.
4. Reverse the list (since the site listed them from 100 → 1).
5. Save the results into `movies.txt`.

---

## 🚀 How to Run
### 1. Clone this repo
```bash
git clone https://github.com/<your-username>/100-movies-to-watch.git
cd 100-movies-to-watch
```

### 2. Create and activate a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the script
```bash
python main.py
```

### 5. Check the output
The results will be saved to a file called **`movie.txt`** in the project folder.

---

## 🌐 Important Note
Since websites change frequently, use the **Internet Archive link** below to ensure consistent results:
```
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
```
*(Do **not** use the live Empire Online URL, as it may differ.)*

---

## 📂 Files in This Project
- `main.py` → Python script for scraping.
- `README.md` → Project instructions & documentation.
- `movie.txt` → Output file with the 100 movie titles.

---

## 📚 Skills Practiced
- Web scraping with **BeautifulSoup**
- Working with **requests**
- Writing to files in Python
- Data parsing and text processing

---

✨ Built as part of Angela Yu’s **100 Days of Code: Python Pro Bootcamp**
