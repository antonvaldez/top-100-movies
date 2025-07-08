import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movies = soup.select("h2 strong")

temp_movies_list = [movie.getText() for movie in movies]

movies_list = temp_movies_list[::-1]

with open("movie.txt", "w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")