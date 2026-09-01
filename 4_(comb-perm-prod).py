import os
from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

os.system('cls')
print_iter(combinations(pessoas, 2))
print("-------------------------------")
print_iter(permutations(pessoas, 2))
print("-------------------------------")
print_iter(product(*camisetas))