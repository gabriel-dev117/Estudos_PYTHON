# count é um iterador sem fim (itertools)
from time import perf_counter
from itertools import count
import os
os.system('cls')



c1 = count(8, 8)
r1 = range(8, 200, 8)


print("-------------------------------------")
print('c1', hasattr(c1, '__iter__'))
print("Significa que 'c1' é um iterável")


print('c1', hasattr(c1, '__next__'))
print("Significa que 'c1' é um iterator")

print("-------------------------------------")

print('r1', hasattr(r1, '__iter__'))
print("Significa que 'r1' é iterável")

print('r1', hasattr(r1, '__next__'))
print("Significa que 'r1' não é um iterator")
print("-------------------------------------")


print("COUNT()")
t1 = perf_counter()
for i in c1:
    if i > 200:
        break

    print(i)
t2 = perf_counter()
t3 = t2 - t1
print(f"O processo levou {t3:.4f}s")

print("----------------------------------------------------")

print("ROUND()")
t4 = perf_counter()
for i in r1:
    print(i)
t5 = perf_counter()
t6 = t5 - t4
print(f"O processo levou {t6:.4f}s")