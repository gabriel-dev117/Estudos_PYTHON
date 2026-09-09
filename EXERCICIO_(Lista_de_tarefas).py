import os
"""
Exercício - Lista de tarefas com desfazer e refazer
todo = [] -> lista de tarefas
todo = ['fazer café'] -> adicionar "fazer café"
todo = ['fazer café', 'caminhar'] -> Adicionar "caminhar"
desfazer = ['fazer café'] -> refazer ['caminhar']
desfazer = [] -> refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""

"""
to_do = []
apagados = []

def tarefas (acao):
    if acao not in ('refazer', 'desfazer', 'listar'):
        to_do.append(acao)
        return to_do

    if acao == 'listar':
        if len(to_do) == 0:
            return "A lista está vazia :)"

        return to_do

    if acao == 'desfazer':
        if len(to_do) == 0:
            return "A lista está vazia :)"

        
        apagados.append(to_do.pop())

        return to_do

    if acao == 'refazer':
        if len(apagados) == 0:
            return "Você ainda não apagou nenhum item :("

        to_do.append(apagados.pop())

        return to_do

    return "Algo de errado não deu certo KKKKKK"

try:
    while True:
        decisao = input("Digite uma tarefa ou um comando\n(listar, desfazer, refazer)\n -> ").lower()
        if decisao == 'sair':
            os.system('cls')
            input("Aperte ENTER para confirmar a saída")
            os.system('cls')
            break

        else:
            resultado = tarefas(decisao)
            os.system('cls')
            print('----------')
            print(resultado)
            print('----------')
            input("\nAperte ENTER para continuar")
            os.system('cls')

except:
    print("Algo deu errado fora da função")
"""

# Resolução do professor:

import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefa)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefa)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefa)


while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input("Digite uma tarefa ou comando: ")

    comandos = {
        'listar': listar(tarefas),
        'desfazer': desfazer(tarefas),
        'refazer': refazer(tarefas, tarefas_refazer),
        'clear': os.system('cls'),
        'adicionar': adicionar(tarefa, tarefas)
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()



"""
tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
"""