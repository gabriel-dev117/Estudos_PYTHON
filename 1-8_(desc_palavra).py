"""
Faça um jogo para o usuário adivinhar qual
a palara secreta.

- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

- Quando o usuário digitar um letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.

Faça a contagem de tentativas do seu
usuário.
"""

# Acho que vou ter que usar len() para verificar cada letra da palavra
# Tá, talvez eu tenha que usar concatenação para conseguir fazer isso
# Acho que vou precisar salvar também as letra que já forma digitas e estão na palavra

import os

palavra = 'redbull'
letra_secreta = ''
tries = 0

while (True): 
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('\nDigite apenas uma letra...')
        continue

     
    if letra_digitada in palavra:
        letra_secreta += letra_digitada

    palavra_formada = ''

    for letra in palavra:
        if letra in letra_secreta:
            palavra_formada += letra

        else:
            palavra_formada += '*'

    tries += 1
    print(f'\nA palavra formada até então é: "{palavra_formada}"\n'
          f'E o você tem {tries} tentativa(s) restante(s).\n')
    
    if palavra_formada == palavra:
        os.system('cls')
        print(f'\nParabéns!! Você achou a palavra "{palavra}".\n'
              f'E utilizou {tries} tentativas.')
        letra_secreta = ''
        palavra_formada = ''
        tries = 0