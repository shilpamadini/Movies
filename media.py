import webbrowser

class Movie():
    """ This class provides a blueprint to store movies information"""
    # Declare the class variable to store valid movie ratings
    VALID_RATINGS = ['G','PG','PG-13','R']
    def __init__(self,movie_title,story,image,trailor):
        """ Constructor for the movie instances that initiate instance variable
        movie_title,story,box image, youtube trailer video"""
        self.title = movie_title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailor
    # Function to that opens a web browser to show the youtube video
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
