from inquirer import List, Text, prompt
from inquirer.themes import BlueComposure
import os

from Model.user.User import User
from Model.movie.Movie import Movie
from Model.favMovie.favMovie import favMovie
from Model.category.CircularlyLinkedListCategory import NodeCategory
from View.Admin.Categories.categoryTools import showMoviesMovieMenu
import View.Client.MainMenu as mainMenu
from main import listFavMovie

choices = [
    "Marcar alguna como favorita",
    "Salir"
]

def __init__( self ):
    pass

def mainMovieListMenu( user: User ):
    os.system('cls')
    
    nodeCategory: NodeCategory = showMoviesMovieMenu()
    
    questions = [
        List(
            name="firstOption",
            message="¿Qué deseas hacer?", 
            choices=choices,
            default=choices[0],
        ),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    optionSelected: str = answers["firstOption"] # type: ignore
    if ( optionSelected == choices[0] ):
        req1 = [
            Text(name='numberMovie', message="¿Cuál desea marcar?"),
        ]
        
        res1: list = prompt(req1, theme=BlueComposure()) # type: ignore
        number: int = int(res1["numberMovie"]) # type: ignore
        
        movie: Movie = nodeCategory.category.movies.findMovie( number )

        movieFav = ( user.name, user.lastName, user.email, movie.title, movie.director, movie.year, movie.date, movie.title )
        
        listFavMovie.append( movieFav )
        
        print("Película agregada a favoritos")
        
        mainMovieListMenu( user )
    else:
        mainMenu.MainMenu( user )