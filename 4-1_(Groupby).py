from itertools import groupby

alunos = [
    {'nome' : 'Luiz', 'nota' : 'A'},
    {'nome' : 'Letícia', 'nota' : 'B'},
    {'nome' : 'Fabrício', 'nota' : 'A'},
    {'nome' : 'Rosemary', 'nota' : 'C'},
    {'nome' : 'Joana', 'nota' : 'D'},
    {'nome' : 'João', 'nota' : 'A'},
    {'nome' : 'Eduardo', 'nota' : 'B'},
    {'nome' : 'André', 'nota' : 'A'},
    {'nome' : 'Anderson', 'nota' : 'C'}
]

"""
Para funcionar, é preciso que os dados que 
serão agrupados estejam todos juntos.
Ex.:
aluno = ['a', 'a', 'a', 'a', 'b', 'c', 'a']

*todos aqueles 4 a's ficaram agrupados, já o 5º "a"
surgirá como um novo grupo
"""

"""
Então, por exemplo, se eu quiser agrupar os alunos de
nota "A", dessa lista de cima, eu preciso primeiro ordenar
os alunos que têm nota "A"
"""

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key = ordena)


grupos = groupby(alunos_agrupados, key = ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)