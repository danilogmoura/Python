funcionario = {
    "nome": "Maria",
    "salario": 7655.22,
    "idade": 35,
    "ativo": True
}

for chave in funcionario:
    print(chave)

for chave in funcionario.keys():
    print(chave)

for valor in funcionario.values():
    print(valor)

for chave in funcionario.keys():
    print(f"chave: {chave}, valor{funcionario[chave]}")

for chave, valor in funcionario.items():
    print(f"{chave} => {valor}")
