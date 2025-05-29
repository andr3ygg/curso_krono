import random

lista = [9,8,5,2,7,1,8,9,5,5]
posicion = 0
numero_items = int(random.random() * 100)
"""for i in range(numero_items):
    lista.append(random.randint(1, 9)) """

longitud_lista = len(lista)
print(f"INPUT: {lista}")
while posicion < (longitud_lista - 1):
    """
    item1 = lista[posicion] # posicion = 0
    item2 = lista[posicion+1] # 0+1
    lista[posicion] = item2
    lista[posicion+1] = item1
    print(lista)
    """
    item1 = lista[posicion]  # posicion = 0
    item2 = lista[posicion + 1]  # 0+1
    posicion += 2
    # == for i in range(0,l,2)
