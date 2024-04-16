lista = [False, False, False, True, False, False]

resultado = any(lista)
print(resultado)

lista_pares = [3, 5, 7, 8, 9, 11]
resultado_tem_algum_par = any(n % 2 == 0 for n in lista_pares)
print(resultado_tem_algum_par)

if resultado_tem_algum_par:
    print("Pelo menos um número é par")
else:
    print("Todos os números são ímpares")
