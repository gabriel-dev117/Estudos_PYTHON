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


# lobby = []
# for player, item in drops:
#     jogadores = {}
#     if (item) in (list(jogadores[player].keys())):
#         jogadores[player][item] += 1

#     elif (jogadores[player][item] == 50):
#         print(f"O slot atingiu a quantidade máxima de {item}")

#     if player not in (p for p in lobby):
#         jogadores[player] = {
#             item : 1
#         }

#     else:
#         print("Algo deu errado aí viu")

#     lobby.append(jogadores)

# for jogador in lobby:
#     print(jogador)
                                                    # set(dict{})

lobby = {}
jogadores = set()
for player, item in drops:
    # jogador = {}
    if player not in list(lobby.keys()):
        lobby[player] = {item : 1}
        print("IF")

    elif (player in list(lobby.keys())) and (item not in lobby[player][item]): # player, item in lobby.items()
        lobby[player][item] += 1
        print("ELSE")



print("-----------------------------")
for i in lobby:
    print(i)
