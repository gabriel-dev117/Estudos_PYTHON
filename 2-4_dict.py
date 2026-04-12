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