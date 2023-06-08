from Model.User import User

def mainMenu(user: User):
    print("MENU CLIENTE")
    print(f"Bienvenido { user.name } { user.lastName }")