"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        - Seu nome é {nome}
        - Seu nome invertido é {nome invertido}
        - Seu nome contém (ou não) espaço
        - Seu nome tem {n} letras
        - A primeira letra do seu nome é {letra}
        - A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
        - "Desculpe, mas você deixou campos em branco."
"""

nome = input("Digite seu nome, por favor: ")
idade = input("Digite sua idade, por favor: ")

if len(nome) > 0 and len(idade) > 0:

    print(f'Seu seu nome é {nome}.')
    
    print(f'Seu seu nome invertido é {nome[::-1]}.')
    
    if ' ' in nome:
        print("Seu nome contém espaço.")
    elif ' ' not in nome:
        print("Seu nome não contém espaço.")
    
    print(f"Seu nome contém '{len(nome)}' letras")

    print(f'A primeira letra do seu nome é "{nome[0]}".')

    print(f'A última letra do seu nome é "{nome[-1]}".')

