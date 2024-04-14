import os

MENU_INICIAL = ["Menu:",
                "----------",
                "1. Opção A",
                "2. Opção B",
                "3. Sair"]


def limpar_terminal():
    os.environ['TERM'] = 'xterm'
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)


def menu_inicial():
    limpar_terminal()
    print("\n".join(MENU_INICIAL))


def opcao_a():
    limpar_terminal()
    nome = input("Informe o seu nome: ")
    print(f"Seu nome ao contrário é {nome[::-1].lower()}")
    input("Enter para continuar")


def opcao_b():
    limpar_terminal()
    email = input("Informe o seu e-mail: ")
    print(f"O domínio do seu e-mail é {email.split('@')[1]}")
    input("Enter para continuar")


def main():
    continuar = 0
    while continuar != 3:
        menu_inicial()
        continuar = int(input("Selecione [1-3]: "))

        match continuar:
            case 1:
                opcao_a()
            case 2:
                opcao_b()


main()
