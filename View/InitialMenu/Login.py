from inquirer import Text, Password, prompt
from inquirer.themes import BlueComposure
from colorama import Fore, Back, Style
import os

from Helpers.utils import list
from View.Client.MainMenu import mainMenu
from View.Admin.MainMenu import MainMenu

def __init__(self):
    pass

def LoginMenu():
    os.system('cls')

    print(Fore.GREEN + "===============================")
    print(Fore.GREEN + "        Iniciar Sesión        ")
    print(Fore.GREEN + "===============================")
    
    questions = [
        Text(name='email', message="Correo Electrónico"),
        Password(name='password', message="Ingresa tu contraseña")
    ]
    
    answers: list = prompt( questions, theme=BlueComposure() ) # type: ignore
    
    email = answers["email"] # type: ignore
    password = answers["password"] # type: ignore
    
    user = list.findToValidate( email.upper(), password )
    
    if user is not None:
        if user.rol == "administrador":
            MainMenu( user )
        else:    
            mainMenu( user )
    else: 
        LoginMenu()