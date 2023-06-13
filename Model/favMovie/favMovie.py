class favMovie(object):
    
    def __init__(self, name: str, lastName: str, email: str, title: str, director: str, year: str, date: str, time: str ) -> None:
        self.name = name
        self.lastName = lastName
        self.email = email
        self.title: str = title
        self.director: str = director
        self.year: str = year
        self.date: str = date
        self.time: str = time