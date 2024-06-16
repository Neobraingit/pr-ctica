'''
Calcular el área de un círculo:
Escribe un programa que tome el radio de un círculo como entrada y calcule su área.
'''

import math

radio = float(input('Introduce el radio del círculo: '))
area = math.pi * (radio ** 2)
print (f'El área del círculo es: {area}')