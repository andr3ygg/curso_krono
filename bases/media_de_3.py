"""
# https://es.wikipedia.org/wiki/Media_ponderada
# pondera una lista de 3 elementos
def media_ponderada(lista):
    if not isinstance(lista, list):
        raise "Esto no es una lista"
    if len(lista) != 3:
        raise "Esta lista no tiene 3 elementos"

    lista_ponderda = []
    pesos = [1, 2, 4]
    ponderacion = [1/7, 2/7, 4/7,]

    for indice in range(len(lista)):
        lista_ponderda.append(lista[indice] * ponderacion[indice])

    return sum(lista_ponderda)


if __name__ == '__main__':
    print(media_ponderada([1, 2, 1]))



[1, 1, 1, 6, 1, 1, 1, 0, 1, 1, -5, 10, 7, 1, 1, 0, 0, 0, 0, 0]
--------
    -------
        -------
            -------
                -------
                    -------
                        -------
"""
import random


def media_ponderada(lista):
    pesos = []
    # lista = [6.4, 9.2, 8.1]
    for i in range(len(lista)):
        pesos.append(random.randint(1, 10))

    print(f"Lista: {lista}")
    print(f"Pesos: {pesos}")
    suma_pesos = sum(pesos)
    for i in range(len(pesos)):
        pesos[i] = pesos[i] / suma_pesos
    # pesos = [0.3, 0.2, 0.5]
    lista_ponderada = []
    resultado = 0
    aux = 0
    for i in range(len(lista)):
        # print(f"VALOR DE I EN LEN LISTA: {i}")
        aux += lista[i] * pesos[i]
        resultado = (aux / sum(pesos))
    return resultado


def generar_lista(num_limite):
    lista = []
    for i in range(0, num_limite):
        lista.append(random.randint(0, num_limite))
    return lista


def main():
    lista = generar_lista(5)
    print(media_ponderada(lista))


if __name__ == '__main__':
    main()
