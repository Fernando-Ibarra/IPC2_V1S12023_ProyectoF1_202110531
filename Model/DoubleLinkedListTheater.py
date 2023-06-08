from Model.NodeTheater import NodeTheater

class DoubleLinkedListTheater(object):
    
    def __init__( self ) -> None:
        self.head: NodeTheater = None # type: ignore
        self.tail: NodeTheater = None # type: ignore
        self.lenght = 0
        
    def isEmpty( self ) -> bool:
        return self.tail == None
    
    def push( self, node ):
        
        newNode: NodeTheater = node
        
        if self.isEmpty():
            self.tail = self.head = newNode
        else:
            oldestHead = self.head
            self.head = oldestHead.next = newNode
            self.head.prev = oldestHead
        self.lenght += 1
        
    def show(self) -> None:
        auxNode: NodeTheater = self.tail
        while auxNode:
            print(f" Nombre { auxNode.theater.nombre } - Salas { auxNode.theater.rooms.show() } ") # type: ignore
            auxNode = auxNode.next # type: ignore