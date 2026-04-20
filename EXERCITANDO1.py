logs_do_sistema = [
    ("gabriel", "iniciar_servidor"),
    ("admin", "atualizar_banco"),
    ("gabriel", "consultar_dados"),
    ("visitante", "login_falho"),
    ("gabriel", "iniciar_servidor"),  # Comando repetido
    ("admin", "reiniciar_sistema"),
    ("visitante", "login_falho"),     # Comando repetido
    ("visitante", "tentativa_acesso")
]

def gerar_relatorio(logs):
    relatorios = {}

    for usuario, acoes in logs:
        if usuario not in relatorios:
            relatorios[usuario] = {
                "total_acoes": 1,
                "acoes_unicas": {acoes}
            }

        else: 
            relatorios[usuario]["total_acoes"] += 1
            relatorios[usuario]["acoes_unicas"].add(acoes)
    
    print()
    return relatorios

 
resultado = gerar_relatorio(logs_do_sistema)

print(resultado)