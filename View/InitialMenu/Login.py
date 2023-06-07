from inquirer import Text, Password

def LoginMenu():
    questions = [
        Text(name='email', message="Ingresa tu correo electrónico"),
        Password(name='password', message="Ingresa tu contraseña")
    ]
    