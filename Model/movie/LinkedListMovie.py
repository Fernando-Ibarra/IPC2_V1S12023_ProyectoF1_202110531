from colorama import Fore

from .NodeMovie import NodeMovie, Movie

class LinkedListMovie(object):
    
    def __init__(self) -> None:
        """ Create an empty stack """
        self.head: NodeMovie = None # type: ignore
        self.tail: NodeMovie = None # type: ignore
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
    def push(self, node: NodeMovie) -> None:
        """Add a new Node to the back of the stack

        Args:
            e (NodeUser): User node
        """
        newNode: NodeMovie = node
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
        print(Fore.WHITE + "#     Titulo     Director     Año     Fecha     Hora")
        auxNode: NodeMovie = self.head
        auxNode.movie.show(index)
        while auxNode.next is not None:
            index += 1
            auxNode = auxNode.next
            auxNode.movie.show(index)
            
    def show2(self) -> None:
        index = 1
        """ Print each element in the linkedList """
        auxNode: NodeMovie = self.head
        auxNode.movie.show(index)
        while auxNode.next is not None:
            index += 1
            auxNode = auxNode.next
            auxNode.movie.show(index)
    
                
    def findMovie( self, indexCome: int ) -> Movie:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode.movie
            else:
                auxNode = auxNode.next
                index += 1
        return None # type: ignore
    
    def findNode( self, indexCome: int ) -> NodeMovie:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next
                index += 1
        return None # type: ignore
    
    def deleteMovie( self, indexCome: int ) -> None:
        deleteNode: NodeMovie = self.findNode( indexCome )
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

    def modifyMovie( self, indexCome: int, field: str, value ) -> None:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                if ( field == "title" ):
                    auxNode.movie.title = value
                    return None
                elif ( field == "director" ):
                    auxNode.movie.director = value
                    return None
                elif ( field == "year" ):
                    auxNode.movie.year = value
                    return None
                elif ( field == "date" ):
                    auxNode.movie.date = value
                    return None
                elif ( field == "time" ):
                    auxNode.movie.time = value
                    return None
                else:
                    return None
            else:
                auxNode = auxNode.next
                index += 1