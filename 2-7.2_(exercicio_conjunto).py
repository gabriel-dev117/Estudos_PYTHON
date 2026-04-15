"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando
o segundo número como a duplicação. Retorne a duplicação 
considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da 
    segunda ocorrência do número, ou seja, o número duplicado
    em si.
    Exemplo:
       [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
       [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
       [1, 4, 9, 8, 9, 4, 8] -> (Retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


lista_alternativa = []
n_repetidos = []

for lista in lista_de_listas_de_inteiros:
    lista_alternativa.clear()
    contador = 0
    for n in lista:
        
        if (contador == 0) and (n not in lista_alternativa):
            lista_alternativa.append(n)
            contador += 1
            continue

        elif (contador == 1) and (n not in lista_alternativa) and (n == lista[-1]):
            n_repetidos.append(-1)
            break

        elif (contador == 1) and (n not in lista_alternativa):
            lista_alternativa.append(n)
            continue

        elif (contador == 1) and (n in lista_alternativa):
            n_repetidos.append(n)
            break        


print(n_repetidos)

"""
A princípio vou ter que jogar cada número que o algorítmo ler
dentro de outra lista, e daí o primeiro que for lido que for
repetido, é o dito cujo
"""

"""
Estava pensando eu fazer um um if para um contador;
o contador vai servir para contar quantas vezes o número aparece,
se o contador for igual a 2, ele faz o .append() na n_repetidos e
da o continue
"""
