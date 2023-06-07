class User:
    """ This is a constructor of user's clss
    """
    def __init__(self, name: str, lastName: str, phoneNUmber: str, email: str, password: str, rol: str, id: int) -> None:
        self.rol = rol
        self.name = name
        self.lastName = lastName
        self.phoneNUmber = phoneNUmber
        self.email = email
        self.password = password
        self.id = id
    
    def show(self):
        print(f" id: { self.id } Name: { self.name } ")
