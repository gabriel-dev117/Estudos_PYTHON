i = 0
cpf = []
while (i<9):
    n = int(input(f"Digite o número de índice {i + 1} do CPF desejado: "))
    cpf.append(n)
    i += 1


mult_1 = 10
soma_1 = 0

for n in cpf:
    soma_1 += n * mult_1
    mult_1 -= 1
# soma = (cpf[0] * 10) + (cpf[1] * 9) + (cpf[2] * 8) + (cpf[3] * 7) + (cpf[4] * 6) + (cpf[5] * 5) + (cpf[6] * 4) + (cpf[7] * 3) + (cpf[8]* 2) 

multiplica_1 = soma_1 * 10

dividir_1 = multiplica_1 % 11

p1 = ''
if dividir_1 > 9:
    p1 = 0

elif 0 <= dividir_1 <= 9:
    p1 = dividir_1

else:
    p1 = "Algo deu errado..."


cpf.append(p1)

mult_2 = 11
soma_2 = 0

for n in cpf:
    soma_2 += n * mult_2
    mult_2 -= 1


multiplica_2 = soma_2 * 10

dividir_2 = multiplica_2 % 11

p2 = ''
if dividir_2 > 9:
    p2 = 0

elif 0 <= dividir_2 <= 9:
    p2 = dividir_2

else:
    p2 = "Algo deu errado..."

cpf.append(p2)    

print(f'O primeiro dígito deu {p1}')
print(f'O primeiro dígito deu {p2}')
print(f'O CPF final é: {cpf}')

"""
Se alguém digitar o cpf com os pontos e o traço
eu posso usar o método ".replace()" para tirar eles:

cpf = 012.021.123-32
cpf.replace('.', '')/.replace('-', '')
cpf = 01202112332
"""