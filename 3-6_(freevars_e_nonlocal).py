def concatenar(linha_inicial):
    valor_final = linha_inicial


    def interna(linha_a_concatenar = ''):
        nonlocal valor_final # se eu não declarar "nonlocal 
                             # para valor_final", eu não consigo 
                             # usa-lo no escopo local
        valor_final += linha_a_concatenar
        return valor_final

    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)