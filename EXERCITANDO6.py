# Exercício - Adiando execução de funções
# Conserte a função

"""
def soma(x, y):
    return x + y
"""
    
"""
def multiplica(x, y):
    return x * y
"""

"""
def criar_funcao(funcao, *args):
    return funcao(*args)
"""

"""
soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
"""

# ---------------------------------------------------------

"""
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


somar_a_5 = criar_funcao(soma, 5)
mult_por_10 = criar_funcao(multiplica, 10)

print(somar_a_5(3))
print(mult_por_10(6))
"""

# ---------------------------------------------------------

def formatar_log(modulo, mensagem):
   return f"[{modulo.upper()}] -> {mensagem}"
# - Preciso aprimorar a função de cima

def criar_logger(modulo):
    def interna(mensagem):
        return formatar_log(modulo, mensagem)
    return interna

voskstt_msg = criar_logger('VOSK_STT')
ollama_msg = criar_logger('OLLAMA')

print(voskstt_msg("O VOSK_STT ta ativo"))
print()
print(ollama_msg("O Ollama ta ativo"))