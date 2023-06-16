from colorama import Fore

from .NodeMovieRoom import NodeMovieRoom
from .MovieRoom import MovieRoom

class DoubleLinkedListMovieRoom(object):
    
    def __init__( self ) -> None:
        """ Create an empty list """
        self.header: NodeMovieRoom = NodeMovieRoom( None, None, None ) # type: ignore
        self.trailer: NodeMovieRoom = NodeMovieRoom( None, None, None ) # type: ignore
        self.header.next = self.trailer
        self.trailer.prev = self.header
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
    
    def insertBetween( self, movieRoom: MovieRoom, predecessor: NodeMovieRoom, sucessor: NodeMovieRoom ) -> None:
        """insertBetween - Add movieRoom between two existing nodes and return new Node 

        Args:
            movieRoom (MovieRoom): movieRoom object
            predecessor (NodeMovieRoom): previous Node
            sucessor (NodeMovieRoom): next Node
        
        Returns:
            [ NodeMovieRoom ] - new NodeMovieRoom
        """
        newest = NodeMovieRoom( movieRoom, predecessor, sucessor )
        predecessor.next = newest
        sucessor.prev = newest
        self.size += 1
        return None
    
    def push( self, movieRoom: MovieRoom ) -> None:
        """push - Add a MovieRoom to the back of the list

        Args:
            movieRoom (MovieRoom): movieRoom object
        """
        self.insertBetween( movieRoom, self.trailer.prev, self.trailer ) # type: ignore
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
        
    def modifyMovieRoom( self, indexCome: int, field: str, value  ):
        index: int = 1
        auxNode = self.header
        while auxNode is not None:
            if( index == indexCome ):
                if ( field == "number" ):
                    auxNode.movieRoom.number = value
                    return None
                elif ( field == "seats" ):
                    auxNode.movieRoom.seats = value
                    return None
                else:
                    return None
            else:
                auxNode = auxNode.next
                index += 1
                
    def returnMovieRoom( self, indexCome: int ): # type: ignore
        index: int = 1
        auxNode = self.header
        while auxNode is not None:
            if( index == indexCome ):
                return auxNode.movieRoom.number, auxNode.movieRoom.seats 
            else:
                auxNode = auxNode.next
                index += 1
    
    def findNode( self, indexCome: int ) -> NodeMovieRoom:
        index: int = 1
        auxNode: NodeMovieRoom = self.header
        while auxNode is not None:
            if( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next # type: ignore
                index += 1
        return None # type: ignore