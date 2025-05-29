resultado = 0
"""
while True:
    numero = int(input("Introduce numero: "))
    resultado += numero
    if numero == 0:
        # print(resultado)
        break
print(resultado)
"""

"""
while True:
    numero = input("Introduce numero: ")
    if numero.isnumeric():
        numero = int(numero)
        resultado += numero
    else:
        print("No es numerico")
        break
print(f"Numeros sumados: {resultado}")
"""


while True:
    numero = input("Introduce numero: ")
    if numero.isdigit():
        print("True")
    else:
        print("False")
        break
