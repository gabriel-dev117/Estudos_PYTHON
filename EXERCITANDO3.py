"""
O Exercício é, mostrar o nick do jogador, quantos slots ele tem preenchidos
com quais itens esses slots estão preenchidos e quantos itens tem dentro desse
mesmo slot
"""

logs_masmorra_v3 = [
    ("Kael", "Espada"),
    ("Lyra", "Poção"),
    ("Kael", "Espada"),
    ("Grom", "Escudo"),
    ("Kael", "Gema"),
    ("Lyra", "Poção"),
    ("Grom", "Escudo"),
    ("Kael", "Espada"),
    ("Elara", "Anel"),
    ("Grom", "Poção"),
    ("Elara", "Anel"),
    ("Elara", "Gema")
]

def organizar_drops(drop):
    inventario = {}
    slots = {}

    for nick, item in drop:
        print(f'{inventario} ------ {slots}')


        if (nick not in inventario) and (item not in slots):
            inventario[nick] = {
                'Slots Preenchidos': 1,
                f'{item}' : {f'Qts de {item}' : 1}
            }
            slots.update(slot = item)


        elif (nick in inventario) and (item not in slots):
            inventario[nick]['Slots Preenchidos'] += 1
            inventario[nick].update({f'{item}': {f'Qtd de {item}': 1}})
            slots.update(slot = item)

        else: 
            inventario[nick][f'{item}'][f'Qts de {item}'] += 1

    return inventario, slots

resultado = organizar_drops(logs_masmorra_v3)

print(resultado)

            