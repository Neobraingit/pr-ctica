
'''
Contar ocurrencias de un caracter:
Escribe un programa que cuente las ocurrencias de un caracter dentro de una cadena de texto. 
'''

cadena = input('Introduce una cadena de texto: ')
letras_a_contar = input('Introduce la letra a contar: ')
contador = cadena.lower().count(letras_a_contar.lower())
print (f'La letras {letras_a_contar} sale un total de {contador} veces.')