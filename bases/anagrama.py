"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""
string1 = "nepal"
string2 = "panel"
auxiliar = 0
for letra in string1:
	if string2.find(letra) != -1:
		auxiliar += 1
	else:
		auxiliar -= 1

if string1 == string2:
	print("NO ES ANAGRAMA PORQUE SON IGUALES")
else:
	if auxiliar >= 1:
		print("Es anagrama")	
	else:
		print("No es anagrama")	
