
'''
Promedio de números de una lista:
Escribe un programa que calcule el promedio de una lista de números. 
'''

numeros = [float(x) for x in input('Introduce una lista de números separados por espacios: ').split()]
promedio = sum(numeros) / len(numeros)
print (f'El promedio de  los nuemeros es: {promedio}')