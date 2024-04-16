def somar(a):
    def finalizar_soma(b):
        return a + b

    return finalizar_soma


finalizar_soma = somar(3)
total = finalizar_soma(3)
print(total)

print(somar(3)(4))

SALARIO_BASE = 2113.98
somar_com_salario_base = somar(SALARIO_BASE)

print(somar_com_salario_base(326.02))
