
'''
Calculadora simple:
Escribe un programa que pueda hacer sumas, restas, divisiones y multiplicaciones. 
El programa debe pedir la operación y los dos números. 
'''
numero_1 = int(input('Introduce un número: '))
numero_2 = int(input('Introduce otro número: '))
def suma():
    print (numero_1 + numero_2)
    
def resta():
    print (numero_1 - numero_2)
    
def multiplicacion():
    print (numero_1 * numero_2)
    
def division():
    print (numero_1 / numero_2)
    
while True:
    print ('--- OPCIONES --- ')
    print (' 1) Sumar\n', '2) Restar\n', '3)Multiplicar\n', '4)Dividir')
    opcion = input('Introduce la opción: ')
    if opcion == '1':
        suma()
    elif opcion == '2':
        resta()
    elif opcion == '3':
        multiplicacion()
    elif opcion == '4':
        division()
    break
else:
        print ('Escoge una opción correcta')
    