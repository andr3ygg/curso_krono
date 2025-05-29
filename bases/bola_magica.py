import random

# Crear una función
# Devolver una respuesta aleatoria de la lista dada

"""
def devolver_respuesta(lista):
    return lista[random.randint(0, len(lista)-1)]
"""


def main():
    arrayRespuestas = [
        'Es cierto.',
        'Es decididamente así.',
        'Sin lugar a dudas.',
        'Sí, definitivamente.',
        'Puedes confiar en ello.',
        'Como yo lo veo, sí.',
        'Lo más probable.',
        'Perspectiva buena.',
        'Sí.',
        'Las señales apuntan a que sí.',
        'Respuesta confusa, vuelve a intentarlo.',
        'Vuelve a preguntar más tarde.',
        'Mejor no decirte ahora.',
        'No se puede predecir ahora.',
        'Concéntrate y vuelve a preguntar.',
        'No cuentes con ello.',
        'Mi respuesta es no.',
        'Mis fuentes dicen que no.',
        'Muy dudoso.'
        'Las perspectivas no son muy buenas.',
    ]

    # print(arrayRespuestas[random.randint(0, len(arrayRespuestas)-1)])
    print(random.choice(arrayRespuestas))


if __name__ == '__main__':
    main()
