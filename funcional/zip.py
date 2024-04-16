lista_nomes = ["Ana", "Pedro", "Maria", "João", "Rebeca"]

lista_idade = [23, 48, 32, 39, 19]

lista_estados = ["SP", "CE", "RJ", "RS", "MG"]

resultado = zip(lista_nomes, lista_idade, lista_estados)
# print(dict(resultado))
# print(list(resultado))

for nome, idade, estado in resultado:
    print(f"{nome} tem {idade} anos e mora no esado de {estado}")
