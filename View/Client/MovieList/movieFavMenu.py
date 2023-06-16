from inquirer import List, prompt
from inquirer.themes import BlueComposure
import os

from Model.user.User import User
import View.Client.MainMenu as mainMenu
from main import listFavMovie

choices = [
    "Mostrar de nuevo",
    "Salir"
]

def __init__( self ):
    pass

def mainFavMovieMenu( user: User ):
    os.system('cls')
    
    print("=========================")
    print("   Películas Favoritas   ")
    print("=========================")
    
    index = 0
    print("#   Nombre   Director   Año")
    for movie in listFavMovie:
        if( movie[0] == user.name and  movie[1] == user.lastName ):
            if( movie[2] == user.email ):
                index += 1
                print(f"{ index } { movie[3] } { movie[4] } { movie[5] } ")
                
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
    
    if ( optionSelected == choices[0] ):
        mainFavMovieMenu( user )
    else:
        mainMenu.MainMenu( user )