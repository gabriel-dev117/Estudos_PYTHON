# Exercícios com funções

"""
Crie uma função que multiplica todos os argumentos
não nomeados recebidos,
Retorne o total para uma variável e mostre o valor
da variável.
"""

# primeiro exercício

numeros = []

def mult(*args):
    total = 1
    for n in args:
        total *= n
    return total

while True:
    try:    
        n = input("Digite um número:  [S]-sair\n-> ")
        n = int(n)
        numeros.append(n)

    except:    
        n = n.lower()
        if n == 's':
            print("Saindo da seleção de números.")
            break

        else:
            print("Houve algum problema. Tente novamente")
            continue

multiplicados = mult(*numeros)

print(multiplicados)

#---------------------------------------------------------

"""
Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

def ip(n):
    r = ''
    if (n % 2 == 0):
        r = print(f"O número {n} é par.")
    else:
        r = print(f"O número {n} é ímpar.")

    return r

nu = int(input("Digite um número inteiro: "))

ip(nu)