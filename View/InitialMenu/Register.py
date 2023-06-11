from colorama import Fore, Back, Style
import os

from Model.user.NodeUser import NodeUser
from Helpers.utils import list
from View.utils.utils import createUser
from View.InitialMenu.Login import LoginMenu

def __init__(self):
    pass

def RegisterMenu():
    os.system('cls')
    
    print(Fore.GREEN + "==========================")
    print(Fore.GREEN + "        Registrate        ")
    print(Fore.GREEN + "==========================")
    
    nodeUser: NodeUser = createUser(1)
    list.push( nodeUser ) # type: ignore
    print(f" Tu usuario ha sido creado satisfactoriamente! ")
    
    LoginMenu()   

