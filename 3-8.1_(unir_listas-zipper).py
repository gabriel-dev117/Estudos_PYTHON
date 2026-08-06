# Exercício - Unir Listas
# Crie uma função zipper
# O trabalho dessa função será unir duas listas na ordem
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG'), ('RJ')]

# -------------------------------------------------------

"""
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']


qtd_estado = len(estados)

local = []

def zipper(x, y):
    if len(y) > len(x):
        decisao = y

    else:
        decisao = y

    
    try:
        for i in range(len(decisao) + 1):
            n += 1
            cid_est = (x[i], y[i])
            local.append(cid_est)

    except IndexError:
        est = (y[i])
        local.append(est)

    return 


zipper(cidades, estados)

print(local)
"""

# --------------------------------------------------------------------------

"""
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    min_lista = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(min_lista)]


z = zipper(cidades, estados)

print(z)
"""

from itertools import zip_longest


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte'] 
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip_longest(l1, l2)))

