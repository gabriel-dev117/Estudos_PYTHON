a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Gabriel',
    'Sobrenome': 'Lima'
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print()
print(b1, b2)
print()
print(a1, b1)
print()
print(a2, b2)
print()


# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa ={
    'idade': 23,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)


print()


def mostrar_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    'args4': 4,
    'args5': 5,
}


print()

mostrar_argumentos_nomeados(**configuracoes)