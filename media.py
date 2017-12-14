import webbrowser


class Movie():
    """
    This class provides a blueprint to store movies information
    """
    # Declare the class variable to store valid movie ratings
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(
        self,
        movie_title,
        story,
        image,
        trailor
    ):

        """
        Constructor for the movie instances that initiate instance variables
        :param movie_title: string
        :param story: string
        :param image: string
        :param trailor: string
        """

        self.title = movie_title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailor

    def show_trailer(self):
        """
        Initialize instance for opening youtube video
        """
        webbrowser.open(self.trailer_youtube_url)
