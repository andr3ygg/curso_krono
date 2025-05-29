contador = 100
#Mientras que contador sea mayor a 0 (actually vale 10), entonces entra
# Y cada vez que entra imprime el valor y le resta 1, por lo cual
#ira de 10 hasta que sea mayor a 0, es decir, el mismo 0
while contador > 0:
    print(contador, end=" ")
    #print(f" Valor del contador antes de restar 1:{contador}")
    # contador - 1 => estamos referenciando pero no estamos guardando el valor (Asignacion)
    if (contador % 10 == 0):
        #print()
        print()
    contador-=1

    # Contador decrementado en 1 y asignado a contador
    #Se ejecuta primero la operacion y despues se asigna
    #print(f"Valor del contador despues de restar 1, es el proximo a validar: {contador}")
    """"
    if contador == 0:
        print("Despegue")  """
#print()
#print("Despegue")

contador_dos = 0
while contador_dos <= 100:
    print(contador_dos, end=" ")
    if (contador_dos % 10 == 0):
        print()
    contador_dos += 1

#print(f"Valor del contador :{contador}")