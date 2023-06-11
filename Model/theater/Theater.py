from Model.movieRoom.DoubleLinkedListMovieRoom import DoubleLinkedListMovieRoom
class Theater(object):
    
    def __init__(self, nombre: str, rooms: DoubleLinkedListMovieRoom) -> None:
        self.nombre = nombre
        self.rooms = rooms
        
    def show( self, index: int ):
        print(f"{ index }  Nombre { self.nombre }")
        return None