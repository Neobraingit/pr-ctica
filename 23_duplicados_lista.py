
'''
Eliminar duplicado de una lista:
Escribe un programa que tome una lista y devuelva una lista sin duplicados. 
'''
lista = input('Introduce una lista de elementos separados por espacios: ').split()
lista_unica = list(dict.fromkeys(lista))
print (f'La lista con los elementos duplicados es: {lista_unica}')