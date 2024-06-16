
'''
Escribe un programa que tome una cadena de texto como entrada y cuente la frecuencia de cada palabra en la cadena. 
'''

def contador():
    cadena = input('Introduce la cadena de texto: ')
    palabras = cadena.lower().split()
    contador_palabras = {}
    
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1
    print (f'Frecuencia de palabras: ', contador_palabras)

    
    
    
    
while True:
    print ('1) Contar frecuencia de palabras')
    opcion  = input('Introduce tu opción: ')
    if opcion == '1':
        contador()
    else:
        print ('Introduce una opción válida')
    