"""
Lista dentro de lista
"""

salas = [
    #   0        1
    ['Maria', 'Helena'], # 0
    #   0
    ['Elaine'], # 1
    #   0      1         2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # 2
]

# print(salas[0][1]) # Helena
# print(salas[2][2]) # Eduarda
# print(salas[2][3][2]) # 20

for sala in salas:
    for item in sala:
        print(item)