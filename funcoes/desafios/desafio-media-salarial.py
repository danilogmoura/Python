dados_salarial = []


def calcular_media_ponderada():
    valor_total = 0
    quantidade_funcionarios_total = 0

    for cargo in dados_salarial:
        valor_total += cargo["salario"] * cargo["quantidade_funcionarios"]
        quantidade_funcionarios_total += cargo["quantidade_funcionarios"]

    return valor_total / quantidade_funcionarios_total


valor = ""
while valor.lower() != "n":
    cargo = input("Tipo de cargo: ")
    quantidade_funcionarios = int(input("Informe a  Qtde de Funcionários: "))
    salario = int(input("Informe o Salário: "))

    dados_salarial.append({
        "cargo": cargo,
        "quantidade_funcionarios": quantidade_funcionarios,
        "salario": salario
    })

    valor = input("Deseja continuar (S/n): ")

print(f"A média salarial da empresa é {calcular_media_ponderada():.2f}")
