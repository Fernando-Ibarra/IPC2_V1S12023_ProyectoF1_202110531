from Model.user.User import User
from Model.user.NodeUser import NodeUser
from Helpers.utils import list
import View.InitialMenu.MainMenu as mm
from Model.theater.LinkedListTheater import LinkedListTheater

name: str 
lastName: str 
phoneNUmber: str 
email: str
password: str
rol: str = "administrador"

ListTheater = LinkedListTheater()

def run():   
    user: User = User( "Fernando", "Ibarra", "49900123", "fi94457@gmail.com", "123", rol)
    nodeUser: NodeUser = NodeUser( user )
    list.push( nodeUser ) # type: ignore
    mm.mainMenu()
    
if __name__=='__main__':
    run()