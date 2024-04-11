conjunt_1 = {1, 2, 3}
conjunt_2 = {3, 4, 5}

uniao = conjunt_1.union(conjunt_2)
print(uniao)

intersecao = conjunt_1.intersection(conjunt_2)
print(intersecao)

diferenca = conjunt_1.difference(conjunt_2)
print(diferenca)

diferenca = conjunt_2.difference(conjunt_1)
print(diferenca)

conjunt_2.update({7, 4, 6})
print(conjunt_2)
