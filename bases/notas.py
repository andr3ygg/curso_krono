def media(suma_total_numeros, cantidad_valores):
    return suma_total_numeros / cantidad_valores
    # Función no necesaria. Se puede anular -> lin:25

def introducir_numero(minimo, maximo):
    nota =

def main():
    try:
        contador = 0
        suma_total = 0
        lista_suma = []
        while contador < 7:
            try:
                """
                if contador >= 7:
                    print(f"Media: {media(suma_total, contador):.1f}")
                    print(f"Media: {suma_total/contador:.1f}")
                    # Calcula la media con la suma total / contador
                    break
                """
                nota = float(input(f"Nota {contador+1}: "))

                if (nota < 0 or nota > 10):
                    print("Debe ser entre 0 y 10")
                else:
                    suma_total += nota
                    contador += 1

            except ValueError as error:
                print(error)
                exit()

            # suma_total += nota
            # contador += 1
        # Fin del bucle While
        print(f"Media: {media(suma_total, contador):.1f}")
        # Suma total y contador en scope
    except KeyboardInterrupt:
        print("")
        print("Has salido del programa")


if __name__ == '__main__':
    main()
