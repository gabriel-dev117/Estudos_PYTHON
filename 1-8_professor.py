import os

palavra_secreta = 'cachorro'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('\nDigite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('\nDigite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        
        else:
            palavra_formada += '*'

    print('palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('\nParabéns!! Você acertou a palavra:', palavra_formada)
        print('O número de tentativas foi:', tentativas)
        letras_acertadas = ''
        tentativas = 0
