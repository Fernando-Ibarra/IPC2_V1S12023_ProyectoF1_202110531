from inquirer import Text, prompt, Password, List
from inquirer.themes import BlueComposure
import xml.etree.ElementTree as ET
import os

from Model.user.User import User
from Model.user.NodeUser import NodeUser
import Helpers.utils as HelUtil

name: str 
lastName: str 
phoneNUmber: str 
email: str
password: str
rol: str

choicesCreate = [
    "cliente",
    "administrador"
]

choicesShowUser = [
    "Cambiar algo más",
    "Salir"
]

choicesDeleteUser = [
    "Eliminar otro más",
    "Salir"
]

choicesXMLUser = [
    "Salir",
]

def __init__(self):
    pass

def createUser( opt: int = 1) -> NodeUser:
    os.system('cls')
    
    if( opt == 1 ):
        questions = [
            Text(name='name', message="Nombres"),
            Text(name='lastName', message="Apellidos"),
            Text(name='phoneNumber', message="Teléfono"),
            Text(name='email', message="Correo Electrónico"),
            Password(name='password', message="Ingresa tu contraseña"),
        ]
    else:
        questions = [
            Text(name='name', message="Nombres"),
            Text(name='lastName', message="Apellidos"),
            Text(name='phoneNumber', message="Teléfono"),
            Text(name='email', message="Correo Electrónico"),
            Password(name='password', message="Ingresa tu contraseña"),
            List(
                name="rol",
                message="¿Qué rol tendrá?", 
                choices=choicesCreate,
                default=choicesCreate[0],
            ),
        ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    
    name = answers["name"] # type: ignore
    lastName = answers["lastName"] # type: ignore
    phoneNumber = answers["phoneNumber"] # type: ignore
    email = answers["email"] # type: ignore
    password = answers["password"] # type: ignore
    
    if( opt == 1 ):
        rol = choicesCreate[0]
    else:
        rol = answers["rol"] # type: ignore
    
    user: User = User( name, lastName, phoneNumber, email, password, rol)
    nodeUser: NodeUser = NodeUser( user )
    
    return nodeUser

def outShowOptionMenu() -> str:
    print("")
    questions = [
        List(
            name="out",
            message="¿Qué deseas hacer?", 
            choices=choicesShowUser,
            default=choicesShowUser[0],
        ),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    out: str = answers["out"] # type: ignore
    return out

def outShowOptionMenu2() -> str:
    print("")
    questions = [
        List(
            name="out",
            message="¿Qué deseas hacer?", 
            choices=choicesShowUser,
            default=choicesShowUser[0],
        ),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    out: str = answers["out"] # type: ignore
    return out

def outShowOptionMenu3() -> str:
    print("")
    questions = [
        List(
            name="out",
            message="¿Qué deseas hacer?", 
            choices=choicesDeleteUser,
            default=choicesDeleteUser[0],
        ),
    ]
    
    answers: list = prompt(questions, theme=BlueComposure()) # type: ignore
    out: str = answers["out"] # type: ignore
    return out

def outShowOptionMenu4() -> str:
    print("")
    questions = [
        List(
            name="out",
            message="¿Qué deseas hacer?", 
            choices=choicesXMLUser,
            default=choicesXMLUser[0],
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

def configModify():
    
    field: str = None # type: ignore
    value: str = None # type: ignore
    
    req1 = [
        List(
            name="changeFields",
            message="¿Qué desea cambiar?",
            choices=[
                "Nombre",
                "Apellidos",
                "Número de teléfono",
                "Correo",
                "Contraseña",
                "Rol"
            ]
        )
    ]
    
    res1: list = prompt(req1, theme=BlueComposure()) # type: ignore
    selectedOption = res1["changeFields"] # type: ignore
    
    if( selectedOption == "Nombre" ):
        field = "name"
        
        nameC = [
            Text(
                name="Name",
                message="Nuevo Nombre"
            )
        ]
        
        answerNameC: list = prompt(nameC, theme=BlueComposure()) # type: ignore
        value = answerNameC["Name"] # type: ignore
        
    elif( selectedOption == "Apellidos" ):
        field = "lastName"
        
        lastNameC = [
            Text(
                name="lastName",
                message="Nuevo Apellidos"
            )
        ]
        
        answerlastNameC: list = prompt(lastNameC, theme=BlueComposure()) # type: ignore
        value = answerlastNameC["lastName"] # type: ignore
        
    elif( selectedOption == "Número de teléfono" ):
        field = "phoneNUmber"
        
        phoneNUmberC = [
            Text(
                name="phoneNUmber",
                message="Nuevo Teléfono"
            )
        ]
        
        answerPhoneNumberC: list = prompt(phoneNUmberC, theme=BlueComposure()) # type: ignore
        value = answerPhoneNumberC["phoneNUmber"] # type: ignore
    
    elif( selectedOption == "Correo" ):
        field = "email"
        
        emailC = [
            Text(
                name="email",
                message="Nuevo Correo"
            )
        ]
        
        answerMailC: list = prompt(emailC, theme=BlueComposure()) # type: ignore
        value = answerMailC["email"] # type: ignore
    
    elif( selectedOption == "Contraseña" ):
        field = "password"
        
        passwordC = [
            Text(
                name="password",
                message="Nuevo Contraseña"
            )
        ]
        
        answerPassC: list = prompt(passwordC, theme=BlueComposure()) # type: ignore
        value = answerPassC["password"] # type: ignore
    
    elif( selectedOption == "Rol" ):
        field = "rol"
        
        rolC = [
            Text(
                name="Rol",
                message="Nuevo Rol"
            )
        ]
        
        answerRolC: list = prompt(rolC, theme=BlueComposure()) # type: ignore
        value = answerRolC["Rol"] # type: ignore
    else:
        print("error chavo")
    
    return field, value # type: ignore
    
def createUserFromXML() -> None:
    tree = ET.parse('listaUsuarios.xml')
    root = tree.getroot()
    
    for usuario in root.findall('usuario'):
        name: str = usuario.find('nombre').text # type: ignore
        lastName: str = usuario.find('apellido').text # type: ignore
        phoneNumber: str = usuario.find('telefono').text # type: ignore
        email: str = usuario.find('correo').text # type: ignore
        password: str = usuario.find('contrasena').text # type: ignore
        rol: str = usuario.find('rol').text # type: ignore

        user: User = User( name, lastName, phoneNumber, email, password, rol)
        nodeUser: NodeUser = NodeUser( user )
        HelUtil.list.push( nodeUser )
    

