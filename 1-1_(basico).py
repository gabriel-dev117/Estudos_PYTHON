n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")

n1 = int(n1)
n2 = int(n2)

if n1 > n2:
    print(f"{n1} é maior que {n2}.")

elif n2 > n1:
    print(f"{n2} é maior que {n1}.")

elif n1 == n2:
    print("Os números são iguais.")

else:
    print("Você não digitou algum número válido.")