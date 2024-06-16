
'''
Contar vocales en una cadena de texto:
Escribe un programa que cuente el número de vocales de una cadena de texto.
'''

def contar_vocales():
    cadena_texto = input('Introduce una cadena de texto: ')
    vocales = 'aeiou'
    contador_vocales = {}
    for i in cadena_texto:
        if i in vocales:
            if i in contador_vocales:
                contador_vocales[i]+=1
            else:
                contador_vocales[i] = 1
    print ('Contador de vocales: ', contador_vocales)
    
    
contar_vocales()
        