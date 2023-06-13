from colorama import Fore
import os

from main import ListCategory
import View.utils.utilsCategory as util
from Model.category.CircularlyLinkedListCategory import NodeCategory
from Model.movie.LinkedListMovie import NodeMovie
import View.Admin.crudCategories as categoriesMenuAdmin
import View.InitialMenu.MainMenu as mainMenu
from Model.user.User import User

# * CATEGORY

def createCategory( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "=========================================")
    print(Fore.LIGHTBLUE_EX + "        Registrar Nueva Categoria        ")
    print(Fore.LIGHTBLUE_EX + "=========================================")
    
    category = util.createCategory()
    print(Fore.WHITE + f"El Categoria ha sido creado satisfactoriamente! ")
    
    ListCategory.push( category )
    out:str = util.outShowOptionMenu( 1 )
    if( out == "Crear otro" ):
        createCategory( user )
    else:
        categoriesMenuAdmin.mainCrudCategories( user )
        
def showCategories( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "====================================")
    print(Fore.LIGHTBLUE_EX + "       Categorias Registrados       ")
    print(Fore.LIGHTBLUE_EX + "====================================")
    
    ListCategory.show()
    
    out:str = util.outShowOptionMenu( 2 )
    if( out == "Mostrar otra vez" ):
        showCategories( user )
    else:
        categoriesMenuAdmin.mainCrudCategories( user )
        
def modifyCategory( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "================================")
    print(Fore.LIGHTBLUE_EX + "       Modificar Categoria      ")
    print(Fore.LIGHTBLUE_EX + "================================")
    ListCategory.show()
    
    index: int = util.selectIndexChange()
    name: str = util.modifyCategory()
    ListCategory.modify( index, name )
    
    ListCategory.show()
    
    out:str = util.outShowOptionMenu( 3 )
    print(f"La categoria ha sido actualizado satisfactoriamente! ")
    if( out == "Volver a cambiar" ):
        modifyCategory( user )
    else:
        categoriesMenuAdmin.mainCrudCategories( user )
        
def deleteCategory( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "===============================")
    print(Fore.LIGHTBLUE_EX + "       Eliminar Categoria      ")
    print(Fore.LIGHTBLUE_EX + "===============================")
    ListCategory.show()
    
    index: int = util.selectIndexChange()
    ListCategory.delete( index )
    
    ListCategory.show()
    
    out:str = util.outShowOptionMenu( 4 )
    print(f"La categoria sido Eliminado satisfactoriamente! ")
    if( out == "Eliminar otro más" ):
        deleteCategory( user )
    else:
        categoriesMenuAdmin.mainCrudCategories( user )
        
# * Movies

def createMovie( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "========================================")
    print(Fore.LIGHTBLUE_EX + "        Registrar Nueva Película        ")
    print(Fore.LIGHTBLUE_EX + "========================================")
    ListCategory.show()
    
    index: int = util.selectIndexChange()
    nodeMovie: NodeMovie = util.createMovie()
    
    nodeCategory: NodeCategory = ListCategory.findNode( index )
    nodeCategory.category.movies.push( nodeMovie )
    
    print(f"La película ha sido creado satisfactoriamente!")
    
    out:str = util.outShowOptionMenu( 1 )
    if( out == "Crear otro" ):
        createMovie( user )
    else:
        categoriesMenuAdmin.mainCrudCategories( user )
        
def showMovies( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "===================================")
    print(Fore.LIGHTBLUE_EX + "        Película Registradas       ")
    print(Fore.LIGHTBLUE_EX + "===================================")
    ListCategory.show()
    index: int = util.selectIndexChange()
    
    nodeCategory: NodeCategory = ListCategory.findNode( index )
    nodeCategory.category.movies.show()
    
    out:str = util.outShowOptionMenu( 2 )
    if( out == "Mostrar otra vez" ):
        showMovies( user )
    else:
        categoriesMenuAdmin.mainCrudCategories( user )
        
def modifyMovie( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "===============================")
    print(Fore.LIGHTBLUE_EX + "       Modificar Película      ")
    print(Fore.LIGHTBLUE_EX + "===============================")
    ListCategory.show()
    
    index: int = util.selectIndexChange()
    nodeCategory: NodeCategory = ListCategory.findNode( index )
    nodeCategory.category.movies.show()
    
    indexMovie: int = util.selectIndexChange()
    field, value = util.modifyMovie()
    nodeCategory.category.movies.modifyMovie( indexMovie, field, value )
    
    nodeCategory.category.movies.show()
    
    out:str = util.outShowOptionMenu( 3 )
    print(f"La película ha sido actualizado satisfactoriamente! ")
    if( out == "Volver a cambiar" ):
        modifyMovie( user )
    else:
        categoriesMenuAdmin.mainCrudCategories( user )
        
def deleteMovie( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "==============================")
    print(Fore.LIGHTBLUE_EX + "       Eliminar Película      ")
    print(Fore.LIGHTBLUE_EX + "==============================")
    ListCategory.show()
    
    index: int = util.selectIndexChange()
    nodeCategory: NodeCategory = ListCategory.findNode( index )
    nodeCategory.category.movies.show()
    
    indexMovie: int = util.selectIndexChange()
    nodeCategory.category.movies.deleteMovie( indexMovie )
    
    ListCategory.show()
    
    out:str = util.outShowOptionMenu( 4 )
    print(f"La película sido eliminada satisfactoriamente! ")
    if( out == "Eliminar otro más" ):
        deleteMovie( user )
    else:
        categoriesMenuAdmin.mainCrudCategories( user )
        
def importXML( user: User ):
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "===========================")
    print(Fore.LIGHTBLUE_EX + "       Importando XML      ")
    print(Fore.LIGHTBLUE_EX + "===========================")
    
    util.createDataFromXMLCa()
    print(f"La información ha sido cargada satisfactoriamente! ")
    
    out:str = util.outShowOptionMenu( 5 )
    if( out == "Salir" ):
        categoriesMenuAdmin.mainCrudCategories( user )
        
def showMoviesMainMenu() -> None:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "========================")
    print(Fore.LIGHTBLUE_EX + "        Películas       ")
    print(Fore.LIGHTBLUE_EX + "========================")
    ListCategory.show()
    index: int = util.selectIndexChange()
    
    nodeCategory: NodeCategory = ListCategory.findNode( index )
    nodeCategory.category.movies.show()
    
    out:str = util.outShowOptionMenu( 2 )
    if( out == "Mostrar otra vez" ):
        showMoviesMainMenu()
    else:
        mainMenu.mainMenu()

def showAllMovies():
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "========================")
    print(Fore.LIGHTBLUE_EX + "        Películas       ")
    print(Fore.LIGHTBLUE_EX + "========================")
    
    lim = ListCategory.size
    index = 0
    
    while index <= lim:
        nodeCategory: NodeCategory = ListCategory.findNode( index )
        nodeCategory.category.movies.show()
    
    out:str = util.outShowOptionMenu( 2 )
    if( out == "Mostrar otra vez" ):
        showAllMovies()
    else:
        mainMenu.mainMenu()
        
def showMoviesMovieMenu() -> NodeCategory:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "========================")
    print(Fore.LIGHTBLUE_EX + "        Películas       ")
    print(Fore.LIGHTBLUE_EX + "========================")
    ListCategory.show()
    index: int = util.selectIndexChange()
    
    nodeCategory: NodeCategory = ListCategory.findNode( index )
    nodeCategory.category.movies.show()
    return nodeCategory
    
def showMoviesTicketMenu():
    
    ListCategory.show()
    index: int = util.selectIndexChange()
    nodeCategory: NodeCategory = ListCategory.findNode( index )
    nodeCategory.category.movies.show()
    return nodeCategory