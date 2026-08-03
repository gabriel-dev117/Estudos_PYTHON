# Exercitando decoradores

def processar_comando_local(comando, modelo='mistral'):
    # Linhas de código não escritas
    resposta = f'Ação "{comando}" executada no modelo {modelo}'
    return resposta

# O que decorar:

"""
1 - Antes da execução, imprimir no console "--- Iniciando auditoria do modelo ---".

2 - Executar a função original de forma flexível(ela precisa aceitar qualquer tipo de argumento,
para não quebrar caso o sistema escale).

3 - Depois da execução, contar quantas caracteres tem a string de resposta, imprimir:
'Auditoria concluída. Tamanho da resposta: x caracteres' e, obrigatóriamente, devolver o resultado
original para o sistema continuar rodando.
"""

# -------------------------------------------------------------

def it_works(parametro):
    if not isinstance(parametro, str):
        raise TypeError("Comando/Modelo não válido...")

def criar_funcao(func):
    def interna(*args, **kwargs):
        print("--- Iniciando auditoria do modelo ---")
        for arg in args:
            it_works(arg)
        resultado = func(*args, **kwargs)
        
        qtd_caracteres = len(resultado)
        print(f"Auditoria concluída. Tamanho da resposta: {qtd_caracteres} caracteres.")    
        return resultado
    
    return interna


auditoria_do_processamento = criar_funcao(processar_comando_local)
auditar = auditoria_do_processamento("Ativar stt", "Mistral")  
print(auditar)   