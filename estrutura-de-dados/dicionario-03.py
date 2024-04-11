funcionario = {
    "nome": "João Pedro",
    "idade": 31,
    "cidade": "São Paulo",
    "ativo": True
}

funcionario["ativo"] = False
print(funcionario)

funcionario.update({
    "idade": 27,
    "ativo": True,
    "quantidade_de_filhos": 2,
    "profissao": "Reporter"})
print(funcionario)

cidade = funcionario.pop("cidade")
print(cidade)
print(funcionario)

funcionario.clear()
print(funcionario)