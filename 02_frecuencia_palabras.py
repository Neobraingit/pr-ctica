
'''
Escribe un programa que tome una cadena de texto como entrada y cuente la frecuencia de cada palabra en la cadena. 
'''


cadena = input('Introduce la cadena: ')
palabras = cadena.lower().split()
contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print ('Frecuencia de palabras: ', contador_palabras)