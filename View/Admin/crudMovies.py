from inquirer import List, prompt
from inquirer.themes import BlueComposure
import os

import View.Admin.Movies.movieTools as movieMenu
import View.Admin.MainMenu as mainMenu
from Model.user.User import User

choices = [
    "Crear Cine",
    "Listar Cines",
    "Modificar Cine",
    "Eliminar Cine",
    "Crear Sala",
    "Listar Salas",
    "Modificar Sala",
    "Eliminar Sala",
    "Importar XML",
    "Expotar XML",
    "Salir"
]

def toCrud( optionSelected: str = "Crear Cine", user: User = None ): # type: ignore
    if ( optionSelected == choices[0] ):
        movieMenu.createTheater( user )
    elif ( optionSelected == choices[1] ):
        movieMenu.showTheaters( user )
    elif ( optionSelected == choices[2] ):
        movieMenu.modifyTheater( user )
    elif ( optionSelected == choices[3] ):
        movieMenu.deleteTheater( user )
    elif ( optionSelected == choices[4] ):
        movieMenu.createMovieRoom( user )
    elif ( optionSelected == choices[5] ):
        movieMenu.showMovieRoom( user )
    elif ( optionSelected == choices[6] ):
        movieMenu.modifyMovieRoom( user )
    elif ( optionSelected == choices[7] ):
        movieMenu.deleteMovieRoom( user )
    elif ( optionSelected == choices[8] ):
        movieMenu.importXML( user )
    elif ( optionSelected == choices[9] ):
        print("EXPOTAR XML")
        # TODO
        # movieMenu.importXML( user )
    else:
        mainMenu.MainMenu( user )

def mainCrudMovies( user ):
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