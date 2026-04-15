# Aula 94 (Caótica)

"""
split e join com list e str
split - divide uma string
join - une uma string
strip - corta espaços do início e fim
rstrip - corta espaço da direita
lstrip - corta espaço da esquerda
"""

frase1 = 'Parenteses vazios.'
lista_palavras = frase1.split()
print(lista_palavras)

frase2 = 'Parenteses, mas agora com vírgula.'
lista_palavras2 = frase2.split(',') # A frase foi separada pelo elemento vírgula
print(lista_palavras2)

nome = 'Gabriel Moura Lima'

frases_unidas = '*'.join(nome)
print('*', frases_unidas, '*')