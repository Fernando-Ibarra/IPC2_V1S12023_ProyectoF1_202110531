from .Theater import Theater

from Model.movieRoom.DoubleLinkedListMovieRoom import DoubleLinkedListMovieRoom

class NodeTheater(object):
    
    listMovieRoom: DoubleLinkedListMovieRoom = None # type: ignore
    
    def __init__(self, theater: Theater, next=None, prev=None) -> None:
        self.theater = theater
        self.next = next
        self.prev = prev