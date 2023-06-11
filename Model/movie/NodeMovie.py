from .Movie import Movie

class NodeMovie(object):
    
    __slost__ = 'user', 'next'
    
    def __init__(self, movie: Movie, next = None, prev = None ) -> None:
        self.movie = movie
        self.next = next
        self.prev = prev