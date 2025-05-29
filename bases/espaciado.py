def convertir_espaciado(texto):
    return ' '.join(texto)


def main():
    texto_usuario = input("String: ")
    print(convertir_espaciado(texto_usuario))


main()
