import os
import textwrap
# Print the size of terminal


def cuadricula(col, lines, relleno):
    margen = 4
    print(f"╔" + "═" * (col-margen) + "╗")
    # for i in range(col):
    for i in relleno:
        # RELLENO
        print("║" + i + "║")

    print(f"╚" + "═" * (col-margen) + "╝")


def contadores(col, lines):
    margen = 4
    contador_derecha = 0
    contador_izquierda = 0
    print(f"Contador derecha: {contador_derecha}" + f"contador_izquierda: {contador_izquierda}".rjust(lines-margen))


def main():
    valor = """This function wraps the input paragraph such that each line
in the paragraph is at most width characters long. The wrap method
returns a list of output lines. The returned list
is empty if the wrapped
output has no content."""
    wrapper = textwrap.TextWrapper(width=50)
    word_list = wrapper.wrap(text=valor)
    col, lines = os.get_terminal_size()
    contadores(col, lines)
    cuadricula(col, lines, word_list)


main()