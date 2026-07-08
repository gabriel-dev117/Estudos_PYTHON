string = "teste"
inteiro = 2
flutuante = 3.7
booleano = True
lista = [1]
metodo = 'upper'

# Marca um breakpoint no print, chama o debugger, vai em debug console 
# escreve o nome da variável e também dir(nome_da_variável)

#print(string)
#print(inteiro)
#print(flutuante)
#print(booleano)
#print(lista)


# Para saber se uma variável tem determinado método 
# usamos hasattr (has attribute)

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

#          ou

if hasattr(string, metodo):
    print(f'Existe o método .{metodo}()')
    print(getattr(string, metodo)())

else:
    print(f"Não existe esse método .{metodo}()")
