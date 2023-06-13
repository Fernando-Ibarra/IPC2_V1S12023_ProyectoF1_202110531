from colorama import Fore

from .NodeUser import NodeUser
from .User import User

class LinkedUser(object):
    
    def __init__(self) -> None:
        """ Create an empty stack """
        self.head: NodeUser = None # type: ignore
        self.tail: NodeUser = None # type: ignore
        self.size: int = 0
        
    def __len__(self) -> int:
        """ Return size methods
        
        Returns:
            [ int ] - The number of elements in the stack
        """
        return self.size
    
    def totalLen(self):
        return len(self)
    
    def isEmpty(self) -> bool:
        """ Validate Empty stack
        
        Returns:
            [ boolean ] - Return True if the stack is empty
        
        """
        return self.tail == None
    
    
    # Add User #
    def push(self, node: NodeUser) -> None:
        """Add a new Node to the back of the stack

        Args:
            e (NodeUser): User node
        """
        newNode = node
        if self.isEmpty():
            self.tail = self.head = newNode
        else:
            auxNode = self.head
            while auxNode.next is not None:
                auxNode = auxNode.next
            auxNode.next = newNode
            self.size += 1
        
    def show(self) -> None:
        index = 1
        """ Print each element in the linkedList """
        print(Fore.WHITE + "#     Nombre     Apellido     Telefono     Correo     Rol")
        auxNode: NodeUser = self.head
        auxNode.user.show(index)
        while auxNode.next is not None:
            index += 1
            auxNode = auxNode.next
            auxNode.user.show(index)
    
    def findToValidate( self, email:str, password: str):
        auxNode = self.head
        while auxNode is not None:
            if auxNode.user.password == password and auxNode.user.email == email:
               ok=True
               return auxNode.user, ok
            auxNode = auxNode.next
        ok = False
        return None, ok
    
    def findUser( self, indexCome: int ) -> User:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode.user
            else:
                auxNode = auxNode.next
                index += 1
        return None
    
    def findNode( self, indexCome: int ) -> NodeUser:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next
                index += 1
        return None # type: ignore
    
    def deleteUser( self, indexCome: int ) -> None:
        deleteNode: NodeUser = self.findNode( indexCome )
        if ( deleteNode is not None):
            auxNode = self.head
            while auxNode is not None:
                if( auxNode.next == deleteNode ): 
                    if( deleteNode is not None ):
                        tempNode = deleteNode.next 
                        auxNode.next = tempNode
                        deleteNode = None # type: ignore
                    else:
                        return None
                auxNode = auxNode.next
            return None
        else:
            return None

    def modifyUser( self, indexCome: int, field: str, value ) -> None:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                if ( field == "name" ):
                    auxNode.user.name = value
                    return None
                elif ( field == "lastName" ):
                    auxNode.user.lastName = value
                    return None
                elif ( field == "phoneNUmber" ):
                    auxNode.user.phoneNUmber = value
                    return None
                elif ( field == "email" ):
                    auxNode.user.email = value
                    return None
                elif ( field == "password" ):
                    auxNode.user.password = value
                    return None
                elif ( field == "rol" ):
                    auxNode.user.rol = value
                    return None
                else:
                    return None
            else:
                auxNode = auxNode.next
                index += 1