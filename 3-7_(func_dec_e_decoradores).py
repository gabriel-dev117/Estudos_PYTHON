# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar -
# as funções decoradoras em outras funções.


def inverte_string(string):
    return string[::-1]

def is_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('O parametro deve ser uma string')

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)