from colorama import Fore
from .Category import Category

class NodeCategory(object):
    
    __slost__ = 'category', 'next', 'priv'
    
    def __init__(self, category: Category, prev=None, next=None, ):
        self.category = category
        self.prev = prev
        self.next = next
        
    def show( self, index ):
        if( self.category is not None ):
            if ( self.category.name is not None and self.category.movies is not None ):
                print(Fore.WHITE + f"{ index } { self.category.name }")