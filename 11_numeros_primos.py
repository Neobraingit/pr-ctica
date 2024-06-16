
'''
Comprobador de números primos:
Escribe una función que compruebe si un número es primo o no. 
'''

def numero_primo():
    numero = int(input('Introduce  un número: '))
    for i in range (2, numero):
        if numero % i == 0:
            print (f'{numero} es primo')
        else:
            print (f'{numero} no es primo')
            

numero_primo()