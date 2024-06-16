
'''
Escribe un programa que genere los primeros números  de la secuencia de Fibnonacci. 
'''

def gereate_fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
        return sequence[:n]
n = int(input('Introduce el número para generar la secuencia de fibonacci: '))
fibonacci_sequence = gereate_fibonacci(n)
print (f'Los primero números de la sequencia son: {fibonacci_sequence}')
    

gereate_fibonacci(10)