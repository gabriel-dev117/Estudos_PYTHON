
perguntas = [
    {
        'pergunta': 'Qual a moto mais linda da Honda?',
        'alternativas': ['hornet', 'bros', 'ncx 500', 'cbr 600 rr'],
        'resposta': 'cbr 600 rr'
    },
    {
        'pergunta': 'Qual marca de carros é melhor?',
        'alternativas': ['wolkswagen', 'audi', 'mercedes-benz', 'bmw'],
        'resposta': 'mercedes-benz'
    },
    {
        'pergunta': 'Qual é o melhor personagem de Teen Wolf?',
        'alternativas': ['scott mcall', 'styles stilinsk', 'derek hale', 'deucalion'],
        'resposta': 'styles stilinsk'
    }
]

d2 = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3
}

abc = ['a', 'b', 'c', 'd']
contador = 0
for pergunta in perguntas:
    while True:    
        print(pergunta['pergunta'])
        
        for a, l in zip(pergunta['alternativas'], abc):
            print(f'{l}) {a}')

        try:
            rspst = input('Resposta: ')
            rspst = d2[rspst]
            if pergunta['alternativas'][rspst]  == pergunta['resposta']:
                print('Você acertou ✅!!!\n\n')
                contador += 1
                break

            else:
                print('Você errou ❌!!!\n\n')
                break
        except KeyError:
            print('Esta alternativa não existe, tente outra.\n\n')
            continue
if contador == 0:
    print('PQP, cê não acertou nenhuma, cê é burro?')
else:        
    print(f'Você acertou {contador} de 3.')
