
'''
        Elementos comunes en dos listas: 
        Escribe un programa que tome dos listas y devuelva una lista de elementos comunes,
        
'''

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 1, 2]
lista_resultado = []

for i in lista_1:
    for g in lista_2:
        if i in lista_1 and i in lista_2:
            lista_resultado.append(i)
            if g in lista_2 and g in lista_1:
                lista_resultado.append(g)
                break
                
print (lista_resultado)