import media
import json
from pprint import pprint

movie_list = []

with open('movie_info.json') as jsonfile:
    movie_info = json.load(jsonfile)

for title, info in movie_info.items():
    data = {}
    data["title"] = title
    data["trailer_url"] = info["youtube trailer"]
    data["img_url"] = info["poster image url"]
    movie = media.Movie(data)
    movie_list.append(movie)

print(movie_list)

# toy_story = media.Movie()
