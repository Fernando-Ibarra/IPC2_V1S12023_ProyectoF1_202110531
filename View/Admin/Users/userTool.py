from inquirer import Text
from colorama import Fore
import os

import View.utils.utils as util
from Model.user.NodeUser import NodeUser
from Model.user.User import User
from Helpers.utils import list
import View.Admin.crudUsers as userMenuAdmin



def createUser( user: User ):
    os.system('cls')
    
    print(Fore.GREEN + "=======================================")
    print(Fore.GREEN + "        Registrar Nuevo Usuario        ")
    print(Fore.GREEN + "=======================================")
    
    nodeUser: NodeUser = util.createUser( 2 )
    list.push( nodeUser ) # type: ignore
    print(f" El usuario ha sido creado satisfactoriamente! ")
    userMenuAdmin.mainCrudUser( user )
    
def showUsers( user: User ):
    os.system('cls')
    print(Fore.GREEN + "==================================")
    print(Fore.GREEN + "       Usuarios Registrados       ")
    print(Fore.GREEN + "==================================")
    
    list.show()
    out:str = util.outShowOptionMenu()
    if( out == "Volver a mostrar" ):
        showUsers( user )
    else:
        userMenuAdmin.mainCrudUser( user )

def modifyUser( user: User ):
    os.system('cls')
    print(Fore.GREEN + "==============================")
    print(Fore.GREEN + "       Modificar Usuario      ")
    print(Fore.GREEN + "==============================")
    list.show()
    
    index: int = util.selectIndexChange()
    field, value = util.configModify()
    list.modifyUser( index, field, value )
    
    list.show()
    
    out:str = util.outShowOptionMenu2()
    if( out == "Cambiar algo más" ):
        modifyUser( user )
    else:
        userMenuAdmin.mainCrudUser( user )

def deleteUser( user: User ):
    os.system('cls')
    print(Fore.GREEN + "=============================")
    print(Fore.GREEN + "       Eliminar Usuario      ")
    print(Fore.GREEN + "=============================")
    list.show()
    
    index: int = util.selectIndexChange()
    list.deleteUser( index )
    
    list.show()
    
    out:str = util.outShowOptionMenu3()
    if( out == "Eliminar otro más" ):
        deleteUser( user )
    else:
        userMenuAdmin.mainCrudUser( user )
        
def importXML( user: User ):
    os.system('cls')
    print(Fore.GREEN + "===========================")
    print(Fore.GREEN + "       Importando XML      ")
    print(Fore.GREEN + "===========================")
    
    util.createUserFromXML()
    
    print("Usuarios Cargados Correctamente")
    list.show()
    
    out:str = util.outShowOptionMenu4()
    if( out == "Salir" ):
        userMenuAdmin.mainCrudUser( user )
        