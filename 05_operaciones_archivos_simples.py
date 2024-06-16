'''
Escribe un programa que lea un archivo de texto, convierta su contenido a mayúsculas y escriba el resultado
en nuevo archivo. Si el archivo de entrada no existe, muestra un mensaje de error. 
'''

input_file = input('Introduce el nombre del archivo inicial: ')
output_file = input('Introduce el nombre del archivo saliente: ')

try:
    with open(input_file, 'r') as infile:
        content = infile.read()
        
    uppercase_content = content.upper()
    with open(output_file, 'w') as outfile:
        outfile.write(uppercase_content)
    
    print ('El contenido has sido convertido a mayúsculas y salvado en output file.')
    
except FileNotFoundError:
    print ('El archivo no existe')