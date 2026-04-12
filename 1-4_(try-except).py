"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
    
try:    
    n1 = int(input('Digite um número inteiro: '))

    if (n1 % 2 == 0):
        print('Este número é par')

    elif (n1 % 2 == 1):
        print('Este número é ímpar')

except ValueError:
    print('Este não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""
hora = int(input('Digite que horas são: '))

if ((0 <= hora) and (hora <= 11)):
    print('Tenha um bom dia')

elif ((12 <= hora) and (hora <= 17)):
    print('Tenha uma boa tarde')

elif ((18 <= hora) and (hora <= 23)):
    print('Tenha uma boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Escreva seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é muito curto')

elif (5 <= len(nome) <= 6):
    print('Seu nome é curto') 

elif (6 <= len(nome)):
    print('Seu é muito grande')