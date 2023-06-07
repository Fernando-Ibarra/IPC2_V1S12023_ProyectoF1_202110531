from inquirer import Text, Password, prompt
from inquirer.themes import BlueComposure
from colorama import Fore, Back, Style
import os

from Model.User import User
from Model.LinkedUser import LinkedUser
from Model.NodeUser import NodeUser

name: str 
lastName: str 
phoneNUmber: str 
email: str
password: str
rol: str = "Cliente"
id: int = LinkedUser.totalSize + 1 # type: ignore
list = LinkedUser()

def __init__(self):
    pass

def RegisterMenu():
    os.system('cls')
    
    print(Fore.GREEN + "==========================")
    print(Fore.GREEN + "        Registrate        ")
    print(Fore.GREEN + "==========================")
    
    questions = [
        Text(name='name', message="Nombres"),
        Text(name='lastName', message="Apellidos"),
        Text(name='phoneNumber', message="Teléfono"),
        Text(name='email', message="Correo Electrónico"),
        Password(name='password', message="Ingresa tu contraseña")
    ]
    
    answers: list = prompt( questions, theme=BlueComposure() ) # type: ignore
    name = answers["name"] # type: ignore
    lastName = answers["lastName"] # type: ignore
    phoneNumber = answers["phoneNumber"] # type: ignore
    email = answers["email"] # type: ignore
    password = answers["password"] # type: ignore
    
    user: User = User( name, lastName, phoneNumber, email, password, rol, id )
    nodeUser: NodeUser = NodeUser( user )
    list.push( nodeUser ) # type: ignore
    list.show() # type: ignore


