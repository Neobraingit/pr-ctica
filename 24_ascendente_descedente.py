
'''
Ordenar una lista en orden ascendente y descendente:
Escribe un programa que tome una lista de números como entrada y devuelva la misma lista ordenada
ascendente y descendentemente. 
'''

lista_numeros = []
while True:
    numeros = int(input('Introduce números para configurar la lista: '))
    if len(lista_numeros) <= 10:
            lista_numeros.append(numeros)
    else:
         print ('No se admiten más números...')
         break
    
print (sorted(lista_numeros))