l1 = [1, 2, 3, 3 ,3 ,3 ,3 , 1]
s1 = set(l1)
l2 = list(s1) # -> agora l2 é igual l1, mas sem número repetidos e talvez embaralhado

print(3 not in s1) # -> vai retornar False
print(2 in s1) # -> vai retornar True

# melhor forma de descobrir valores estão dentro do set
for n in s1:
    print(n)

# Métodos úteis para set
s2 = set() # -> criando set vazio
s2.add('Gabriel') 
s2.add(77)
s2.update(('Tudo bem?',)) # -> se eu não fizer o update em uma string assim, ela fica toda dividida
#s2.clear() # -> simplesmente limpa o set todo
#s2.discar() # -> para isso funcionar eu preciso saber exatamente oq eu quero remover e escrever dentro do parenteses 
print(s2) # -> como dito antes, set não mantém a ordem

# Operadores úteis:
# união | união (union) -> Uni
# intersecção & (intersection) -> Itens presentes em ambos
# diferença - -> Itens presentes apenas no set da esquerda
# diferença simétrica ^ -> Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # -> RETORNA {1, 2, 3, 4}
s3 = s1 & s2 # -> RETORNA {2, 3}
s3 = s2 - s1 # -> RETORNA {4}
s3 = s1 - s2 # -> RETORNA {1}
s3 = s1 ^ s2 # -> RETORNA {1, 4}; é basicamente "(s1 - s2) | (s2 - s1)"