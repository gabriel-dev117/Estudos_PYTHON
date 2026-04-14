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
"""
A princípio vou ter que jogar cada número que o algorítmo ler
dentro de outra lista, e daí o primeiro que for lido que for
repetido, é o dito cujo
"""