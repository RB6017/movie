import media
import json
from pprint import pprint
import fresh_tomatoes

if __name__ == "__main__":

    # Instantiate a factory class to build a list of movie objects
    mb = media.MovieBuilder()
    # MovieBuilder has access to a json file with the values necessary to
    # build the movie objects
    movie_list = mb.get_list_of_movies()
    # Dynamically generate html content using fresh_tomatoes.py
    fresh_tomatoes.open_movies_page(movie_list)

