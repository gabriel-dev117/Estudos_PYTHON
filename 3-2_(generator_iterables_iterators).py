import sys

"""
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)
"""


# O generator ocupa muito menos espaço na memória do que uma lista,
# mas por ser um iterator, somente é possível saber qual o próximo
# item do conjunto; não é possível buscar um item por seu índice, saber o útimo 
# item ou saber quantos itens tem nesse conjunto de elementos.

# A lista ocupa MUITO mais espaço na memória, mas em contra partida, é possível
# saber quantos itens a lista tem e selecionar um elemento por seu índicie.

# --------------------------------------------------------------

def generator(n = 0):
    yield 1  # Pausar
    print("Continuando....")
    yield 2  # Pausar
    print("Mais uma...")
    yield 3  # Pausar
    print("Acabando...")
    return "Acabou"


""" --------
gen = generator(0)
print(next(gen))
print(next(gen))
print(next(gen))
""" 


""" --------
gen = generator(0)
for n in gen:
    print(n)
"""

"""
def generator(n = 0, maximum = 10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return


gen = generator(maximum = 22)
for n in gen:
    print(n)
"""


# ----------------------------------------------------

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g = gen2()

for n in g:
    print(n)