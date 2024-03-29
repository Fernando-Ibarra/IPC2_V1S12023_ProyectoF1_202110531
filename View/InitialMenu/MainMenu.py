import sys
import os
import inquirer
from inquirer.themes import BlueComposure

from View.InitialMenu.Login import LoginMenu
from View.InitialMenu.Register import RegisterMenu
from View.InitialMenu.MovieMenu import movieMenu

choices = [
    "Iniciar Sesión", 
    "Registrar Usuario", 
    "Listado de Películas",
    "Salir",
]

def validMenu( optionSelected: str = "Iniciar Sesión" ):
    if ( optionSelected == choices[0] ):
        LoginMenu()
    elif ( optionSelected == choices[1] ):
        RegisterMenu()
    elif ( optionSelected == choices[2] ):
        movieMenu()
    else:
        sys.exit()

def mainMenu():
    os.system('cls')
    questions = [
        inquirer.List(
            name="firstOption",
            message="¿Qué deseas hacer hoy?", 
            choices=choices,
            default=choices[0],
        ),
    ]

    answers: list = inquirer.prompt(questions, theme=BlueComposure()) # type: ignore
    optionSelected: str = answers["firstOption"] # type: ignore
    validMenu( optionSelected )

if __name__=='__main__':
    mainMenu()