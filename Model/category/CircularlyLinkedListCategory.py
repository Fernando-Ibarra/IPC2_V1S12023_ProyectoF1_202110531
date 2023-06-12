from .NodeCategory import NodeCategory, Category

class CircularlyLinkedListCategory(object):

    def __init__(self) -> None:
        """ Create an empty list """
        self.head: NodeCategory = None # type: ignore
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
        return self.head == None

    def push(self, category: Category):
        """push - Add a Category to the back of the list

        Args:
            category (Category): category object
        """
        tempNode: NodeCategory = NodeCategory( category )

        if self.head is None:
            tempNode.next = tempNode
            tempNode.prev = tempNode
            self.head = tempNode
        else:
            ultimo: NodeCategory = self.head.prev # type: ignore

            tempNode.next = self.head
            tempNode.prev = ultimo

            self.head.prev = tempNode
            ultimo.next = tempNode
        self.size += 1
        
    def show( self ):
        index = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            print("#     Nombre")
            auxNode: NodeCategory = self.head
            
            while True:
                if( auxNode is not None ):
                    if( auxNode.category is not None ):
                        auxNode.show( index )
                        auxNode = auxNode.next # type: ignore
                        if auxNode == self.head:
                            break
                        index += 1
    
    def modify( self, indexCome: int, name: str ) -> None:
        index: int = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            auxNode: NodeCategory = self.head
            while True:
                if( index == indexCome ):
                    auxNode.category.name = name
                    return None
                else:
                    auxNode = auxNode.next # type: ignore
                    if auxNode == self.head:
                        break
                    index += 1
            return None
        
    def delete( self, indexCome: int ) -> None:
        index: int = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            auxNode: NodeCategory = self.head
            while True:
                if( index == indexCome ):
                    if( auxNode == self.head ):
                                            
                        newFirst: NodeCategory = auxNode.next # type: ignore
                        lastOne: NodeCategory = auxNode.prev # type: ignore
                        
                        lastOne.next = self.head = newFirst
                        newFirst.prev = lastOne
                        
                        auxNode.prev = auxNode.next = auxNode.category = None # type: ignore
                        return None
                    
                    if( auxNode is not self.head ):
                        predecessor: NodeCategory = auxNode.prev # type: ignore
                        sucessor: NodeCategory = auxNode.next # type: ignore
                        predecessor.next = sucessor
                        sucessor.prev = predecessor
                        self.size -= 1
                        auxNode.prev = auxNode.next = auxNode.category = None # type: ignore
                        return None
                else:
                    auxNode = auxNode.next # type: ignore
                    if auxNode == self.head:
                        break
                    index += 1
            return None
        
    def findNode( self, indexCome: int ) -> NodeCategory: # type: ignore
        index: int = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            auxNode: NodeCategory = self.head
            while True:
                if( index == indexCome ):
                    return auxNode
                else:
                    auxNode = auxNode.next # type: ignore
                    if auxNode == self.head:
                        break
                    index += 1
            return None # type: ignore
        