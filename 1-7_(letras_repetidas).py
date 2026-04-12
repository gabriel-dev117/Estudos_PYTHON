frase = 'Toda vez que eu viajava pela estrada de ouro fino;'\
        'De longe eu avistava a figura de um menino;'\
        'Que corria, abria a porteira, depois vinha me pedindo'\
        'Toque o berrante, seu moço, que eu para eu ficar ouvindo.'

i = 0
qtd_mais_apareceu = 0
a_letra = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu = frase.count(letra_atual)
    
    if qtd_mais_apareceu < qtd_apareceu:
        if letra_atual == ' ':
            i += 1
            continue

        else:
            qtd_mais_apareceu = qtd_apareceu
            a_letra = letra_atual
        
        
    i += 1
   

print(f'A letra que mais apareceu foi "{a_letra}", aparecendo {qtd_mais_apareceu} vezes.')