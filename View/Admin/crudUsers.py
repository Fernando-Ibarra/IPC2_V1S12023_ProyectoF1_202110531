from inquirer import List, prompt
from inquirer.themes import BlueComposure
import os

from Model.user.User import User
import View.Admin.Users.userTool as userMenu
import View.Admin.MainMenu as mainMenu

choices = [
    "Crear Usuario",
    "Listar Usuarios",
    "Modificar Usuario",
    "Eliminar Usuario",
    "Importar XML",
    "Expotar XML",
    "Salir"
]

def toCrud( optionSelected: str = "Crear Usuario", user: User = None  ):
    if ( optionSelected == choices[0] ):
        userMenu.createUser( user )
    elif ( optionSelected == choices[1] ):
        userMenu.showUsers( user )
    elif ( optionSelected == choices[2] ):
        userMenu.modifyUser( user )
    elif ( optionSelected == choices[3] ):
        userMenu.deleteUser( user )
    elif ( optionSelected == choices[4] ):
        userMenu.importXML( user )
    elif ( optionSelected == choices[5] ):
        print("Expotar XML")
    else:
        mainMenu.MainMenu( user )

def mainCrudUser( user: User ):
    os.system('cls')
    questions = [
        List(
            name="firstOption",
            message="¿Qué deseas hacer?", 
            choices=choices,
            default=choices[0],
        ),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    optionSelected: str = answers["firstOption"] # type: ignore
    toCrud( optionSelected, user )