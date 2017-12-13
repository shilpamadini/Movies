import webbrowser

class Movie():
    """ This class provides a blueprint to store movies information"""
    VALID_RATINGS = ['G','PG','PG-13','R']
    def __init__(self,movie_title,story,image,trailor):
        self.title = movie_title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailor

    def show_trailor(self):
        webbrowser.open(self.youtube_url)
