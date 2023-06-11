from inquirer import Text, prompt, List
from inquirer.themes import BlueComposure
import xml.etree.ElementTree as ET
import os

from Model.movieRoom.DoubleLinkedListMovieRoom import DoubleLinkedListMovieRoom, NodeMovieRoom, MovieRoom
from Model.theater.NodeTheater import NodeTheater, Theater

number: str
seats: int

def __init__(self):
    pass

# * THEATER

def createTheater() -> NodeTheater:
    os.system('cls')
    
    questions = [
            Text(name='name', message="Nombre"),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    
    name = answers["name"] # type: ignore
    
    rooms = DoubleLinkedListMovieRoom()

    theater: Theater = Theater( name, rooms )
    nodeTheater: NodeTheater = NodeTheater( theater )
    
    return nodeTheater

def modifyTheater() -> str:
    os.system('cls')
    
    questions = [
            Text(name='name', message="Nuevo Nombre"),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore

    name = answers["name"] # type: ignore
    return name

# * MOVIEROOM

def createMovieRoom() -> MovieRoom:
    
    questions = [
            Text(name='number', message="Número"),
            Text(name='seats', message="Asientos"),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    
    number = answers["number"] # type: ignore
    seats = answers["seats"] # type: ignore
    
    movieRoom: MovieRoom = MovieRoom( number, seats )
    
    return movieRoom

def modifyConfig():
    
    field: str = None # type: ignore
    value: str = None # type: ignore
    
    req1 = [
        List(
            name="changeFields",
            message="¿Qué desea cambiar?",
            choices=[
                "Número",
                "Asientos",
            ]
        )
    ]
    
    res1: list = prompt(req1, theme=BlueComposure()) # type: ignore
    selectedOption = res1["changeFields"] # type: ignore
    
    if( selectedOption == "Número" ):
        field = "number"
        
        number = [
            Text(
                name="number",
                message="Nuevo Número"
            )
        ]
        
        answerNumber: list = prompt(number, theme=BlueComposure()) # type: ignore
        value = answerNumber["number"] # type: ignore
        
    elif( selectedOption == "Asientos" ):
        field = "seats"
        
        seats = [
            Text(
                name="seats",
                message="Nuevo Asientos"
            )
        ]
        
        answerSeats: list = prompt(seats, theme=BlueComposure()) # type: ignore
        value = answerSeats["seats"] # type: ignore

    else:
        print("error")
    
    return field, value # type: ignore


# * GENERAL

choicesCreate = [
    "Crear otro",
    "Salir"
]

choicesShow = [
    "Mostrar otra vez",
    "Salir"
]

choicesChange = [
    "Volver a cambiar",
    "Salir"
]

choicesDelete = [
    "Eliminar otro más",
    "Salir"
]


def selectIndexChange() -> int:
    print("")
    questions = [
        Text(
            name="index",
            message="¿Cuál deseas seleccionar?",
        ),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    index: int = int(answers["index"]) # type: ignore
    return index

def outShowOptionMenu( opt: int = 1) -> str:
    print("")
    
    if( opt == 1 ): 
        questions = [
            List(
                name="out",
                message="¿Qué deseas hacer?", 
                choices=choicesCreate,
                default=choicesCreate[0],
            ),
        ]
    elif ( opt == 2 ):
        questions = [
            List(
                name="out",
                message="¿Qué deseas hacer?", 
                choices=choicesShow,
                default=choicesShow[0],
            ),
        ]
    elif ( opt == 3 ):
        questions = [
            List(
                name="out",
                message="¿Qué deseas hacer?", 
                choices=choicesChange,
                default=choicesChange[0],
            ),
        ]
    elif ( opt == 4 ):
        questions = [
            List(
                name="out",
                message="¿Qué deseas hacer?", 
                choices=choicesDelete,
                default=choicesDelete[0],
            ),
        ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    out: str = answers["out"] # type: ignore
    return out