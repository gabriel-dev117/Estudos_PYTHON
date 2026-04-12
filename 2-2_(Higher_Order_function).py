# def saudacao(msg):
#     return msg

# def executa(funcao, msg):
#     return funcao(msg)

# v = executa(saudacao, 'Bom dia')

#---------------------------------------------

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia', 'Gabriel')
s2 = criar_saudacao('Boa noite', 'Gabriel')

print(s1())
print(s2())