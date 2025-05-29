"""
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y
devuelve el valor máximo y el mínimo. Crea un programa que pida números por
teclado y muestre el máximo y el mínimo, utilizando la función anterior.
"""


def calcular_max_min(lista):
    return max(lista), min(lista)


def pedir_numeros():
    lista_numeros = []
    pedir = True
    while pedir:
        numero = float(input("Ingresa un numero: "))
        if numero == 0:
            pedir = False
        lista_numeros.append(numero)

    return calcular_max_min(lista_numeros)


def main():
    maximo, minimo = calcular_max_min([1, 4, 6, -1, 20, -4, 9, -2, 12, -5])
    print(f"""Número máximo: {maximo}
Numero minimo: {minimo}""")

    # 2 Programa (Pedir numeros y devolver max y min)
    maximo_usuario, minimo_usuario = pedir_numeros()
    print(f"""Numero maximo ingresado: {maximo_usuario}
Numero minimo: {minimo_usuario}""")


main()
