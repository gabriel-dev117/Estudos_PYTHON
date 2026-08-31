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

import os

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

drops  = drops_da_masmorra


os.system('cls')

lobby = {}

for player, item in drops:
    if player not in lobby.keys():
        lobby[player] = {item : 1}


    elif item not in lobby[player]:
        lobby[player][item] = 1


    elif item in lobby[player].keys():
        lobby[player][item] += 1



print("-----------------------------")
for jogador, inventario in lobby.items():
    print(jogador, inventario)
print("-----------------------------")

