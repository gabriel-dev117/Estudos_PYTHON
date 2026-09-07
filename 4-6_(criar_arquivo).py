# Criando arquivos em Python
# Usamos a função open para abrir 
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escrever ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo "os", mas :
# os.remove ou unlink - apaga o arquivo
# os.rename - trocar o nome ou move o arquivo
# Vamos falar mais sobre o m´dulo json, mas:
# json.dump = Gera um arquivo json
#json.load

import os

# caminho = "C:\\Users\\estud\\OneDrive\\Documentos\\GABRIEL_DEV\\Criação de arquivo PYTHON\\"
caminho = "4-6_(criar_arquivo).txt"
print(caminho)


"""
#ler o arquivo
arquivo = open(caminho, 'w')

# fechar o arquivo que abriu (open) - extremamente necessário
arquivo.close()
"""

os.system('cls')

"""
# abrir e fechar
with open(caminho, 'w') as arquivo:       #
    # print("Hello World")                #
    # print("arquivo será fechado...")    #
    arquivo.write('Linha 1\n')            #
    arquivo.write('Linha 1')              #
                                          # Abre o arquivo pra escrever
with open(caminho, 'r') as arquivo:       # e
    print("Lendo o primeiro: ")             # depois abre o arquivo para ler
    print(arquivo.read())                 # 


print('-' * 30)


with open(caminho, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2')
    arquivo.seek(0,0) # Voltar o cursor para o início
    print("Lendo o segundo: ") 
    print(arquivo.read())


print('-' * 30)


with open(caminho, 'w+') as arquivo:
    arquivo.writelines(
        ('Linha 1\n', 'Linha 2\n',
         'Linha 3\n', 'Linha 4\n')  # O "writelines" é bom para iteráveis
    )
    arquivo.seek(0,0) # Voltar o cursor para o início 
    print("Lendo o terceiro: ")
    print(arquivo.read())
    print('Lendo o terceiro: ')
    arquivo.seek(0,0)
    print(arquivo.readline(), end = '') # forma 1 de tirar o espaçamento indesejado entre as linhas
    print(arquivo.readline().strip()) # o strip() remove os espaços do começo e do fim
    print(arquivo.readline().strip())
    print(arquivo.readline())


print('-' * 30)


with open(caminho, 'w+') as arquivo:
    arquivo.writelines(
        ('Linha 1\n', 'Linha 2\n',
         'Linha 3\n', 'Linha 4\n')  # O "writelines" é bom para iteráveis
    )
    arquivo.seek(0,0)
    print("Lendo o quarto: ")
    for linha in arquivo.readlines(): # pra ser sincero, iterou perfeitamente, mesmo sem o "readlines"
        print(linha.strip())
"""

with open(caminho, 'w+', encoding = 'utf8') as arquivo: # Usar o "encoding" para especificar o padrão
    arquivo.write('Atenção...\n')
    arquivo.writelines(
        ('Linha 1\n', 'Linha 2\n',
         'Linha 3\n', 'Linha 4\n')  # O "writelines" é bom para iteráveis
    )
    arquivo.seek(0,0)
    print(arquivo.read())