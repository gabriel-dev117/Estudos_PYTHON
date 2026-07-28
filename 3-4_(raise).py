import os
os.system('cls')
def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError("Não da para dividir qualquer número por zero")
    return True
# essa função vai servir para analisar se um possível denominador é zero,
# se for retorna o erro, se não for, passa direto
 

def nao_aceita_str(n,d):
    if isinstance(n, str):
        raise TypeError(f"'{n}' é uma string, precisa ser um número. {type(n)}")
    
    
    if isinstance(d, str):
        raise TypeError(f"'{d}' é uma string, precisa ser um número. {type(n)}")
    

# Como as funções acima servem como guardiãs e provavelmente retornariam um booleano,
# não é necessário ter return


def divide(n, d):

    nao_aceita_str(n, d)
    nao_aceita_zero(d)
    return n / d

print(divide(8, 2))
