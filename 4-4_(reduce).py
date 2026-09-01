from functools import reduce
import os

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total  = reduce(
    lambda acumulador, p: acumulador + p['preco'],
    produtos,
    0   # Se não tiver esse 0, o reduce pega o primeiro dicionário como valor no acumulador,
        # logo, vai somar um dict com um int
)

os.system('cls')
print('Total é', total)