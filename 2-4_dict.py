# Cridado o dicionário ---------------------------------------------

pessoa = {
    'nome': 'Gabriel Lima',
    'idade': 23,
    'numeros': [ 
        {'whatsapp': '(XX) XXXXX-XXXX', 'ligação': '(XX) XXXXX-XXXX'},
        {'whatsapp': '(XX) XXXXX-XXXX', 'ligação': '(XX) XXXXX-XXXX'},
    ],
}

carro = dict(modelo = 'Chevette', 
             marca = 'Chevrolet', 
             dono = 'Gabriel Moura Lima')

# Chamando o dicionário ---------------------------------------------

# print(f'Nome do sujeito: {pessoa['nome']}\n'
#       f'Idade do sujeito: {pessoa['idade']}')
# print('------------------------------------')
# print(f'Modelo do carro: {carro['modelo']}\n'
#       f'Marca do carro: {carro['marca']}\n'
#       f'Dono(a) do carro: {carro['dono']}')

for info in pessoa:
    print(f'{info}: {pessoa[info]}')

print('------------------------------------')


for chave in carro:
    print(f'{chave}: {carro[chave]}')
print('------------------------------------')

# Para criar chaves depois do dicionário já criado

turma = {}
turma['professor'] = 'Jairo'
print(turma)
print(turma['professor'])
print('------------------------------------')

# Para apagar alguma chave

del carro['dono']
print(carro)
print('------------------------------------')

# Para saber se uma chave existe sem travar o sistema caso ela não exista

if carro.get('dono') is None:
    print('Não existe')

else:
    print(carro['dono'])

#               se existe     se não existe
#                   |               |
print(carro.get('dono',       'sem dono'))