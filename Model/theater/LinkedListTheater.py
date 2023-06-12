from colorama import Fore

from .NodeTheater import NodeTheater, Theater

class LinkedListTheater(object):
    
    def __init__( self ) -> None:
        self.head: NodeTheater = None # type: ignore
        self.tail: NodeTheater = None # type: ignore
        self.size = 0
        
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
    def push(self, node: NodeTheater) -> None:
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
        print(Fore.WHITE + "#     Cine  ")
        auxNode: NodeTheater = self.head
        auxNode.theater.show(index)
        while auxNode.next is not None:
            index += 1
            auxNode = auxNode.next
            auxNode.theater.show(index)
            
    def findTheater( self, indexCome: int ) -> Theater:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode.theater
            else:
                auxNode = auxNode.next
                index += 1
        return None # type: ignore
    
    def findNode( self, indexCome: int ) -> NodeTheater:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next
                index += 1
        return None # type: ignore
    
    def findNodeByName( self, name: str ) -> NodeTheater:
        auxNode = self.head
        while auxNode is not None:
            if ( auxNode.theater.nombre == name ):
                return auxNode
            else:
                auxNode = auxNode.next
        return None # type: ignore
    
    def deleteTheater( self, indexCome: int ) -> None:
        deleteNode: NodeTheater = self.findNode( indexCome )
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
        
    def modifyUser( self, indexCome: int, name: str) -> None:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                auxNode.theater.nombre = name
                return None
            else:
                auxNode = auxNode.next
                index += 1
        return None