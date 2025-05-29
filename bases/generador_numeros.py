import random

def generar_numero ():
	return random.randint(0,9)

for i in range(10):
	numero_random = generar_numero() #Tomar cajita 1 y guardarla
	#numero_random_2 = generar_numero() #Tomar cajita 2 y guardarla

	print(f"""Input: {numero_random} y {numero_random_2}""")
	#print(i, numero_random_2)
	print(i, generar_numero() ) #No deja la cajita en el suelo sino que lo lleva directamente a la salida
	print(f"  {numero_random}")
# INPUT: 9 8
# OUTPUT = 8 9
# INVERTIR EL ORDEN DE PAREJAS