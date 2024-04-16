lista = [True, False, "", True, True]

resultado = all(lista)
print(resultado)

lista_pares = [2, 4, 6, 8, 10, 11]
resultado_pares = all(n % 2 == 0 for n in lista_pares)
print(resultado_pares)
