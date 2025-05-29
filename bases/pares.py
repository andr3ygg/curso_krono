import random

def generar_numero ():
	return random.randint(0,9)


for i in range(10):

	numero_1 = generar_numero()
	numero_2 = generar_numero()
	#print(f"Numeros generados: {numero_1} y {numero_2}")
	if (numero_1 % 2 == 0):
		print(numero_1)

	if (numero_2 % 2 == 0):
		print(numero_2)