valor = ""
contador = 1
while valor.lower() != "sair":
    valor = input("Informe algo ou sair: ")
    print(f"{contador}. Você digitou {valor}")
    contador += 1

print("Fim!")
