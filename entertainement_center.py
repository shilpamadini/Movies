import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","The story of a boy and his toys that come alive.","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar"," The story of Aliens.","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print( avatar.storyline)
#avatar.show_trailor()

#sweet_home_alabama = media.Movie("Sweet Home Alabama","Romantic comedy of a small town girl from Alabama","https://en.wikipedia.org/wiki/File:Sweet_Home_Alabama_film.jpg","https://www.youtube.com/watch?v=BM89EgWx_Gs")
#sweet_home_alabama.show_trailor()

school_of_rock = media.Movie("School of Rock"," Using rock music to learn","https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouille = media.Movie("Ratatouille","A rat is a checf in Paris","https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie(" Midnight in Paris","Going back in time to meet the authors","https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games","A really real reality show","https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://www.youtube.com/watch?v=FovFG3N_RSU")

movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]

#fresh_tomatoes.open_movies_page(movies)

# print class variable
#print(media.Movie.VALID_RATINGS)

# print predefined class variables
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)