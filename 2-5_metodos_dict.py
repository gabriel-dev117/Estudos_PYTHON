# Métodos úteis nos dicionários Python


# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existir
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apafa o último iteem adicionado
# update - atualiza um dicionário com outro

pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Moura Lima',
    'idade': 707,
}

pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
print(f'Quantas chaves tem no dicionário usando print(len(pessoa)):'
      f'{len(pessoa)}')
print('---------------------------')
print(f'Quais chaves tem no dicionário usando print(list(pessoa.keys())):'
      f'{list(pessoa.keys())}')
print('---------------------------')
print(f'Quais valores tem no dicionário usando print(list(pessoa.values())):'
      f'{list(pessoa.values())}')
print('---------------------------')
print(f'Quais itens tem no dicionário usando print(list(pessoa.items())):'
      f'\n{list(pessoa.items())}')
print('---------------------------')

for valor in pessoa.values():
    print(valor)

print('---------------------------')

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

import copy
d2 = d1 # -> desse jeito, se eu alterar o dicionário d2, o d1 também muda

# d2 = d1.copy()  -> desse jeito ele altera somente o imutável do dicionário d2,
#                    mas se eu alterar a lista do d2 ele também altera a lista do d1.

# d2 = copy.deepcopy(d1) -> agora sim, eu conseigo alterar valores do dicionário d2
#                           sem alterar o dicionário d1

d2['c2'] = 99
d2['l1'][0] = 100

print(d1)
print(d2)

print('---------------------------\n\n\n\n\n\n')

p1 = {
    'nome': 'Gabriel',
    'sobrenome': 'Lima',
    'idade': 23,
}

# print(p1.get('nome'), p1.get('sobrenome'))

# nome = p1.pop('sobrenome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'Guillermo',
#     'sobrenome': 'Varela',
#     'time': 'Flamengo',
# })

# OU

p1.update(nome = 'Aspas', time = 'MIBR')

print(p1)