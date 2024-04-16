def repetir(funcao, quantidade):
    for _ in range(quantidade):
        funcao()


def bom_dia():
    print("Bom dia!")


# bom_dia()

repetir(bom_dia, 10)
