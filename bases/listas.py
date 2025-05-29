"""
lista[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output: [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
"""
# NEW TYPE OF DATE: LIST
# NUM LISTA ALEATORIOS E IMPRIMIR INTERCAMBIADO PAREJAS
# PRIMERO IMPART Y LUEGO PAR
# IN: 33 (1) 30 (2)
# OUT: 30 (2) 33 (1)

import random

lista_numeros = []


for i in range(9):
    lista_numeros.append(random.randint(0, 9))

print(f"INPUT: {lista_numeros}")
longitud_lista = len(lista_numeros)
# print(f"Longitud de la lista: {longitud_lista}")
for i in range(0, longitud_lista - 1, 2):  # 0,2,4,6,8 directa; 1,3,5,7 indirecta
    # print(i)
    item1 = lista_numeros[i]  # ITEM 1 = 0,2,4,6,8
    item2 = lista_numeros[i + 1]  # ITEM 2 = 1,3,5,7,9
    # Longitud: 10
    # Longitud - 1 porque comienza desde 0 y no desde 1, entonces en sistema decimal tendría 1 más (el cero)
    # Si es impar, el ultimo item no se toca porque hay un -1 en la longitud
    """
	item1 = 0			=>  1
	item 2 = 0+1 (1)	=>	2
	lista[i(0)] = item2 (2) => lista[0] = 2
	lista[i+1(1)] = item1 (1) => lista[1] = 1

	item1 = 2  (3)		=> 
	item2 = 2+1 (4)		=>
	lista[i]			=> 2 (3)
	lista[i+1]			=> 3 (4)
	lista[i] = item2	=> 3 = 4
	lista[i+1] = item1	=> 4 = 3
	(...)
	item1 = 6			=> 7
	item2 = 7			=> 8	LONGITUD = 9 (THIS CASE) SO LET'S LESS 1 NUMBER = 8 => CUENTA HASTA AQUÍ


	"""
    """
	lista_numeros[i] = item2
	lista_numeros[i+1] = item1
	"""
    # print(f"""{lista_numeros[i]} {lista_numeros[i+1]}""")
    # print(lista_numeros)
    print(f"{item2} {item1}")
# print(f"OUTPUT: {lista_numeros}")
