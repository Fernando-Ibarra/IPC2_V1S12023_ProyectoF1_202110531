from colorama import Fore
import os

from Model.user.User import User
from main import listTicket
from View.utils.utilsTicketSold import outShowOptionMenu, selectIndexChange
import View.Admin.crudSoldTickets as tickerMenuAdmin

def showSoldTicke( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTCYAN_EX + "==============================")
    print(Fore.LIGHTCYAN_EX + "       Boletos Vendidos       ")
    print(Fore.LIGHTCYAN_EX + "==============================")
    
    print(" #  Id  Estado")
    for index,ticket in enumerate(listTicket):
        if( ticket['estado'] is False):
            estado = "Cancelado"
            print(f"{ index + 1 } { ticket['id'] } { estado }")
        else:
            estado = "Activa"
            print(f"{ index + 1 } { ticket['id'] } { estado }")
    
    out:str = outShowOptionMenu( 1 )
    if( out == "Mostrar otra vez" ):
        showSoldTicke( user )
    else:
        tickerMenuAdmin.mainCrudSoldTickets( user )
        
def canceleSoldTicke( user: User ) -> None:
    os.system('cls')
    print(Fore.LIGHTCYAN_EX + "=============================")
    print(Fore.LIGHTCYAN_EX + "       Cancelar Boleto       ")
    print(Fore.LIGHTCYAN_EX + "=============================")
    
    print(" #  Id  Estado")
    for index,ticket in enumerate(listTicket):
        if( ticket['estado'] is False):
            estado = "Cancelado"
            print(f"{ index + 1 } { ticket['id'] } { estado }")
        else:
            estado = "Activa"
            print(f"{ index + 1 } { ticket['id'] } { estado }")
        
    index = selectIndexChange()
    obj_Ticket = listTicket[index - 1]
    obj_Ticket['estado'] = False
    
    print(" #  Id  Estado")
    for index,ticket in enumerate(listTicket):
        if( ticket['estado'] is False):
            estado = "Cancelado"
            print(Fore.LIGHTCYAN_EX + f"{ index + 1 } { ticket['id'] } { estado }")
        else:
            estado = "Activa"
            print(Fore.LIGHTCYAN_EX + f"{ index + 1 } { ticket['id'] } { estado }")
    
    out:str = outShowOptionMenu( 2 )
    if( out == "Cancelar otro más" ):
        canceleSoldTicke( user )
    else:
        tickerMenuAdmin.mainCrudSoldTickets( user )