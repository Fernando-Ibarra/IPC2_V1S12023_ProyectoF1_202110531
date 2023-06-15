from inquirer import List, prompt
from inquirer.themes import BlueComposure
import os

import View.Admin.MainMenu as mainMenu
import View.Admin.Categories.categoryTools as categoryMenu
from Model.user.User import User

choices = [
    "Crear Categoria",
    "Listar Categorias",
    "Modificar Categoria",
    "Eliminar Categoria",
    "Crear Película",
    "Listar Películas",
    "Modificar Película",
    "Eliminar Película",
    "Importar XML",
    "Expotar XML",
    "Salir"
]

def toCrud( optionSelected: str = "Crear Categoria", user: User = None ): # type: ignore
    if ( optionSelected == choices[0] ):
        categoryMenu.createCategory( user )
    elif ( optionSelected == choices[1] ):
        categoryMenu.showCategories( user )
    elif ( optionSelected == choices[2] ):
        categoryMenu.modifyCategory( user )
    elif ( optionSelected == choices[3] ):
        categoryMenu.deleteCategory( user )
    elif ( optionSelected == choices[4] ):
        categoryMenu.createMovie( user )
    elif ( optionSelected == choices[5] ):
        categoryMenu.showMovies( user )
    elif ( optionSelected == choices[6] ):
        categoryMenu.modifyMovie( user )
    elif ( optionSelected == choices[7] ):
        categoryMenu.deleteMovie( user )
    elif ( optionSelected == choices[8] ):
        categoryMenu.importXML( user )
    elif ( optionSelected == choices[9] ):
        categoryMenu.exportXML( user )
    else:
        mainMenu.MainMenu( user )

def mainCrudCategories( user ):
    os.system('cls')
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
    toCrud( optionSelected, user )