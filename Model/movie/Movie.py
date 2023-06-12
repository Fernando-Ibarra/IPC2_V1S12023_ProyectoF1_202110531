class Movie(object):
    
    def __init__(self, title: str, director: str, year: str, date: str, time: str ) -> None:
        self.title: str = title
        self.director: str = director
        self.year: str = year
        self.date: str = date
        self.time: str = time
        
    def show(self, index: int):
        print(f"{ index }    { self.title }    { self.director }    { self.year }     { self.date }      { self.time }")