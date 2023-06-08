from Model.Movie import Movie
from Model.NodeMovie import NodeMovie

class DoubleCircularLinkedListMovie(object):
    
    def __init__(self) -> None:
        self.head: NodeMovie = None # type: ignore
        self.tail: NodeMovie = None # type: ignore
        self.size: int = 0
        
    def isEmpty(self):
        return self.tail == None
    
    def push(self, node: NodeMovie):
        newNode: NodeMovie = node
        if self.isEmpty():
            self.tail = self.head = newNode
        else:
            oldestNode: NodeMovie = self.head
            self.head = oldestNode.next = newNode