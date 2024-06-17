
'''
Suma de dígitos de un número:
Escribe un programa que calcule la suma de los dígitos de un número. 
'''

numero = int(input('Introduce un entero: '))
suma_digitos = sum(int(digit)for digit in str(numero))
print (f'La suma de los digitos del número {numero} es {suma_digitos}')
    
