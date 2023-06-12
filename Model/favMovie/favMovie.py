from Model.movie.Movie import Movie
from Model.user.User import User

class favMovie(object):
    
    def __init__(self, user: User, movie: Movie) -> None:
        self.user = user
        self.movie = movie