# resultado_resta = 0

"""def generar_error(tipo_error, mensaje_error):
    raise tipo_error(mensaje_error)
"""


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "No se puede dividir entre 0"

    # IF STATEMENT
    """
    if num2 == 0:
        print("No se puede dividir un numero entre 0")
    else:
        print(f"resultado: {num1 / num2}")
    """

    # Raise Exception
    """
    if num2 == 0:
        raise Exception("No se puede divivir un numero entre 0")
    """


def suma_infinita(*args):
    print(f"Total: {sum(args)}")


def resta_infinita(*args):
    resultado = args[0]
    print("resultado: ", resultado)
    for x in args:
        resultado -= x
    # for j in lista:
        # resultado = j
        # resultado -= int(j)
    return resultado + args[0]


# print(resta_infinita(20,10,10,5,5)) # OUTPU: -10
def multiplicacion_infinita(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

# print(multiplicacion_infinita(5,2,3,2)) # OUTPUT 60


def division_infinita(*args):
    resultado = 1
    lengh_tuple = len(args)
    for i in args:
        print(f"VALOR DE I {i}")
        print("RESULTADO DE ITERACION:")
        resultado /= i
        print(resultado)
    return resultado


print(division_infinita(10, 2))
# division_infinita(10,2)
# print(suma(10,10)) # OUTPUT = 20
# print(resta(20,10)) # OUTPUT = 10
# print(multiplicacion(5,2)) # OUTPUT = 10
# print(division(50,2)) # OUTPUT = 25

# suma_infinita(5,5,5,5)