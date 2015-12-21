import json

class Movie:
    """
    Simple data model for storing the information required to populate
    the movie trailer html page
    """
    def __init__(self, movie_info):
        # Set some defaults, should the required movie_info not be provided
        self.title = movie_info.get("title", "Title not provided.")
        self.trailer_youtube_url = movie_info.get("trailer_url", 
                                                  "No trailer provided")
        self.poster_image_url = movie_info.get("img_url", "No trailer provided")

class MovieBuilder:
    """
    Simple factory class designed to encapsulate Movie 
    functionality and operation
    """
    def __init__(self):
        self._jsonfile = None
    
    @property
    def movie_info(self):
        if self._jsonfile is None:
            # take the json file and transform it into a python dictionary
            with open('movie_info.json') as jsonfile:
                self._jsonfile = json.load(jsonfile)
        # return an iterator over the key value pairs in the dictionary
        return self._jsonfile.items()

    def get_list_of_movies(self):
        movie_list = []
        # unpack the values in the dictionary and initialize the necessary
        # movie objects with the data
        for title, info in self.movie_info:
            movie = self.build_movie(title, info)
            movie_list.append(movie)
        return movie_list

    def build_movie(self, title, info):
        data = {}
        data["title"] = title
        data["trailer_url"] = info["youtube trailer"]
        data["img_url"] = info["poster image url"]
        movie = Movie(data)
        return movie
        
