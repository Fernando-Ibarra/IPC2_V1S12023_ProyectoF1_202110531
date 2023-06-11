from colorama import Fore

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
    
    def show(self, index: int):
        print(Fore.WHITE + f"{ index }      { self.name }    { self.lastName }    { self.phoneNUmber }     { self.email }      { self.rol }")
        