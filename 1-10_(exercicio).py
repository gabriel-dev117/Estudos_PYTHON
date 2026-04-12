lista = []

while(True):
    dec = input('\nPara alterar a lista:\n' \
    '[i] - Inserir\n' \
    '[r] - Remover\n' \
    '[l] - Listar:\n').lower()
    print('')

    if dec == 'i':
        while(True):
            item = input('Qual item deseja inserir na lista?\n')
            lista.append(item)

            dnv_1 = input('Deseja inserir mais algum item na lista?\n').lower()
            if dnv_1 == 'sim':
                continue

            else:
                break


    elif dec == 'r':
        while(True):
            for ind, nome in enumerate(lista):
                print(f'{ind} - {nome}')

            apagar = int(input('\nDigite o índice do item que deseja remover:\n'))
            del lista[apagar]

            dnv_2 = input('Deseja remover mais algum item da lista?\n')
            if dnv_2 == 'sim':
                continue

            else:
                break

    
    elif dec == 'l':
        if len(lista) == 0:
           print('-- A lista está vasia --')

        else:
            for ind, nome in enumerate(lista):
                print(f'{ind} - {nome}') 


    else:
        print('Digite algo válido')