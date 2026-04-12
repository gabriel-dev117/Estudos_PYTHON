def soma(x, y, z):
    print(f'{x=} {y=} {z=} | x + y + z = {x+y+z}')

soma(1, 2, 3)
soma(1, 2, z=5)
print(1, 2, 3, sep='-')

print('\n------------------------------------\n')

def subt(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x - y - z)

    else:
        print(f'{x=} {y=}', x - y)

subt(2, 1)
subt(5, 3)
subt(200, 110)
subt(9, 7, 0)
subt(y=9, z=0, x=7)

print('\n------------------------------------\n')

x = 1

def escopo():
    x = 10

    def outra_funcao():
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)

print('\n------------------------------------\n')

def soma_(x, y):
    if x > 10:
        return [10, 20]
    return x + y # Se o if não for alcançado, ele vai pro próximo passo automaticamente

soma1 = soma_(2, 2)
soma2 = soma_(3, 3)
print(soma1)
print(soma2)
print(soma_(11, 55))