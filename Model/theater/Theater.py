from Model.DoubleLinkedListMovieRoom import DoubleLinkedListMovieRoom

class Theater(object):
    
    def __init__(self, nombre: str, rooms: DoubleLinkedListMovieRoom) -> None:
        self.nombre = nombre
        self.rooms = rooms