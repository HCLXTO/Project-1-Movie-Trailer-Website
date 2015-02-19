import webbrowser#used to open the browser on Movie.show_trailer

class Movie(object):#class used to represent each movie on the website
	"""Documentation for the class Movie
	It represents movies!"""# using triple quotes we can make multiple lines strings and placing it like this i will be available when Movie.__doc__ be called
	VALID_RATINGS = ["G","PG","PG-13","R"]#this is a class variable and every instance of this class will have the same value for it (as it act as a constant the style convention says to use capital letter to name it)
	
	def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, actors, director):#constructor of the Movie class
		"""Doc for __init__:
			variables: title, storyline, poster_image_url, trailer_youtube_url"""
		#define the object's properties
		self.title = title#hold the movie title
		self.storyline = storyline#hold it's story line
		self.poster_image_url = poster_image_url#holds a link to the movie's poster image
		self.trailer_youtube_url = trailer_youtube_url#hold a link to the movie's trailer on youtube
		self.actors =  actors#hold the main actors
		self.director = director#The director's name
	
	#methods
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)