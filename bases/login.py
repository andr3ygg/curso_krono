"""
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una
contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1”
y la contraseña es “asdasd”. Además recibe el número de intentos que se ha
 intentado hacer login y si no se ha podido hacer login incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y una contraseña
 y se intente hacer login, solamente tenemos tres oportunidades para intentarlo
"""


def pedir_datos():
    try:
        usuario = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
    except Exception as err:
        print("Ha ocurrido un error", err)

    return usuario, contrasena


def login():
    numero_intentos = 3
    condicion = None
    while numero_intentos > 0:
        usuario, contrasena = pedir_datos()
        if usuario == "andrey" and contrasena == "1234":
            return True
        else:
            print("Datos incorrectos")
            condicion = False
        numero_intentos -= 1
    return condicion


def main():
    # usuario, contrasena = pedir_datos()
    print(login())


main()
