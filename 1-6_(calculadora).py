while True:
    decisao = input('Quer calcular algo? [s]sim  [n]não ')
    if decisao == 'n':
        break
    
    elif decisao == 's':
        n1 = int(input('Qual o primeiro número da sua operação? '))
        op = input('Qual operação deseja fazer?\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\nR:')
        n2 = int(input('Qual o outro do número da operação que você deseja calcular? '))
        
        calculo = ''

        if op == 1:
            calculo = n1 + n2
            op = 'soma'

        elif op == 2:
            calculo = n1 - n2
            op = 'subtração'

        elif op == 3:
            calculo = n1 * n2
            op = 'multiplicação'

        elif op == 4:
            calculo = n1 / n2
            op = 'divisão'
            print(f'A {op} entre {n1} e {n2} resultou {calculo}.')

        print(f'A {op} entre {n1} e {n2} resultou {calculo}.')
        