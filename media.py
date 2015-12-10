class Movie:
    def __init__(self, movie_info):
        self.title = movie_info["title"]
        self.trailer_youtube_url = movie_info["trailer_url"]
        self.poster_image_url = movie_info["img_url"]

