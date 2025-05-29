RESULTADO = 0
NUMERO_ITERACIONES = 0
LISTA_RESUMEN = []
LISTA_NUMEROS = []


def obtener_numero():
    numero = float(input("Numero: "))
    # Casting number
    if numero % 1 == 0:
        numero = int(numero)
    return numero


"""

Casting function moved to obtener_numero
def casting_numbers(num):
    if num % 1 != 0:
        num = float(num)
    elif num % 1 == 0:
        num = int(num)
    else:
        return "ERROR"
    return num

"""

"""
def calc_media(numero_sumado, NUMERO_ITERACIONES):
    return round(numero_sumado / NUMERO_ITERACIONES, 2)
"""


def calc_media(lista):
    auxiliar = 0
    for i in range(len(lista)):
        # print("CALC MEDIA")
        auxiliar += lista[i]
        # print(f"Aux: {auxiliar}")
    return auxiliar / len(lista)


def calc_media_lista(lista, ultimo):
    try:
        if ultimo > len(lista):
            # Si es mayor lo que pide, que imprima toda la lista

            ultimo = len(lista)

        auxiliar = 0
        # Para guardar la suma total de los items de la lista
        # print(f"Numero dado por el usuario: {ultimo}")
        lista_nueva = []
        # print(f"LISTA NUEVA: {lista_nueva}")

        for i in range(0, ultimo):
            # Agrega los ultimos numeros según el numero ingresado por el usuario
            lista_nueva.append(lista.pop())
            # Quita el ultimo item y lo agrega a lista_nueva

        print(f"LISTA NUEVA: {lista_nueva}")

        # Itero la longitud de la lista_nueva y sumo los items
        # en base a eso hago la media
        for i in range(0, len(lista_nueva)):
            auxiliar += lista_nueva[i]
        print(f"SUMA TOTAL: {auxiliar}")
        return auxiliar / len(lista_nueva)

    except Exception as err:
        print(err)


def resumen(lista, media, RESULTADO):
    # print("LISTA FINAL:",lista)
    for i in range(0, len(lista) - 1, 2):
        print(f"La media de {lista[i]} es: {lista[i+1]}")

    print(f"Suma de los numeros: {RESULTADO}")
    # Format a float
    print(f"Media: {media:.2f}")


while True:
    try:
        numero = obtener_numero()
        if numero == 0:
            print()
            # resumen(LISTA_RESUMEN, media, RESULTADO)

            ultimas_pos = int(input("Ultimos numeros a imprimir: "))
            print(calc_media_lista(LISTA_NUMEROS, ultimas_pos))

            # print(LISTA_NUMEROS[ultimas_pos-1:])

            break
        # ELSE
        NUMERO_ITERACIONES += 1
        RESULTADO += numero
        LISTA_NUMEROS.append(numero)
        # media = calc_media(RESULTADO, NUMERO_ITERACIONES)
        media = calc_media(LISTA_NUMEROS)
        # print(f"Media de {RESULTADO} (/{NUMERO_ITERACIONES}): {media}")
        # else:
        # numero = casting_numbers(numero)
        LISTA_RESUMEN.append(RESULTADO)
        LISTA_RESUMEN.append(media)
        # print(f"Lista: {LISTA_RESUMEN}")
        # print(f"Media de {RESULTADO}: {media}")
    except ValueError as error:
        print("Solamente se pueden ingresar numeros")
        # print(error)
        break
