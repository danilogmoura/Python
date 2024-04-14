x = "global"


def minha_funcao():
    # global x
    x = "local"
    print("Dentro da função = ", x)


print("Antes da função = ", x)
minha_funcao()
print("Depois da função = ", x)
