try: 
    a = 18
    b = 0
    print(b[0])
    # print('Linha 1'[1000])
    c = a/b
    print('Linha 2')

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)

except NameError:
    print('Nome b não está definido')

except (TypeError, IndexError) as error:
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)

except Exception:
    print('Erro Desconhecido')

else:
    print('Execute isso APENAS se o try não gerar exceções. Mas se algo falhar ' \
    'AQUI dentro, deixe o erro estourar livremente')

# No bloco do try, só existe um "else", que será 
# executado somente se nenhum except acontecer


finally:
    print('-----\nNão importa o que acontecer dentro do bloco Try, o que está dentro do' \
    'Finally tentará sempre ser executado\n-----')