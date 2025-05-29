def calcular_circunferencia(area):
    PI = 3.1416
    return (PI * area**2), ((2 * PI) * area)


def main():
    area, perimetro = calcular_circunferencia(10)
    print(f"""Area: {area:.3f}
Perimetro: {perimetro}""")


main()
