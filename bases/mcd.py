"""
Crear una función que calcule el MCD de dos número por el método de Euclides.
 El método de Euclides es el siguiente:

    Se divide el número mayor entre el menor.
    Si la división es exacta, el divisor es el MCD.
    Si la división no es exacta, dividimos el divisor entre el resto obtenido
     y se continúa de esta forma hasta obtener una división exacta, s
     iendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD.
"""


def calcular_numero(num1, num2):
    numero_mayor = max(num1, num2)
    numero_menor = min(num1, num2)
    resto = numero_mayor % numero_menor





def main():
    pass


main()
