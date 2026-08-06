"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho 
da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

========================================== RESULTADO

lista_soma = [2, 4, 6, 8 ]



lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def soma_lista(x):
    soma = 0
    for i in x:
        soma += i

    return soma

resultado_a = soma_lista(lista_a)
resultado_b = soma_lista(lista_b)


print("-----| Primeiro método |-----")
print(f"A soma dos termos da primeira lista deu {resultado_a}")
print()
print(f"A soma dos termos da segunda lista deu {resultado_b}")
print("-----------------------------")

resultado2_a = sum(lista_a)
resultado2_b = sum(lista_b)

print("-----| Segundo método |-----")
print(f"A soma dos termos da primeira lista deu {resultado2_a}")
print()
print(f"A soma dos termos da segunda lista deu {resultado2_b}")
print("-----------------------------")
"""

# Interpretei o exercício da forma errada, Forma certa a seguir:

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def soma(lista1, lista2):
    size_lista_1 = len(lista1)
    size_lista_2 = len(lista2)
    nova_lista = []

    if size_lista_1 == size_lista_2:
        for i in lista1:
            novo_termo = lista1[i] + lista2[i]
            nova_lista.append(novo_termo)

    menor = min(size_lista_1, size_lista_2)
    for i in range(menor):
        novo_termo = lista1[i] + lista2[i]
        nova_lista.append(novo_termo)

    return nova_lista

resultado = soma(lista_a, lista_b)
print(resultado)

# solução do professor

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])

# print(lista_soma)

lista_soma = [x + y for x, y in zip(lista_a, lista_b)] # q tesão a forma que ele resolveu isso

print(f"lista do professor {lista_soma}")