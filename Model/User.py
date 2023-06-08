class User(object):
    """ This is a constructor of user's clss
    """
    def __init__(self, name: str, lastName: str, phoneNUmber: str, email: str, password: str, rol: str) -> None:
        self.rol = rol
        self.name = name
        self.lastName = lastName
        self.phoneNUmber = phoneNUmber
        self.email = email
        self.password = password
    
    def show(self):
        print(f"email: { self.email } ")
        print(f"password: { self.password } ")
