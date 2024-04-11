primeiro_nome = "Guilherme"
segundo_nome = "Bianco"

nome_completo = primeiro_nome + " " + segundo_nome
print(nome_completo)

h = input("Informe a hora: ")
m = input("Informe a minutos: ")
s = input("Informe a segundos: ")

data_formatada = "{}h {}m {}s"
print(data_formatada.format(h, m, s))

texto = """
    Este é um exemplo
    de uma string
    que ocupa várias linhas.
"""

print(texto)

print(texto.upper())
print(texto.find("ocupa"))
print(texto.split())

lista_palavras = texto.split()
print(lista_palavras)
print("-".join(lista_palavras))

print(len(texto))

valor = "123456"
print(valor.isnumeric())
print(valor.isdigit())

real = "123.45"
print(real.replace(".", "", 1).isnumeric())
