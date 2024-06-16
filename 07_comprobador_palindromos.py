
'''
Comprobador de palíndromo:
Escribe un programa que compruebe  si una palabra es un palíndromo.
'''


palabra = input('Introduce una palabra: ')
if palabra == palabra[::-1]:
    print ('Es palíndromo.')
else:
    print ('No es un palíndromo')