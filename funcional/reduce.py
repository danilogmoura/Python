from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = reduce(lambda a, b: a + b, numeros, 0)
print(resultado)
