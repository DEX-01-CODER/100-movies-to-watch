import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

movie_title_info_list = soup.find_all(name="h3", class_="title")

movie_title = [tag.get_text() for tag in movie_title_info_list]

movie_title.reverse()
movies = movie_title

with open("movie.txt", 'w') as file:
    for name in movies:
        file.write(f"{name}\n")



