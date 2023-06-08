from Model.NodeMovieRoom import NodeMovieRoom

class DoubleLinkedListMovieRoom(object):
    
    def __init__( self ) -> None:
        self.head: NodeMovieRoom = None # type: ignore
        self.tail: NodeMovieRoom = None # type: ignore
        self.lenght = 0
        
    def isEmpty( self ) -> bool:
        return self.tail == None
    
    def push( self, node ):
        
        newNode: NodeMovieRoom = node
        
        if self.isEmpty():
            self.tail = self.head = newNode
        else:
            oldestHead = self.head
            self.head = oldestHead.next = newNode
            self.head.prev = oldestHead
        self.lenght += 1
        
    def show(self) -> None:
        auxNode: NodeMovieRoom = self.tail
        while auxNode:
            print(f" Sala { auxNode.movieRoom.number } - Asienot { auxNode.movieRoom.seats } ")
            auxNode = auxNode.next # type: ignore