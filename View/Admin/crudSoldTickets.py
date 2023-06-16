from inquirer import List, prompt
from inquirer.themes import BlueComposure
import os

import View.Admin.historyTickets.ticketTools as ticketMenu
from Model.user.User import User
import View.Admin.MainMenu as mainMenu

choices = [
    "Listar Boletos",
    "Cancelar Boleto",
    "Salir"
]

def toCrud( optionSelected: str = "Crear Usuario", user: User = None  ): # type: ignore
    if ( optionSelected == choices[0] ):
        ticketMenu.showSoldTicke( user )
    elif ( optionSelected == choices[1] ):
        ticketMenu.canceleSoldTicke( user )
    else:
        mainMenu.MainMenu( user )

def mainCrudSoldTickets( user: User ):
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
    