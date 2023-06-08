from Model.User import User
from Model.NodeUser import NodeUser
from Helpers.utils import list
from View.InitialMenu.MainMenu import mainMenu

name: str 
lastName: str 
phoneNUmber: str 
email: str
password: str
rol: str = "administrador"

def run():
    user: User = User( "Fernando", "Ibarra", "49900123", "fi94457@gmail.com", "123456", rol)
    nodeUser: NodeUser = NodeUser( user )
    list.push( nodeUser ) # type: ignore
    mainMenu()
    
    
if __name__=='__main__':
    run()