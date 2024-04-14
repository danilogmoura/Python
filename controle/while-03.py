menu = ["Menu:",
        "----------",
        "1. Opção A",
        "2. Opção B",
        "3. Sair"]

print("\n".join(menu))

opcao_selecionada = 0
while opcao_selecionada != 3:
    opcao_selecionada = int(input("Informe a opção desejada [1-3]: "))

    if opcao_selecionada == 1:
        nome = input("Informe seu nome: ")
        print(f"Seu nome {nome}")
        input("Enter para continuar")
    elif opcao_selecionada == 2:
        email = input("Informe seu e-mail: ")
        print(f"Seu e-mail {email}")
        input("Enter para continuar")
    elif opcao_selecionada == 3:
        print("Tchau!")

print("Fim!")
