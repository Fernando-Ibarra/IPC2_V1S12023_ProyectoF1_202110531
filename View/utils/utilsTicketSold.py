from inquirer import Text, prompt, List
from inquirer.themes import BlueComposure
from colorama import Fore
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

choicesShow = [
    "Mostrar otra vez",
    "Salir"
]

choicesCancele = [
    "Cancelar otro más",
    "Salir"
]


def outShowOptionMenu( opt: int = 1) -> str:
    print("")
    
    if( opt == 1 ): 
        questions = [
            List(
                name="out",
                message="¿Qué deseas hacer?", 
                choices=choicesShow,
                default=choicesShow[0],
            ),
        ]
    elif ( opt == 2 ):
        questions = [
            List(
                name="out",
                message="¿Qué deseas hacer?", 
                choices=choicesCancele,
                default=choicesCancele[0],
            ),
        ]    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    out: str = answers["out"] # type: ignore
    return out

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