from inquirer import List, prompt
from inquirer.themes import BlueComposure
import os

from Model.user.User import User
import View.InitialMenu.MainMenu as MenuInitial
from View.Client.MovieList.movieListMenu import mainMovieListMenu
from View.Client.MovieList.movieFavMenu import mainFavMovieMenu 
from View.Client.Shopping.shopTicketMenu import mainShopTicketMenu
from View.Client.Shopping.viewTicketBought import viewTickets

choices = [
    "Ver Películas",
    "Películas Favoritas",
    "Compras Boletos",
    "Historial de Boletos Comprados",
    "Salir"
]

def validMenu( optionSelected: str = "Iniciar Sesión", user: User = None ): # type: ignore
    if ( optionSelected == choices[0] ):
        mainMovieListMenu( user )
    elif ( optionSelected == choices[1] ):
        mainFavMovieMenu( user )
    elif ( optionSelected == choices[2] ):
        mainShopTicketMenu( user )
    elif ( optionSelected == choices[3] ):
        viewTickets( user )
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