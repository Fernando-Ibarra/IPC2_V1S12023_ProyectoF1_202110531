class MovieRoom(object):
        
    def __init__(self, number: str, seats: int) -> None:
        self.number = number
        self.seats = seats
        
    def show( self, index: int ):
        print(f"{ index }  Numero { self.number }  Asientos { self.seats }")