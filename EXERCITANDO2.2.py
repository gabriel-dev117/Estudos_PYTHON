import os
"""
Como um inventário funciona:
Vários itens, 
alguns repetidos, outros não,
slots separados por item e 
quantidade limitada de item por slot.
"""

"""
Eu tenho player que se repetem,
tenho itens que se repetem,
quando um item se repetir no mesmo jogador, tenho que apenas somar
"""

os.system('cls')
drops_da_masmorra = [
    ("Kael", "Espada Longa"),
    ("Lyra", "Poção de Vida"),
    ("Grom", "Escudo de Carvalho"),
    ("Kael", "Espada Longa"),        # Kael pegou outra espada igual (Set não deve contar)
    ("Elara", "Anel de Prata"),
    ("Lyra", "Pergaminho de Fogo"),
    ("Grom", "Poção de Vida"),
    ("Kael", "Gema Bruta"),
    ("Lyra", "Poção de Vida"),       # Lyra pegou outra poção igual
    ("Grom", "Escudo de Carvalho"),  # Grom pegou outro escudo igual
    ("Elara", "Gema Bruta"),
    ("Kael", "Poção de Vida")
]

drops = drops_da_masmorra


def inventario(espolio):
    lobby = []
    for player, item in drops:
        jogadores = {}
        if player not in jogadores:
            jogadores[player] = {
                item : 1
            }

        elif (item) in (list(jogadores[player].keys())):
            jogadores[player][item] += 1

        elif (jogadores[player][item] == 50):
            print(f"O slot atingiu a quantidade máxima de {item}")

        else:
            print("Algo deu errado aí viu")

        lobby.append(jogadores)
    return lobby

resultado = inventario(drops)
for jogador in resultado:
    print (jogador)