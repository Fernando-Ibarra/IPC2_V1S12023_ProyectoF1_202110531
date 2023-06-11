from colorama import Fore

from .NodeMovieRoom import NodeMovieRoom
from .MovieRoom import MovieRoom

class DoubleLinkedListMovieRoom(object):
    
    def __init__( self ) -> None:
        """ Create an empty list """
        self.head: NodeMovieRoom = NodeMovieRoom( None, None, None ) # type: ignore
        self.tail: NodeMovieRoom = NodeMovieRoom( None, None, None ) # type: ignore
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def __len__( self ):
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
        return self.size == 0
    
    def insertBetween( self, movieRoom: MovieRoom, predecessor, sucessor ) -> None:
        """insertBetween - Add movieRoom between two existing nodes and return new Node 

        Args:
            movieRoom (MovieRoom): movieRoom object
            predecessor (NodeMovieRoom): previous Node
            sucessor (NodeMovieRoom): next Node
        
        Returns:
            [ NodeMovieRoom ] - new NodeMovieRoom
        """
        newest = NodeMovieRoom( movieRoom, predecessor, sucessor )
        if ( self.head is None ):
            self.head = newest
        else:
            predecessor.next = newest
            sucessor.prev = newest
            self.size += 1
        return None
    
    def push( self, movieRoom: MovieRoom ) -> None:
        """push - Add a MovieRoom to the back of the list

        Args:
            movieRoom (MovieRoom): movieRoom object
        """
        self.insertBetween( movieRoom, self.tail.prev, self.tail )
        return None
    
    def deleteNode( self, node: NodeMovieRoom ) -> None:
        """deleteNode Delete node from the list

        Args:
            node (NodeMovieRoom): movieRoom object
        """
        predecessor: NodeMovieRoom = node.prev # type: ignore
        sucessor: NodeMovieRoom = node.next # type: ignore
        predecessor.next = sucessor
        sucessor.prev = predecessor
        self.size -= 1
        # deprecate Node
        node.prev = node.next = node.movieRoom = None # type: ignore
        return None
    
    def show( self ):
        index: int = 0
        """ Print each element in the linkedList """
        print(Fore.WHITE + "#     Número     Asientos")
        auxNode: NodeMovieRoom = self.head
        if auxNode.movieRoom is not None:
            index += 1
            auxNode.movieRoom.show( index )
        while auxNode.next is not None:
            index += 1
            auxNode = auxNode.next
            auxNode.movieRoom.show( index )
        return None
    
    def modifyMovieRoom( self, indexCome: int, field: str, value  ):
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                if ( field == "number" ):
                    auxNode.movieRoom.number = value
                    return None
                elif ( field == "lastName" ):
                    auxNode.movieRoom.seats = value
                    return None
                else:
                    return None
            else:
                auxNode = auxNode.next
                index += 1
    
    def findNode( self, indexCome: int ) -> NodeMovieRoom:
        index: int = 1
        auxNode: NodeMovieRoom = self.head
        while auxNode is not None:
            if( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next # type: ignore
                index += 1
        return None # type: ignore