funcionario = {
    "nome": "João Pedro",
    "idade": 31,
    "cidade": "São Paulo",
    "ativo": True
}

print(funcionario.get("nome"))

# print(funcionario["salario"])
print(funcionario.get("salario"))
print(funcionario.get("salario", 0))

print()
print(funcionario.keys())
print(funcionario.values())
print(funcionario.items())
