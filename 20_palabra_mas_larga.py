'''
 Palabra más larga de una oración:
 Escribe una programa que muestre la palabra más larga de una oración. 
 '''
 
oracion = input('Introduce una frase: ').split()
palabras = ''
maximo_longitud = 0
for palabra in oracion:
    if len(palabra) > maximo_longitud:
        maximo_longitud = len(palabra)
        palabra_mas_larga = palabra
print (f'La palabra más larga en la oración es: {palabra_mas_larga}')    

 
 