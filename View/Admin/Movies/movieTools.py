from colorama import Fore
import os

import View.utils.utilsMovieRoom as util
import View.Admin.crudMovies as movieMenuAdmin
from Model.theater.LinkedListTheater import NodeTheater
from Model.movieRoom.NodeMovieRoom import NodeMovieRoom, MovieRoom
from Model.user.User import User
from Helpers.utils import ListTheater

# * THEATER

def createTheater( user: User ) -> None:
    os.system('cls')
    
    print(Fore.GREEN + "====================================")
    print(Fore.GREEN + "        Registrar Nuevo Cine        ")
    print(Fore.GREEN + "====================================")
    
    nodeTheater: NodeTheater = util.createTheater()
    ListTheater.push( nodeTheater )
    print(f" El cine ha sido creado satisfactoriamente! ")
    out:str = util.outShowOptionMenu( 1 )
    if( out == "Crear otro" ):
        return showTheaters( user )
    else:
        return movieMenuAdmin.mainCrudMovies( user )
    
def showTheaters( user: User ) -> None:
    os.system('cls')
    print(Fore.GREEN + "===============================")
    print(Fore.GREEN + "       Cines Registrados       ")
    print(Fore.GREEN + "===============================")
    
    ListTheater.show()
    out:str = util.outShowOptionMenu( 2 )
    if( out == "Mostrar otra vez" ):
        return showTheaters( user )
    else:
        return movieMenuAdmin.mainCrudMovies( user )
        
def modifyTheater( user: User ) -> None:
    os.system('cls')
    print(Fore.GREEN + "===========================")
    print(Fore.GREEN + "       Modificar Cine      ")
    print(Fore.GREEN + "===========================")
    ListTheater.show()
    
    index: int = util.selectIndexChange()
    name: str = util.modifyTheater()
    ListTheater.modifyUser( index, name )
    
    ListTheater.show()
    
    out:str = util.outShowOptionMenu( 3 )
    print(f" El cine ha sido actualizado satisfactoriamente! ")
    if( out == "Volver a cambiar" ):
        return modifyTheater( user )
    else:
        return movieMenuAdmin.mainCrudMovies( user )

def deleteTheater( user: User ) -> None:
    os.system('cls')
    print(Fore.GREEN + "==========================")
    print(Fore.GREEN + "       Eliminar Cine      ")
    print(Fore.GREEN + "==========================")
    ListTheater.show()
    
    index: int = util.selectIndexChange()
    ListTheater.deleteTheater( index )
    
    ListTheater.show()
    
    out:str = util.outShowOptionMenu( 4 )
    print(f" El cine ha sido Eliminado satisfactoriamente! ")
    if( out == "Eliminar otro más" ):
        return deleteTheater( user )
    else:
        return movieMenuAdmin.mainCrudMovies( user )

# * MovieRoom

def createMovieRoom( user: User, ):
    os.system('cls')
    
    print(Fore.GREEN + "====================================")
    print(Fore.GREEN + "        Registrar Nueva Sala        ")
    print(Fore.GREEN + "====================================")
    ListTheater.show()
    
    index: int = util.selectIndexChange()
    nodeTheater: NodeTheater = ListTheater.findNode( index )
    movieRoom: MovieRoom = util.createMovieRoom()
    nodeTheater.theater.rooms.push( movieRoom )
    print(f" La sala ha sido creado satisfactoriamente! ")
    out:str = util.outShowOptionMenu( 1 )
    if( out == "Crear otro" ):
        return createMovieRoom( user )
    else:
        return movieMenuAdmin.mainCrudMovies( user )

def showMovieRoom( user: User, ):
    os.system('cls')
    
    print(Fore.GREEN + "=================================")
    print(Fore.GREEN + "        Salas Registradas        ")
    print(Fore.GREEN + "=================================")
    ListTheater.show()
    
    index: int = util.selectIndexChange()
    nodeTheater: NodeTheater = ListTheater.findNode( index )
    nodeTheater.theater.rooms.show()
    
    out:str = util.outShowOptionMenu( 2 )
    if( out == "Mostrar otra vez" ):
        showMovieRoom( user )
    else:
        movieMenuAdmin.mainCrudMovies( user )
    
def modifyMovieRoom( user: User ) -> None:
    os.system('cls')
    print(Fore.GREEN + "===========================")
    print(Fore.GREEN + "       Modificar Sala      ")
    print(Fore.GREEN + "===========================")
    ListTheater.show()
    
    index: int = util.selectIndexChange()
    nodeTheater: NodeTheater = ListTheater.findNode( index )
    nodeTheater.theater.rooms.show()
    
    indexMovieRoom: int = util.selectIndexChange()
    field, value = util.modifyConfig()
    nodeTheater.theater.rooms.modifyMovieRoom( indexMovieRoom, field, value )
    
    nodeTheater.theater.rooms.show()
    
    out:str = util.outShowOptionMenu( 3 )
    print(f" La sala ha sido actualizado satisfactoriamente! ")
    if( out == "Volver a cambiar" ):
        return modifyMovieRoom( user )
    else:
        return movieMenuAdmin.mainCrudMovies( user )


def deleteMovieRoom( user: User ) -> None:
    os.system('cls')
    print(Fore.GREEN + "==========================")
    print(Fore.GREEN + "       Eliminar Sala      ")
    print(Fore.GREEN + "==========================")
    ListTheater.show()
    
    index: int = util.selectIndexChange()
    nodeTheater: NodeTheater = ListTheater.findNode( index )
    nodeTheater.theater.rooms.show()
    
    indexMovieRoom: int = util.selectIndexChange()
    nodeMovieRoom: NodeMovieRoom = nodeTheater.theater.rooms.findNode( indexMovieRoom )
    nodeTheater.theater.rooms.deleteNode( nodeMovieRoom )
    
    nodeTheater.theater.rooms.show()
    
    out:str = util.outShowOptionMenu( 4 )
    print(f" La sala ha sido Eliminado satisfactoriamente! ")
    if( out == "Eliminar otro más" ):
        return deleteMovieRoom( user )
    else:
        return movieMenuAdmin.mainCrudMovies( user )