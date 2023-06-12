from Model.movie.LinkedListMovie import LinkedListMovie

class Category:
    def __init__(self, name: str, movies: LinkedListMovie ) -> None:
        self.name = name
        self.movies = movies