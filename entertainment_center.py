import fresh_tomatoes
import media

# Creating instances of the movie class for the
# movies that will be displayed on the movie website

lotr_two_towers = media.Movie("Lord of the Rings: The Two Towers",
	"While Frodo and Sam edge closer to Mordor with the help of the"
	"shifty Gollum, the divided fellowship makes a stand against"
	"Sauron's new ally, Saruman, and his hordes of Isengard.",
	"https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg", #noqa
	"https://www.youtube.com/watch?v=LbfMDwc4azU")

good_will_hunting = media.Movie("Good Will Hunting",
	"Will Hunting, a janitor at M.I.T., has a gift for mathematics, but"
	"needs help from a psychologist to find direction in his life.",
	"https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg", #noqa
	"https://www.youtube.com/watch?v=PaZVjZEFkRs")

grave_of_the_fireflies = media.Movie("Grave of the Fireflies",
	"In the aftermath of a World War II bombing, two orphaned children"
	"struggle to survive in the Japanese countryside",
	"https://upload.wikimedia.org/wikipedia/en/a/a5/Grave_of_the_Fireflies_Japanese_poster.jpg", #noqa
	"https://www.youtube.com/watch?v=4vPeTSRd580")

you_are_the_apple_of_my_eye = media.Movie("You are the Apple of my Eye",
	"Those years, the girl we went after together",
	"https://upload.wikimedia.org/wikipedia/en/a/aa/You_Are_the_Apple_of_My_Eye_film_poster.jpg", #noqa
	"https://www.youtube.com/watch?v=v5H6wE47FrI")
		
pulp_fiction = media.Movie("Pulp Fiction",
	"The lives of two mob hit men, a boxer, a gangster's wife, and a"
	"pair of diner bandits intertwine in four tales of violence"
	"and redemption.",
	"https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg", #noqa
	"https://www.youtube.com/watch?v=s7EdQ4FqbhY")

wreck_it_ralph = media.Movie("Wreck it Ralph",
	"A video game villain wants to be a hero and sets out to fulfill"
	"his dream, but his quest brings havoc to the whole arcade"
	"where he lives.",
	"https://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg", #noqa
	"https://www.youtube.com/watch?v=87E6N7ToCxs")

the_incredibles = media.Movie("The Incredibles",
	"A family of undercover superheroes, while trying to live the"
	"quiet suburban life, are forced into action to save the world.",
	"https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
	"https://www.youtube.com/watch?v=eZbzbC9285I")

# Append each of the movie instances into a list
movies = [lotr_two_towers, good_will_hunting, grave_of_the_fireflies,
you_are_the_apple_of_my_eye, pulp_fiction, wreck_it_ralph,
the_incredibles]

# Call the function which will render the movies on the webpage
fresh_tomatoes.open_movies_page(movies)
