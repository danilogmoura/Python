import random


def sorteador(quantidade=6):
    numeros = []

    if 6 <= quantidade <= 20:
        numeros = random.sample([x for x in range(1, 61)], quantidade)
        numeros.sort()

    return numeros


print(sorteador())
print(sorteador(9))
print(sorteador(12))
print(sorteador(20))
print(sorteador())
