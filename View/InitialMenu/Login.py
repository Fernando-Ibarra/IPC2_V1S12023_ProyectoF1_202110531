from inquirer import Text, Password, prompt
from inquirer.themes import BlueComposure
from colorama import Fore, Back, Style
import os

from Helpers.utils import list
import View.Client.MainMenu as client
from View.Admin.MainMenu import MainMenu

def __init__(self):
    pass

def LoginMenu():
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + "===============================")
    print(Fore.LIGHTYELLOW_EX + "        Iniciar Sesión        ")
    print(Fore.LIGHTYELLOW_EX + "===============================")
    
    questions = [
        Text(name='email', message="Correo Electrónico"),
        Password(name='password', message="Ingresa tu contraseña")
    ]
    
    answers: list = prompt( questions, theme=BlueComposure() ) # type: ignore
    
    email = answers["email"] # type: ignore
    password = answers["password"] # type: ignore
    
    user, ok = list.findToValidate( email, password )
    
    if ok is False:
        print("Contraseña o correo invalido")
    
    if user is not None:
        if user.rol == "administrador":
            MainMenu( user )
        else:    
            client.MainMenu( user )
    else: 
        LoginMenu()