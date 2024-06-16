
'''
Año bisisesto:
Escribe un programa que compruebe si un año es bisiesto. 
'''

ano  = int(input('Introduce un año para saber si es bisiesto: '))

def calcular_bisisesto():
    if ano % 4 == 0:
        print ('Es bisisesto...')
    else:
        print ('No es bisisiesto...')
        

calcular_bisisesto()