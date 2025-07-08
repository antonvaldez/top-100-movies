# 🎬 Empire's Top Movies Scraper

This is a Python script that scrapes movie titles from [Empire's 100 Greatest Movies](https://www.empireonline.com/movies/features/best-movies-2/) list and saves them into a `.txt` file.

## 📌 Features
- Scrapes all movie titles from the Empire Online page
- Reverses the order so the list starts from #1
- Saves the titles to a `movie.txt` file (overwrites the file on each run)

## 🛠 Requirements
- Python 3
- `requests` and `beautifulsoup4` libraries

Install them with:
```bash
pip install requests beautifulsoup4
