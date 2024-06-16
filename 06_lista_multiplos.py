
'''
Escribe un programa que tome un número como entrada y devuelva una lista con sus diez primeros múltiplos. 
'''

numero = int(input('Introduce un número: '))

multiplos = [numero * i for i in range(1, 11)]
print (f'Los diez primeros múltiplos de {numero} son: {multiplos}')
 