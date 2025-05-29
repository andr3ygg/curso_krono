"""
Crear una función recursiva que permita calcular el factorial de un número.
Realiza un programa principal donde se lea un entero
y se muestre el resultado del factorial.

5! = 1 x 2 x 3 x 4 x 5

de 1 hasta 5

(5-1)   x   5
4   x   5
(5-2)   x   5
3   x   5
(5-3)   x   5
2   x   5
(5-4)   x   5
1   x   5
(5-5)   x   5
0   x   5

for i in range (1,n)
    print((n-i) * n)
"""


def factorial(n):
    resultado = 1
    num = 1
    for i in range(0, n-1):
        num = n-i
        resultado *= num
    print(f"Factorial de {n} es: {resultado}")


def main():
    numero = int(input())
    factorial(numero)


main()
