from Model.NodeUser import NodeUser
from Model.User import User

class LinkedUser(object):
    
    totalSize: int = 0
    
    def __init__(self) -> None:
        """ Create an empty stack """
        self.head: NodeUser = None # type: ignore
        self.tail: NodeUser = None # type: ignore
        self.size: int = 0
        totalSize = self.size
        
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
        """ Print each element in the linkedList """
        auxNode: NodeUser = self.head
        auxNode.user.show()
        while auxNode.next is not None:
            auxNode = auxNode.next
            auxNode.user.show()
    
    def findToValidate( self, email:str, password: str) -> User:
        auxNode = self.head
        while auxNode is not None:
            if auxNode.user.password == password and auxNode.user.email == email:
               return auxNode.user
            auxNode = auxNode.next
        return None
    
           
