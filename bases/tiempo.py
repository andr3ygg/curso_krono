def pedir_temp():
    minima = float(input(f"Temperatura minima: "))
    maxima = float(input(f"Temperatura maxima: "))
    return minima, maxima


def calcular_media(minimo, maximo, divisor):
    return (minimo + maximo) / divisor


def main():
    dias = int(input("Dias a calcular: "))
    contador = 0
    media_semanal = 0

    while contador < dias:
        print(f"DIA: {contador+1}")
        minima, maxima = pedir_temp()
        print(f"Media: {calcular_media(minima, maxima, 2)}")
        contador += 1


main()
