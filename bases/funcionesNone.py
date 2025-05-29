def saludar (nombre):
	print(f"Hola {nombre}")
	return 5

retorno = saludar("Andrey")
print(f"El valor de retorno es: {retorno} y el tipo es: {type(saludar)}")
