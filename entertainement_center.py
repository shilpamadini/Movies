import fresh_tomatoes
import media

#Creating multiple instances of the class Movie
sweet_home_alabama = media.Movie("Sweet Home Alabama","Romantic comedy of a small town girl from Alabama","https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Sweet_Home_Alabama_film.jpg/220px-Sweet_Home_Alabama_film.jpg","https://www.youtube.com/watch?v=BM89EgWx_Gs")
beautiful_mind = media.Movie("A Beautiful Mind"," An American Biographical film based on the life of John Nash, a Nobel Laureate in economics","https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/A_Beautiful_Mind_Poster.jpg/220px-A_Beautiful_Mind_Poster.jpg","https://www.youtube.com/watch?v=YWwAOutgWBQ")
gladiator = media.Movie("Gladiator","Story of an army general who becomes gladiator by fate","https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg","https://www.youtube.com/watch?v=Q-b7B8tOAQU")
good_will_hunting = media.Movie("Good Will Hunting","Story of a janitor at MIT who has a genius level IQ","https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Good_Will_Hunting_theatrical_poster.jpg/220px-Good_Will_Hunting_theatrical_poster.jpg","https://www.youtube.com/watch?v=PaZVjZEFkRs")
spy_game = media.Movie("Spy Game","Story of an american spy","https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Spy_Game_poster.jpg/220px-Spy_Game_poster.jpg","https://www.youtube.com/watch?v=EH30237stWM")
bone_collector = media.Movie("The Bone Collector","Story of Tetraplegic forensics expert and a patrol cop","https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Bone_collector_poster.jpg/220px-Bone_collector_poster.jpg","https://www.youtube.com/watch?v=w4z4Xsp-bos")

#Create a list of movie instances
movies = [sweet_home_alabama,beautiful_mind,gladiator,good_will_hunting,spy_game,bone_collector]

# Pass the list of movie instances to open movie page function
fresh_tomatoes.open_movies_page(movies)

