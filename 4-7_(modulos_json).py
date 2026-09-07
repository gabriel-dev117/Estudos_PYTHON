import json
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


"""
pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Lima',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula_4-7.json', 'w', encoding = 'utf8) as arquivo:
    json.dump(
        pessoa, 
        arquivo,
        indent = 2
        ) 
"""

with open('aula_4-7.json', 'r', encoding = 'utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print("Nome:", pessoa['nome'], pessoa['sobrenome'])
    print("Altura:", pessoa['altura'])
    print("Dev:", pessoa['dev'])