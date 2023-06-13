from inquirer import List, prompt
from inquirer.themes import BlueComposure
import os

from Model.user.User import User
from View.Admin.crudUsers import mainCrudUser
import View.Admin.crudCategories as categories
from View.Admin.crudMovies import mainCrudMovies
from View.Admin.crudSoldTickets import mainCrudSoldTickets
import View.InitialMenu.MainMenu as MenuInitial 

choices = [
    "Gestionar Usuarios",
    "Gestionar Categorías y Películas",
    "Gestionar Cines y Salas",
    "Gestionar Boletos Comprados", 
    "Salir"
]

def validMenu( optionSelected: str = "Iniciar Sesión", user: User = None ): # type: ignore
    if ( optionSelected == choices[0] ):
        mainCrudUser( user )
    elif ( optionSelected == choices[1] ):
        categories.mainCrudCategories( user )
    elif ( optionSelected == choices[2] ):
        mainCrudMovies( user )
    elif ( optionSelected == choices[3] ):
        mainCrudSoldTickets()
    else:
        MenuInitial.mainMenu()

def MainMenu(user: User):
    os.system('cls')
    print(f"¡Bienvenido { user.name } { user.lastName }!")
    questions = [
        List(
            name="firstOption",
            message="¿Qué deseas hacer hoy?", 
            choices=choices,
            default=choices[0],
        ),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    optionSelected: str = answers["firstOption"] # type: ignore
    validMenu( optionSelected, user )