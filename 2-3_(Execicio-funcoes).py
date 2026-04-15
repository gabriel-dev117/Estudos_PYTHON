"""
Exercício
- Crie funções que dupliquem, tripliquem e quadrupliquem
o número recebido como parâmetro.
"""


# -----------------------------------------------------------

# n = input("Digite um número: ")
# tipo = input("Você inseriu um número modelo 'int' ou 'float'?\n[i]-int  [f]-float\n")
# if tipo == 'i':
#     n = int(n)

# elif tipo == 'f':
#     n = float(n)

# else:
#     print("Algo de errado não está certo...")

# def operacao(v):
#     def duplicar():
#         def triplicar():
#             def quadruplicar():
#                 return v*4
#             return v*3, quadruplicar()
#         return v*2, *triplicar()
#     return duplicar

# r1 = operacao(n)


# print(f"R = {r1()}\nTipo = {type(r1())}")


# EU SOU BOM NESSA POHA KARAAAAAAAAAALHO!!!!!


# -----------------------------------------------------------


n1 = int(input("Digite o número que deseja multiplicar: "))
n2 = int(input("Digite por qual número deseja multiplicar: "))

def multiplicador(v1):
    def multiplo(v2):
        return v1 * v2
    return multiplo

multiplicando = multiplicador(n2)

print(multiplicando(n1))