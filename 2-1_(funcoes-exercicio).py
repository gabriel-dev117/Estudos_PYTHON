# Exercícios com funções

"""
- Crie uma função que multiplica todos os argumentos
  não nomeados recebidos;
- Retorne o total para uma variável e mostre o valor
  da variável.
"""

# Crie uma função que fala se um número é par ou ímpar;
# Retorne se o número é par ou ímpar;

# Lembrar do empacotamento e desempacotamento

"""def mult(*args):
    total = 1
    for n in args:
        total *= n
    print(total)
    return total
    
lista = []

while(True):
    numero = input("Digite um número para os argumentos: [S]sair ")

    if numero == 's':
        print("OK, saindo...")
        break

    try:
        numero = int(numero)
        lista.append(numero)
        continue
    except ValueError:
        print("Algo deu errado, tente novamente...")
        continue


print(f"lista final -> {lista}")
mult(*lista)"""

#--------------------------------------------

def ip(n):
    if n % 2 == 0:
        print(f"O número {n} é par")

    elif n % 2 == 1:
        print(f"O número {n} é ímpar")

    # resultado = print(n % 2 == 0)
    if (n % 2 == 0) == True:
        resultado = 'PAR'

    else:
        resultado = 'ÍMPAR'

    return resultado


numero = int(input("Digite um número: "))

r = ip(numero)

print(f"O resultado foi: {r}")