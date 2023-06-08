from Model.MovieRoom import MovieRoom

class NodeMovieRoom(object):
    
    def __init__(self, movieRoom: MovieRoom, next=None, prev=None) -> None:
        self.movieRoom = movieRoom
        self.next = next
        self.prev = prev