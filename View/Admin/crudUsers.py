from inquirer import List, prompt
from inquirer.themes import BlueComposure
import os

choices = [
    "Crear Usuario",
    "Listar Usuarios",
    "Modificar Usuario",
    "Eliminar Usuario",
    "Importar XML",
    "Expotar XML"
    "Salir"
]

def mainCrudUser():
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