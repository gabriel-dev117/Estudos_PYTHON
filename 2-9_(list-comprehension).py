lista = [(numero + 1) for numero in range(10)]
# print(lista)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

print('Preço original')
print(*produtos, sep= '\n')
print()


novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print('Preços todos alterados')
print(*novos_produtos, sep= '\n')
print()

produtos_selecionados = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 
    else {**produto}
    for produto in produtos
]

print('Somente preços maiores que 20 alterados')
print(*produtos_selecionados, sep= '\n')
print()

teste = [
    (i+1, '-> par')
    if (i+1) %2 == 0 else (i+1, '-> ímpar')
    for i in range(10)
]

print('Teste ímpar-par')
print(teste)
print