from inquirer import List, prompt, Text, errors
from inquirer.themes import BlueComposure
from colorama import Fore, Back
import os

from Model.user.User import User
from View.Admin.Categories.categoryTools import showMoviesTicketMenu, NodeCategory
from Model.theater.LinkedListTheater import NodeTheater
from Model.movie.Movie import Movie
from View.utils.utilsMovieRoom import showMovieRooms
from Model.movieRoom.MovieRoom import MovieRoom
from main import ListTheater, listTicket
import View.Client.MainMenu as mainMenu

choices = [
    "Comprar otro",
    "Salir"
]

def __init__( self ):
    pass

def mainShopTicketMenu( user: User ):
    os.system('cls')
    print(Fore.LIGHTRED_EX + "==============================")
    print(Fore.LIGHTRED_EX + "        Comprar Boletos       ")
    print(Fore.LIGHTRED_EX + "==============================")
    
    nodeCategory: NodeCategory = showMoviesTicketMenu()
    
    req1 = [
        Text(name='numberMovie', message="¿Cuál desea marcar?"),
    ]
    
    res1: list = prompt(req1, theme=BlueComposure()) # type: ignore
    number: int = int(res1["numberMovie"]) # type: ignore
        
    movie: Movie = nodeCategory.category.movies.findMovie( number )
        
    req2 = [
        Text(name='amount', message="¿Cuántos desea comprar"),
    ]    
    
    res2: list = prompt(req2, theme=BlueComposure()) # type: ignore
    amount: int = int(res2["amount"]) # type: ignore
        
    ListTheater.show()
    
    req3 = [
        Text(name='numberIndex', message="¿Cuántos desea comprar"),
    ]    
    
    res3: list = prompt(req3, theme=BlueComposure()) # type: ignore
    numberIndex: int = int(res3["numberIndex"]) # type: ignore
    nodeTheater: NodeTheater = ListTheater.findNode( numberIndex )
    
    showMovieRooms( nodeTheater )
    
    req4 = [
        Text(name='indexMovieRoom', message="¿Cúal desea seleccionar"),
    ]    
    
    res4: list = prompt(req4, theme=BlueComposure()) # type: ignore
    indexMovieRoom: int = int(res4["indexMovieRoom"]) # type: ignore
    
    numberC, seatsC = nodeTheater.theater.rooms.returnMovieRoom( indexMovieRoom + 1 )
    
    def seat_validation( answers, current ):
        if  int(current) <= seatsC:
            return True
        else:
            raise errors.ValidationError( '', reason="El asiento no esta en el rango" )
            
    req5 = [
        Text(
                name='seats', 
                message="¿Qué asiento desea?", 
                validate=seat_validation
            ),
    ]    
    
    res5: list = prompt(req5, theme=BlueComposure()) # type: ignore
    seats: int = int(res5["seats"]) # type: ignore
    
    req6 = [
        List(
                name='modoPago', 
                message="¿Facturación?",
                choices=[
                    "C/F",
                    "NIT"
                ]
            ),
    ]    
    
    res6: list = prompt(req6, theme=BlueComposure()) # type: ignore
    metNit: str = res6["modoPago"] # type: ignore

    obj_Ticket = {}
    
    idF: int = listTicket.__len__() + 1
    
    idFac = f"#USACIPC2_2022110531_{ idF }"
    
    if( metNit == "C/F"):
        obj_Ticket = {
            'id': idFac,
            'película': movie.title,
            'fecha': movie.date,
            'hora': movie.time,
            'cantidad': amount,
            'sala': numberC,
            'asientos': seatsC,
            'total': amount*42,
            'nit': "C/F",
            'Nombre': "C/F",
            'dirección': "C/F",
            'nameUser': user.name,
            'lastNameUser': user.lastName,
            'emailUser': user.email,
            'estado': True
        }
    else:
        req6 = [
            Text(
                    name='nombre', 
                    message="Nombre"
                ),
            Text(
                    name='nit', 
                    message="NIT"
                ),
            Text(
                    name='direccion', 
                    message="Dirección"
                ),
        ]    

        res6: list = prompt(req6, theme=BlueComposure()) # type: ignore
        
        nombreF: str = res6["nombre"] # type: ignore
        nitF: str = res6["nit"] # type: ignore
        direcF: str = res6["direccion"] # type: ignore
        
        obj_Ticket = {
            'id': idFac,
            'película': movie.title,
            'fecha': movie.date,
            'hora': movie.time,
            'cantidad': amount,
            'sala': numberC,
            'asientos': seatsC,
            'total': amount*42,
            'nit': nitF,
            'Nombre': nombreF,
            'dirección': direcF,
            'nameUser': user.name,
            'lastNameUser': user.lastName,
            'emailUser': user.email,
            'estado': True
        }
        
    listTicket.append( obj_Ticket )
    
    print(Fore.LIGHTMAGENTA_EX + "=============================")
    print(Fore.LIGHTMAGENTA_EX + "        USAC - CINEMA        ")
    print(Fore.LIGHTMAGENTA_EX + "=============================")
    
    print(Fore.LIGHTYELLOW_EX + f"Id: { obj_Ticket['id'] }")
                                  
    print(Fore.LIGHTMAGENTA_EX + "======== Datos Película ========")
    print(Fore.LIGHTRED_EX + f"Película: { obj_Ticket['película'] }")
    print(Fore.LIGHTRED_EX + f"Sala: { obj_Ticket['sala'] }")
    print(Fore.LIGHTRED_EX + f"Asientos: { obj_Ticket['asientos'] }")
    print(Fore.LIGHTRED_EX + f"Fecha: { obj_Ticket['fecha'] } Hora: { obj_Ticket['hora'] }")
    
    print(Fore.LIGHTMAGENTA_EX + "======== Datos Factura ========")
    print(Fore.LIGHTYELLOW_EX + f"NIT: { obj_Ticket['nit'] }  Nombre: { obj_Ticket['Nombre'] }")
    print(Fore.LIGHTYELLOW_EX + f"Dirección: { obj_Ticket['dirección'] }")
    print(Fore.LIGHTMAGENTA_EX + f"         Cantidad        Precio Unitario")
    print(Fore.LIGHTYELLOW_EX + f"{ obj_Ticket['total'] / 42 }        Q42.00 ")
    print(Fore.LIGHTGREEN_EX + f"              Total              { obj_Ticket['total'] }")
    
    questions = [
            List(
                name="firstOption",
                message="¿Qué deseas hacer hoy?", 
                choices=choices,
                default=choices[0],
            ),
        ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    optionSelected: str = answers["firstOption"] # type: ignore
    
    if ( optionSelected == choices[0] ):
        mainShopTicketMenu( user )
    else:
        mainMenu.MainMenu( user )