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

def organizar_inverntario(drops):
    inventario = {}

    for nick, item in drops:
        if nick not in inventario:
            inventario[nick] = {
                "slots_ocupados" : 1,
                "itens_coletados" : {item}
            }

        else:
            inventario[nick]["slots_ocupados"] += 1
            inventario[nick]["itens_coletados"].add(item)

    print()
    return inventario

resultado = organizar_inverntario(drops_da_masmorra)

print(resultado)
