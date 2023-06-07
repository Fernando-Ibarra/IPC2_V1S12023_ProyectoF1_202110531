from Model.User import User

class NodeUser:
    
    __slost__ = 'user', 'next'
        
    def __init__(self, user: User, next = None ) -> None:
        self.user = user
        self.next = next