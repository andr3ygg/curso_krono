import random


def generar_lista (max_items):
	lista = []
	for i in range(0,max_items):
		lista.append(int(random.random()*100))
	return lista


def ordenar_array (lista):
	print(f"INPUT: {lista}")
	for indice_lista in range(0, len(lista)-1):
		# print(f"Indice lista: {indice_lista}")
		for sub_indice in range (0, len(lista)-1):
			# print(f"Iteracion: {iteracion}")
			if lista[sub_indice] > lista[sub_indice+1]: #j+1 = 8
				numero = lista[sub_indice] # 9
				lista[sub_indice] = lista[sub_indice+1] # 9 = 8
				lista[sub_indice+1] = numero #
	return lista


lista = generar_lista(10)
lista_ordenada = ordenar_array(lista)
print(lista_ordenada)

"""
indice_lista = 0 (0 a 6, 6 vueltas)
j = 0 (0 a 6, 6 vueltas)

lista[j] = 9 || lista[j+1] = 8
Si 9(j) es mayor que 8(j+1), guardo 9(j) porque es el numero que sobreescribo. lista[j] = 9 ahora es j+1 8. => 8,8
Ahora, la j (9) que guardé, lo pongo el posición que estaba b (j+1) 
LISTA ACTUALIZADA: 8,9,7,9,5,2,1
indice_lista 1 & j = 1
DESDE 0 A 1

1 vuelta: 9,8,7,9,5,2,1 => trabaja desde 0 a 0, una sola vez -> 9 > 8: cambio posicion
2 vuelta: 8,9,7,9,5,2,1 => trabaja desde 0 a 1, 8 > 9X; 9 > 7: cambio posicion
3 vuelta 8,7,9,5,2,1 => trabaja desde 0 a 2, 8 > 7: cambio posicion. 8 > 9X; 9 > 5: cambio posicion
4 vuelta 7,8,5,9,2,1 => trabaja desde 0 a 3, 7>8X: 8>5:cambio; 8>9X; 9>2: cambio posicion
5 vuelta 7,5,8,2,9,1 => trabaja desde 0 a 4, 7>5:cambios; 7>8X; 8>2:cambio; 8>9X 9>1:cambio
6 vuelta 5,7,2,8,1,9 => trabaja desde 0 a 5, 5>7X: 7>2:cambio: 7>8X: 8>1:cambio: 8>9x
7 vuelta 5,2,7,1,8,9 => trabaja desde 0 a 6, 5>2:cambio: 5>7x 7>1:cambio:7>8:8>9
8 vuelta 2,5,1,7,8,9 => trabaja desde 0 a 7, 2>5,5>1:cambio,5>7,7>8,8>9
9 vuelta 2,1,5,7,8,9 => trabaja desde 0 a 8, 2>1:cambio,2>5,5>7,7>8,8>9
10 vuelta 1,2,5,7,8,9 

















"""