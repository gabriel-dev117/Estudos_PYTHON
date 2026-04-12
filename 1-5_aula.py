nome = 'Gabriel Lima'
tamanho = len(nome)

contador = 0
novo_n = ''
while contador < tamanho:
    letra = nome[contador]
    novo_n += '*' + letra
    contador += 1

novo_n += '*'
print(novo_n)