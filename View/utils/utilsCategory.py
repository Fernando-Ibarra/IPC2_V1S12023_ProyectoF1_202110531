from inquirer import Text, prompt, List
from inquirer.themes import BlueComposure
from colorama import Fore
import xml.etree.ElementTree as ET
import os

from Model.category.Category import Category
from Model.movie.LinkedListMovie import LinkedListMovie, Movie, NodeMovie
from main import ListCategory

def __init__(self):
    pass

# * CATEGORY
def createCategory() -> Category:
    os.system('cls')
    
    questions = [
            Text(name='name', message="Nombre"),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    
    name = answers["name"] # type: ignore
    
    movies = LinkedListMovie()
    
    category = Category( name, movies )
    return category

def modifyCategory()-> str:
    os.system('cls')
    
    questions = [
            Text(name='name', message="Nuevo Nombre"),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore

    name = answers["name"] # type: ignore
    return name

# * Movies

title: str 
director: str 
year: str 
date: str
time: str

def createMovie() -> NodeMovie:
    questions = [
        Text(name='title', message="Titulo"),
        Text(name='director', message="Director"),
        Text(name='year', message="Año"),
        Text(name='date', message="Fecha"),
        Text(name='time', message="Hora"),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    
    title: str = str( answers["title"] ) # type: ignore
    director: str = str( answers["director"] ) # type: ignore
    year: str = str( answers["year"] ) # type: ignore
    date: str = str( answers["date"] ) # type: ignore
    time: str = str( answers["time"] ) # type: ignore
    
    movie: Movie = Movie( title, director, year, date, time )
    nodeMovie: NodeMovie = NodeMovie( movie )
    return nodeMovie

def modifyMovie():
    
    field: str = None # type: ignore
    value: str = None # type: ignore
    
    req1 = [
        List(
            name="changeFields",
            message="¿Qué desea cambiar?",
            choices=[
                "Titulo",
                "Director",
                "Año",
                "Fecha",
                "Hora"
            ]
        )
    ]
    
    res1: list = prompt(req1, theme=BlueComposure()) # type: ignore
    selectedOption = res1["changeFields"] # type: ignore
    
    if( selectedOption == "Titulo" ):
        field = "title"
        
        titleN = [
            Text(
                name="title",
                message="Nuevo Titulo"
            )
        ]
        
        answertitleN: list = prompt(titleN, theme=BlueComposure()) # type: ignore
        value = answertitleN["title"] # type: ignore
    elif( selectedOption == "Director" ):
        field = "director"
        
        directorN = [
            Text(
                name="director",
                message="Nuevo Director"
            )
        ]
        
        answerdirectorN: list = prompt(directorN, theme=BlueComposure()) # type: ignore
        value = answerdirectorN["director"] # type: ignore
    elif( selectedOption == "Año" ):
        field = "year"
        
        yearN = [
            Text(
                name="year",
                message="Nuevo Año"
            )
        ]
        
        answeryearN: list = prompt(yearN, theme=BlueComposure()) # type: ignore
        value = answeryearN["year"] # type: ignore
    elif( selectedOption == "Fecha" ):
        field = "date"
        
        dateN = [
            Text(
                name="date",
                message="Nuevo Fecha"
            )
        ]
        
        answerdateN: list = prompt(dateN, theme=BlueComposure()) # type: ignore
        value = answerdateN["date"] # type: ignore
    
    elif( selectedOption == "Hora" ):
        field = "time"
        
        timeN = [
            Text(
                name="time",
                message="Nuevo Hora"
            )
        ]
        
        answertimeN: list = prompt(timeN, theme=BlueComposure()) # type: ignore
        value = answertimeN["time"] # type: ignore
    else:
        print("error")
    
    return field, value # type: ignore

# * GENERAL

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

choicesXML = [
    "Salir",
]

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
    elif ( opt == 5):
        questions = [
            List(
                name="out",
                message="¿Qué deseas hacer?", 
                choices=choicesXML,
                default=choicesXML[0],
            ),
        ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    out: str = answers["out"] # type: ignore
    return out

def createDataFromXMLCa() -> None:
    tree = ET.parse('listaPeliculas.xml')
    root = tree.getroot()

    for categoria in root.findall('categoria'):
        name: str = categoria.find('nombre').text # type: ignore
        movies = LinkedListMovie()
        for pelicula in categoria.findall('peliculas/pelicula'):
            title: str = pelicula.find('titulo').text # type: ignore
            director: str = pelicula.find('director').text # type: ignore
            year: str = pelicula.find('anio').text # type: ignore
            date: str = pelicula.find('fecha').text # type: ignore
            time: str = pelicula.find('hora').text # type: ignore
            
            movie: Movie = Movie( title, director, year, date, time )
            movieNode: NodeMovie = NodeMovie( movie )
            
            movies.push(movieNode)
            
        category: Category = Category(name, movies)
        ListCategory.push(category)