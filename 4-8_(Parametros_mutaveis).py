import os
# Problema dos parâmetros mutáveis em função Python

os.system('cls')

"""
def adiciona_clientes(nome, lista = []):
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_clientes('Gabriel', lista1) # Para corrigir, criar uma lista fora da função
print(cliente1)

print()

adiciona_clientes('Cláudia', cliente1)
print(cliente1)

print('-' * 35)

cliente2 = adiciona_clientes('Lúcio')
adiciona_clientes('Maria', cliente2)
print(cliente2)
"""

def adiciona_clientes(nome, lista = None): # Agora toda vez que uma lista não for chamada
    if lista is None:                      # uma nova será criada
        lista = []
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_clientes('Gabriel', lista1) # Para corrigir, criar uma lista fora da função
print(cliente1)

print()

adiciona_clientes('Cláudia', cliente1)
print(cliente1)

print('-' * 35)

cliente2 = adiciona_clientes('Lúcio') # Como a variável armazena uma lista, ela responde como lista
adiciona_clientes('Maria', cliente2)
cliente2.append('Raul')
print(cliente2)

"""
 Observação final: sempre que for criar uma função com parâmetro,
se o parâmetro for mutável, não colocar valor padrão. Em vez disso,
fazer um Parâmetro = None, e trabalhar com isso dentro da função.
 Se colocar um parâmetro mutável, toda vez que chamar a função o 
 parâmetro será o mesmo
"""