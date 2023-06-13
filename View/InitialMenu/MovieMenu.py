import os
from inquirer import List, prompt
from inquirer.themes import BlueComposure

from View.Admin.Categories.categoryTools import showMoviesMainMenu, showAllMovies
import View.InitialMenu.MainMenu as mainMenu

def __init__( self ):
    pass

def validMenu( optionSelected: str = "Por Categoria" ):
    if ( optionSelected == "Por Categoria" ):
        showMoviesMainMenu()
    elif ( optionSelected == "Listado General" ):
        showAllMovies()
    else:
        mainMenu.mainMenu()

def movieMenu():
    os.system('cls')
    questions = [
        List(
            name="firstOption",
            message="¿Qué deseas hacer hoy?", 
            choices=[
                "Por Categoria",
                "Listado General",
                "Volver"
            ],
            
        ),
    ]

    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    optionSelected: str = answers["firstOption"] # type: ignore
    validMenu( optionSelected )
