texto = "Seja bem vindo ao curso de Python"
print("Python" in texto)

lista = [1, 2, 3]
print(3 in lista)
print(7 not in lista)

tupla = ("a", "b", "c")
print("d" not in tupla)
print("a" in tupla)

conjunto = {"banana", "maça", "morango"}
resultado = "morango" in tupla
print(resultado)

dicionario = {
    "nome": "Maria",
    "idade": 31
}

print("nome" in dicionario)
print("Maria" not in dicionario)
print(dicionario["nome"] in "Maria")
