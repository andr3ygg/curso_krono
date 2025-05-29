RESULTADO = 0
NUMERO_ITERACIONES = 0
LISTA_RESUMEN = []


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


def calc_media(numero_sumado, NUMERO_ITERACIONES):
    return round(numero_sumado / NUMERO_ITERACIONES, 2)


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
            resumen(LISTA_RESUMEN, media, RESULTADO)
            break

        NUMERO_ITERACIONES += 1
        RESULTADO += numero
        media = calc_media(RESULTADO, NUMERO_ITERACIONES)
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
