from inquirer import List, prompt
from inquirer.themes import BlueComposure
from colorama import Fore
import os

from Model.user.User import User
from main import listTicket

import View.Client.MainMenu as mainMenu

choices = [
    "Mostrar otra vez",
    "Salir"
]

def __init__( self ):
    pass

def viewTickets( user: User ):
    os.system('cls')
    print(Fore.LIGHTRED_EX + "=============================================")
    print(Fore.LIGHTRED_EX + "        Historial de Boletos Comprados       ")
    print(Fore.LIGHTRED_EX + "=============================================")
    
    print(" Id                  Película          Fecha    Hora  Cantidad       Sala")
    for ticket in listTicket:
        if( ticket['nameUser'] == user.name and ticket['lastNameUser'] == user.lastName):
            if( ticket['emailUser'] == user.email):
                if( ticket['estado'] is not False):
                    print(" Id                  Película          Fecha    Hora  Cantidad       Sala")
                    print(Fore.LIGHTYELLOW_EX + f"{ ticket['id'] }  { ticket['película'] }  { ticket['fecha'] }  { ticket['hora'] } { ticket['cantidad'] } { ticket['sala'] }")
                else:
                    print(Fore.LIGHTYELLOW_EX + "No tiene Boletos activos")
    
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
        viewTickets( user )
    else:
        mainMenu.MainMenu( user )