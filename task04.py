class Movie:
    def __init__(self, title: str, genre: str, duration: int, rating: int):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
        
movie = Movie("Inception", "Action", 148, 8.8)

print("Title:", movie.title)
print("Genre:", movie.genre)
print("Duration:", movie.duration, "minutes")
print("Rating:", movie.rating)